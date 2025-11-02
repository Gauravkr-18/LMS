from rest_framework import serializers

class lmsSignupSerializer(serializers.Serializer):  
    userName = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    number = serializers.CharField()  
    password = serializers.CharField(max_length=20)
    userType = serializers.CharField(max_length=20)
    gender = serializers.CharField(max_length=10, allow_null=True, allow_blank=True)

class lmsUpdateEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    number = serializers.CharField()  