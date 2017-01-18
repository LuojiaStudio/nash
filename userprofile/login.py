from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from userprofile.models import StudentUser, Token
from django.http import JsonResponse


def login(request):
    """
    login wrapper
    :param request:see https://docs.djangoproject.com/en/1.10/ref/request-response for details
    :return:token_key(login successful)
            0(user do not exist)
            1(password error)
    """
    login_token = request.POST['login_token']
    password = request.POST['password']

    login_result = 0
    login_method_list = [
        login_by_username(login_token, password),
        login_by_email(login_token, password),
        login_by_school_number(login_token, password)
    ]

    for item in login_method_list:
        if item == 0:
            pass
        elif item == 1:
            login_result = item
        else:
            login_result = item
            return login_result

    if login_result == 0:
        return JsonResponse({'status': 0, 'message': 0}, safe=False, status=401)
    elif login_result == 1:
        return JsonResponse({'status': 0, 'message': 1}, safe=False, status=401)
    else:
        return JsonResponse({'status': 0, 'message': login_result}, safe=False, status=401)


def login_by_username(username, password):
    """
    :param username:
    :param password:
    :return:token_key(login successful)
            0(user do not exist)
            1(password error)
    """
    user = authenticate(username=username, password=password)
    if user is not None:
        token = create_token(user)
        return token
    else:
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return 0
        else:
            return 1


def login_by_school_number(school_number, password):
    """
    :param school_number:
    :param password:
    :return:token_key(login successful)
            0(user do not exist)
            1(password error)
    """
    try:
        student_user = StudentUser.objects.get(school_number=school_number)
    except StudentUser.DoesNotExist:
        return 0
    else:
        username = student_user.user.username
        return login_by_username(username, password)


def login_by_email(email, password):
    """
    :param email:
    :param password:
    :return:token_key(login successful)
            0(user do not exist)
            1(password error)
    """
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return 0
    else:
        username = user.username
        return login_by_username(username, password)


def create_token(user):
    token = Token.objects.create(user=user)
    return token.key
