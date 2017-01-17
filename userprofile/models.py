import binascii
import os

from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import JSONField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):
    """
    abstract model and be inherited by Department in School Student Union
    and CollegeStudentUnion(e.g. Computer College Student Union)
    """
    class Meta:
        abstract = True

    name = models.CharField(max_length=15)
    job_titles = GenericRelation('JobTitle')

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
        return self.college_student_union.name + self.name


class JobTitle(models.Model):
    """
    position in department(only department in college student union and department in Wuhan University Student Union)
    using Django generic relation, see the official documentation for details
    """
    group = models.OneToOneField(Group, null=True)
    department_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    department_object_id = models.PositiveIntegerField()
    department_object = GenericForeignKey('department_type', 'department_object_id')
    tag = models.CharField(max_length=10)

    def __str__(self):
        return self.department_object.name + self.tag


class College(models.Model):
    name = models.CharField(max_length=20)
    faculty = models.ForeignKey(
        'Faculty',
        related_name='college_in',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name


class Faculty(models.Model):
    """
    [xin xi xue bu, wen li xue bu, gong xue bu, yi xue bu]
    """
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
        return self.area.name + self.dormitory_serial_number


class StudentUser(models.Model):
    """
    include normal student and staff in student union
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_number = models.CharField(max_length=15)
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
    house_number = models.CharField(max_length=10, null=True)
    personal_info = JSONField(null=True)
    setting_info = JSONField(null=True)

    def __str__(self):
        return self.user.username


class Staff(models.Model):
    """
    staff in Wuhan University Student Union and College Student Union
    """
    user = models.OneToOneField(StudentUser, on_delete=models.CASCADE)
    job_title = models.ForeignKey(
        JobTitle,
        related_name='staff_in',
        on_delete=models.CASCADE
    )

    def get_department(self):
        return self.job_title.department_object

    def __str__(self):
        return self.user.__str__() + self.job_title.__str__()


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    @staticmethod
    def generate_key():
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key














































