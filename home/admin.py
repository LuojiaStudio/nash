from django.contrib import admin
from userprofile.models import JobTitle, CollegeStudentUnion, StudentUser, Staff
# Register your models here.
admin.site.register(JobTitle)
admin.site.register(CollegeStudentUnion)
admin.site.register(StudentUser)
admin.site.register(Staff)