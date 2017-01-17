from django.contrib import admin
from userprofile.models import \
    JobTitle, \
    CollegeStudentUnion, \
    StudentUser, \
    Staff, \
    DepartmentInCollegeStudentUnion, \
    DepartmentInSchoolStudentUnion, \
    College, \
    Faculty, \
    Area, \
    Dormitory

# Register your models here.
admin.site.register(JobTitle)
admin.site.register(CollegeStudentUnion)
admin.site.register(StudentUser)
admin.site.register(Staff)
admin.site.register(DepartmentInSchoolStudentUnion)
admin.site.register(DepartmentInCollegeStudentUnion)
admin.site.register(College)
admin.site.register(Faculty)
admin.site.register(Area)
admin.site.register(Dormitory)
