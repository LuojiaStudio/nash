from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


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
    school = models.ForeignKey(
        'College',
        related_name='student_union_of',
        on_delete=models.SET_NULL,
        null=True
    )


class DepartmentInCollegeStudentUnion(Department):
    """
    lower than the department in Wuhan University Student Union
    """
    college_student_union = models.ForeignKey(
        CollegeStudentUnion,
        related_name='departments_in',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.college_student_union + self.name


class Position(models.Model):
    """
    position in department(only department in college student union and department in Wuhan University Student Union)
    """
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='position_in',
    )
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=20)
    faculty = models.ForeignKey(
        Faculty,
        related_name='college_in',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Area(models.Model):
    """
    the area where the dormitory is located
    """
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Dormitory(models.Model):
    area = models.ForeignKey(
        Area,
        related_name='dormitory_in',
        on_delete=models.SET_NULL,
        null=True
    )
    dormitory_serial_number = models.CharField(max_length=10)

    def __str__(self):
        return self.area + self.dormitory_serial_number


class StudentUser(models.Model):
    """
    include normal student and staff in student union
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_id = models.CharField(max_length=15)
    college = models.ForeignKey(
        College,
        related_name='user_in',
        on_delete=models.SET_NULL,
        null=True
    )
    dormitory = models.ForeignKey(
        Dormitory,
        related_name='user_in',
        on_delete=models.SET_NULL,
        null=True
    )
    house_number = models.CharField(max_length=10)
    personal_info = JSONField()
    setting_info = JSONField()

    def __str__(self):
        return self.user.username


class Staff(models.Model):
    """
    staff in Wuhan University Student Union and College Student Union
    """
    user = models.OneToOneField(StudentUser, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department,
        related_name='staff_in',
        on_delete=models.CASCADE
    )
    position = models.ForeignKey(
        Position,
        related_name='staff_in',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user














































