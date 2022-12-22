
from rest_framework import serializers 
from .models import Team

class TeamSerializer(serializers.ModelSerializer):

    members_count = serializers.IntegerField(read_only=True)
    members = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='profile-detail')
    manager = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')

    class Meta:
        model = Team
        fields = ['url', 'id', 'image', 'name', 'created_on',
        'manager', 'description', 'members_count', 'members', 'points',
        'completed_tasks_count', 'notcompleted_tasks_count']
        read_only_fields = ['points', 'completed_tasks_count', 'notcompleted_tasks_count']