#coding: utf-8

from rest_framework import serializers

from myauth.models import User

class PickledObjectFieldSerializer(serializers.WritableField):

    def to_native(self, obj):
        return obj


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'avatar',
            'created_at',
            'updated_at',
            'is_delete',
            'is_admin',
        )
