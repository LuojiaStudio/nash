from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    """
    abstract model and be inherited by Department in School Student Union
    and CollegeStudentUnion(e.g. Computer College Student Union)
    """
    class Meta:
        abstract = True

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class DepartmentInSchoolStudentUnion(Department):
    """
    departments in Wuhan University Student Union
    """


class CollegeStudentUnion(Department):
    """
    regard College Student Union(e.g. Computer College Student Union) as a department
    """
    school = models.ForeignKey(College)


class College(models.Model):
    name = models.CharField(max_length=20)
    faculty = models.ForeignKey(Faculty)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PositionInDepartment(models.Model):
    """
    position in department
    """
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name













































