from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=12)
    age = serializers.IntegerField()
