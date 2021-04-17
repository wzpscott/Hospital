from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms


def start(request):
    return redirect('/login')


def login(request):
    return render(request, 'HMIS/login.html')


def patientLogin(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/patientIndex/')
    if request.method == "POST":
        pid = request.POST.get('pid')
        password = request.POST.get('password')
        message = '输入为空'
        if pid.strip() and password:
            patient = models.Patient.objects.filter(patientID=pid)
            if not patient:
                message = '用户不存在'
                return render(request, 'HMIS/patientLogin.html', {'message': message})
            patient = patient[0]
            if password != patient.password:
                message = '密码错误'
                return render(request, 'HMIS/patientLogin.html', {'message': message})

            request.session['is_login'] = True
            request.session['pid'] = pid
            return redirect('/patientIndex/')
        return render(request, 'HMIS/patientLogin.html', {'message': message})
    return render(request, 'HMIS/patientLogin.html')


def logout(request):
    if request.session.get('is_login', None):
        request.session['is_login'] = False
        return redirect('/login/')


def doctorLogin(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/doctorIndex/')
    if request.method == "POST":
        did = request.POST.get('did')
        password = request.POST.get('password')
        message = '输入为空'
        if did.strip() and password:
            doctor = models.Doctor.objects.filter(doctorID=did)
            if len(doctor) == 0:
                message = '用户不存在'
                return render(request, 'HMIS/doctorLogin.html', {'message': message})
            doctor = doctor[0]
            if password != doctor.password:
                message = '密码错误'
                return render(request, 'HMIS/doctorLogin.html', {'message': message})

            request.session['is_login'] = True
            request.session['did'] = did

            return redirect('/doctorIndex/')
        return render(request, 'HMIS/doctorLogin.html', {'message': message})
    return render(request, 'HMIS/doctorLogin.html')


def patientRegister(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        pname = request.POST.get('pname')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not (pid and pname and password1 and password2):
            message = '输入为空'
            render(request, 'HMIS/patientRegister.html', {'message': message})

        if models.Patient.objects.filter(patientID= pid):
            message = '用户已注册'
            render(request, 'HMIS/patientRegister.html', {'message': message})

        if password1 != password2:
            message = '两次输入密码不一致'
            render(request, 'HMIS/patientRegister.html', {'message': message})

        new_patient = models.Patient()
        new_patient.patientID = pid
        new_patient.password = password1
        new_patient.name = pname
        new_patient.save()

        return redirect('/patientLogin/')
    return render(request, 'HMIS/patientRegister.html')


def doctorRegister(request):
    if request.method == "POST":
        did = request.POST.get('did')
        dname = request.POST.get('dname')
        department = request.POST.get('department')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not (did and dname and password1 and password2 and department):
            message = '输入为空'
            render(request, 'HMIS/doctorRegister.html', {'message': message})

        if models.Doctor.objects.filter(doctorID=did):
            message = '用户已注册'
            render(request, 'HMIS/doctorRegister.html', {'message': message})

        if password1 != password2:
            message = '两次输入密码不一致'
            render(request, 'HMIS/doctorRegister.html', {'message': message})

        new_doctor = models.Doctor()
        new_doctor.doctorID = did
        new_doctor.password = password1
        new_doctor.name = dname
        new_doctor.department = department
        new_doctor.save()
        return redirect('/doctorLogin/')
    return render(request, 'HMIS/doctorRegister.html')


def patientIndex(request):
    return render(request, 'HMIS/patientIndex.html')


def doctorIndex(request):
    pass
    return render(request, 'HMIS/doctorIndex.html')


def patientInfo(request):
    pid = request.session['pid']
    patient = models.Patient.objects.get(patientID=pid)
    return render(request, 'HMIS/patientInfo.html', {'patient':patient})


def doctorInfo(request):
    did = request.session['did']
    doctor = models.Doctor.objects.get(doctorID=did)
    return render(request, 'HMIS/doctorInfo.html', {'doctor':doctor})


def registration(request):
    message = ''
    departments = models.Doctor.department_choices
    dic = {k[0]: [] for k in departments}
    for k in dic:
        dic[k] = models.Doctor.objects.filter(department=k)
    if request.method == "POST":

        did = request.POST.get('did')
        pid = request.session.get('pid')
        doctor = models.Doctor.objects.get(doctorID=did)
        patient = models.Patient.objects.get(patientID=pid)
        if doctor.num == 0:
            message = '已挂满'
            return render(request,'HMIS/registration.html',{'dic':dic,'message':message})
        doctor.num -= 1
        doctor.save()

        record = models.RegistrationRecord()
        record.doctor = doctor
        record.patient = patient
        record.save()
        message = '挂号成功'
        return render(request, 'HMIS/registration.html', {'dic': dic, 'message': message})
    return render(request, 'HMIS/registration.html',{'dic':dic,'message':message})


def registrationRecord(request):
    did = request.session['did']
    doctor = models.Doctor.objects.get(doctorID=did)
    records = models.RegistrationRecord.objects.filter(doctor=doctor)
    if request.method == 'POST':
        record_id = request.POST.get('id')
        record = models.RegistrationRecord.objects.get(id=record_id)
        request.session['record_id'] = record.id
        return redirect('/doctorIndex/treatment')
    return render(request, 'HMIS/registrationRecord.html', {'doctor':doctor,'records':records})


def treatment(request):
    record_id = request.session['record_id']
    record = models.RegistrationRecord.objects.get(id=record_id)
    if request.method == 'POST':
        diagnosis = request.POST.get('diagnosis')
        treatment_record = models.TreatmentRecord()
        treatment_record.patient = record.patient
        treatment_record.doctor = record.doctor
        treatment_record.diagnosis = diagnosis
        treatment_record.registration = record
        treatment_record.save()
        record.isActive = False
        record.save()
        return redirect("/doctorIndex")
    return render(request, 'HMIS/treatment.html', {'record': record})
