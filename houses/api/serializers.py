
from rest_framework import serializers
from ..models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House  # 要序列化的模型
        fields = '__all__'  # 要序列化的字段
