from django.test import TestCase
from userprofile.models import StudentUser, Staff, Token
from django.contrib.auth.models import User
from userprofile.login import login_by_username, login_by_school_number, login_by_email, create_token


class LoginTestCase(TestCase):
    user_case = {
        'name': 'john',
        'email': 'john@gmail.com',
        'password': 'johnPassword',
        'school_number': '2014301500228'
    }

    def setUp(self):
        user = User.objects.create_user(
            self.user_case['name'],
            self.user_case['email'],
            self.user_case['password']
        )
        StudentUser.objects.create(user=user, school_number=self.user_case['school_number'])

    def test_login_by_username(self):
        case_1 = {
            'username': self.user_case['name'],
            'password': self.user_case['password']
        }
        case_2 = {
            'username': self.user_case['name'],
            'password': 'wrongPassword'
        }
        case_3 = {
            'username': 'wrongUsername',
            'password': self.user_case['password']
        }
        self.assertEqual(
            type(login_by_username(case_1['username'], case_1['password'])) is str,
            True
        )
        self.assertEqual(
            login_by_username(case_2['username'], case_2['password']),
            1
        )
        self.assertEqual(
            login_by_username(case_3['username'], case_3['password']),
            0
        )

    def test_login_by_email(self):
        case_1 = {
            'username': self.user_case['email'],
            'password': self.user_case['password']
        }
        case_2 = {
            'username': self.user_case['email'],
            'password': 'wrongPassword'
        }
        case_3 = {
            'username': 'wrongUsername',
            'password': self.user_case['password']
        }
        self.assertEqual(
            type(login_by_email(case_1['username'], case_1['password'])) is str,
            True
        )
        self.assertEqual(
            login_by_email(case_2['username'], case_2['password']),
            1
        )
        self.assertEqual(
            login_by_email(case_3['username'], case_3['password']),
            0
        )

    def test_login_by_school_number(self):
        case_1 = {
            'username': self.user_case['school_number'],
            'password': self.user_case['password']
        }
        case_2 = {
            'username': self.user_case['school_number'],
            'password': 'wrongPassword'
        }
        case_3 = {
            'username': 'wrongUsername',
            'password': self.user_case['password']
        }
        self.assertEqual(
            type(login_by_school_number(case_1['username'], case_1['password'])) is str,
            True
        )
        self.assertEqual(
            login_by_school_number(case_2['username'], case_2['password']),
            1
        )
        self.assertEqual(
            login_by_school_number(case_3['username'], case_3['password']),
            0
        )

    def test_create_token(self):
        user = User.objects.get(username=self.user_case['name'])
        token = create_token(user)
        self.assertEqual(type(token) is str, True)
