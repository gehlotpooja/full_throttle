from task_app.serializers import TaskSerializer
from task_project.config import *
from .models import *
from django.db.models import Q


def save_org(request):
    success = False
    msg = 'No data'
    try:
        org_list = []
        for org_name in DEFAULT_ORG_LIST:
            org_obj = Organisation()
            org_obj.name = org_name
            org_list.append(org_obj)
        Organisation.objects.bulk_create(org_list)
        success = True
        msg = 'org data saved successfully'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg':msg}


def register(request):
    msg = 'not able to save data'
    success = False
    try:
        post_data = request.POST

        if post_data.get('password') == post_data.get('confirm_password'):
            user_obj = User()
            user_obj.email = post_data.get('email')
            user_obj.first_name = post_data.get('firstName')
            user_obj.last_name = post_data.get('lastName')
            user_obj.set_password(post_data.get('password'))
            user_obj.username = post_data.get('username')
            user_obj.is_staff = True
            user_obj.save()
            user_id = user_obj.id
            user_profile_obj = UserProfile()
            user_profile_obj.user_id = user_id
            user_profile_obj.org_id = post_data.get('org_id')
            user_profile_obj.mobile_number = post_data.get('mobile_no')
            user_profile_obj.address = post_data.get('address')
            user_profile_obj.add_latitude = post_data.get('longitude')
            user_profile_obj.add_longitude = post_data.get('latitude')
            user_profile_obj.save()

            msg = 'User data saved successfully'
            success = True

    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}


def add_task(request):
    msg = 'not able to save data'
    success = False
    try:
        post_data = request.POST
        assigned_to_id = post_data.get('assigned_to')
        task_obj = Task()
        user_profile_obj = UserProfile.objects.filter(user_id = request.user.id)
        user_profile_obj = user_profile_obj[0]
        assigned_user_profile = UserProfile.objects.filter(user_id = assigned_to_id, org_id = user_profile_obj.org_id)
        if assigned_user_profile:
            assigned_user_profile = assigned_user_profile[0]
            task_obj.org_id = user_profile_obj.org_id
            task_obj.assigned_by_id = user_profile_obj.id

            task_obj.assigned_to_id = assigned_user_profile.id
            task_obj.name = post_data.get('task_name')
            task_obj.status = post_data.get('status')
            task_obj.save()
            msg = 'Task data saved successfully'
            success = True
        else:
            msg = 'Assign task within the organisation'
            success = False

    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}


def get_task(request):
    success = False
    msg = 'No data'
    try:
        user_id = request.GET.get('user_id')
        extra_filter = Q()
        if user_id:
            extra_filter = Q(assigned_to_id=user_id)
        obj = Task.objects.filter(extra_filter)
        serializer = TaskSerializer(obj, many=True)
        data = serializer.data
        success = True
        msg = 'Success in getting view data.'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg':msg, 'data': data}

