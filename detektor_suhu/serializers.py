from rest_framework import serializers

from detektor_suhu.models import Stats


class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'