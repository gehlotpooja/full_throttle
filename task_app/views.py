from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .controllers import *
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

'''Takes organisation name from task_project.config.py and save them all at one shot using bulk_create'''
@api_view(['POST'])
@permission_classes((AllowAny,))
def save_org_api(request):
    data = {
        'success': False,
        'msg': 'No data to save',
    }
    try:
        data = save_org(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


'''This api is used for registering users'''
@api_view(['POST'])
@permission_classes((AllowAny,))
def register_api(request):
    data = {
        'msg': 'Enter valid data',
        'success': 'False'
    }
    try:
        data = register(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


'''This api is used by logged in user to add task and assign it to other user within the same organisation'''
@api_view(['POST'])
def add_task_api(request):
    data = {
        'msg': 'Enter valid data',
        'success': 'False'
    }
    try:
        data = add_task(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


'''This api allows user to login using username and password with the help of token authentication'''
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


'''This api gets all the task which has been asked to the user for which user_id needs to be passed from front end'''
@api_view(['GET'])
def get_task_api(request):
    data = {
        'msg': 'Enter valid data',
        'success': 'False'
    }
    try:
        data = get_task(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def delete(request):
    task = Task.objects.filter().delete()
    data = 'deleted'
    return Response(data=data)
