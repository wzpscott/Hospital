from django.db import models


class Student(models.Model):
    gender_choices = (
        ('male', "男"),
        ('female', "女"),
    )
    student_id = models.CharField(max_length=8,unique=True)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=256)
    gender = models.CharField(max_length=32, choices=gender_choices)
    age = models.IntegerField(null=True)
    department = models.CharField(max_length=32,null=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Patient(models.Model):
    patientID = models.CharField(max_length=8, unique=True, primary_key=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    doctorID = models.CharField(max_length=8, unique=True, primary_key=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=15)
    numLimit = models.IntegerField(default=0,null=True)
    num = models.IntegerField(default=0,null=True)
    department_choices = (
        ('ophthalmology', '眼科'),
        ('dentistry', '牙科'),
    )
    department = models.CharField(max_length=32, choices=department_choices)

    def __str__(self):
        return self.name


class RegistrationRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    regTime = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.patient.patientID+'-'+self.doctor.doctorID+'-'+str(self.regTime)

    class Meta:
        ordering = ["-regTime"]


# class TreatmentPlan(models.Model):
#     doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     numLimit = models.IntegerField(default=0)
#     num = models.IntegerField(default=0)


class TreatmentRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    registration = models.ForeignKey(RegistrationRecord, on_delete=models.CASCADE)
    diagnosis = models.TextField(max_length=1000)
    treTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.patientID+'-'+self.doctor.doctorID+'-'+str(self.treTime)

    class Meta:
        ordering = ["-treTime"]