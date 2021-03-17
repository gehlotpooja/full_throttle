from rest_framework import serializers
from .models import *
from task_project.config import *

class TaskSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()
    assigned_to = serializers.CharField(source='assigned_to.user.get_full_name')
    assigned_by = serializers.CharField(source='assigned_by.user.get_full_name')
    status = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'date', 'time', 'assigned_to', 'assigned_by', 'status')


    def get_status(self, obj):
        try:
            if obj.status:
                return DEFAULT_STATUS_DICT.get(obj.status)
        except Exception as e:
            print(e.args)
        return ''

    def get_time(self, obj):

        h = int(obj.date.strftime("%H"))
        if h>12:
            H = h-12
            return obj.date.strftime(str(H)+":%M:%S PM")
        else:
            return obj.date.strftime("%H :%M:%S AM")

    def get_date(self, obj):
        return obj.date.strftime("%b %d,%Y ")