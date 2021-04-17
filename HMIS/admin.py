from django.contrib import admin
from . import models

admin.site.register(models.Student)
admin.site.register(models.Patient)
admin.site.register(models.Doctor)
admin.site.register(models.RegistrationRecord)
# admin.site.register(models.TreatmentPlan)
admin.site.register(models.TreatmentRecord)

