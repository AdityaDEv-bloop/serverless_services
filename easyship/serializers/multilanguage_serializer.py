from rest_framework import serializers


class TranslateSerializer(serializers.Serializer):
    language = serializers.CharField()
    content = serializers.ListField()
