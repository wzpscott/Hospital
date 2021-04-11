from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms

def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'HMIS/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')

    if request.method == "POST":
        log_form = forms.StudentForm(request.POST)
        if log_form.is_valid():
            student_id = log_form.cleaned_data.get('student_id')
            password = log_form.cleaned_data.get('password')

            if not models.Student.objects.filter(student_id=student_id).exists():
                message = '用户不存在'
                return render(request, 'HMIS/login.html', locals())

            user = models.Student.objects.get(student_id=student_id)

            if user.password != password:
                message = '密码错误'
                return render(request, 'HMIS/login.html', locals())

            request.session['is_login'] = True
            request.session['user_id'] = user.student_id
            request.session['user_name'] = user.name
            return redirect('/index/')
    log_form = forms.StudentForm()
    return render(request, 'HMIS/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)

        if register_form.is_valid():
            student_id = register_form.cleaned_data.get('student_id')
            name = register_form.cleaned_data.get('name')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'HMIS/register.html', locals())
            else:
                same_name_user = models.Student.objects.filter(name=student_id)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'HMIS/register.html', locals())

                new_user = models.Student()
                new_user.student_id = student_id
                new_user.name = name
                new_user.password = password1
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')

    register_form = forms.RegisterForm()
    return render(request, 'HMIS/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")


def reimbursement(request):
    return render(request, 'HMIS/reimbursement.html')


def registration(request):
    return render(request, 'HMIS/registration.html')