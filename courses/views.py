from django.shortcuts import render  # Import render for rendering templates (not used here)
from rest_framework.views import APIView  # Import APIView for class-based API views
from django.http import JsonResponse  # Import JsonResponse to return JSON responses
from rest_framework import status  # Import status codes for HTTP responses
from .models import *  # Import all models from the current app
from .serlizers import *  # Import all serializers from the current app

# Create your views here.

class lmsSignupUser(APIView):  # API view for user signup
    def post(self, request):  # Handle POST requests
        userdata = lmsSignupSerializer(data=request.data)  # Deserialize and validate incoming data
        if userdata.is_valid():  # If data is valid
            lmsUser.objects.create(**userdata.validated_data)  # Create a new user with validated data
            return JsonResponse({"message": "User created successfully"}, status=status.HTTP_201_CREATED)  # Return success response
        return JsonResponse(userdata.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if data is invalid

class lmsGetUserDetails(APIView):  # API view to get all user details
    def get(self, request):  # Handle GET requests
        result = list(lmsUser.objects.all().values())  # Get all users as a list of dictionaries
        return JsonResponse(result, safe=False, status=status.HTTP_200_OK)  # Return user data as JSON




class lmsUpdateEmail(APIView):  # API view to update user email
    def put(self, request):
        userdata = lmsUpdateEmailSerializer(data=request.data)
        if userdata.is_valid():
            email = userdata.data["email"]
            number = userdata.data["number"]
            lmsUser.objects.filter(number=number).update(email=email)
            message = {"message": "Email updated successfully"}
            return JsonResponse(message, status=status.HTTP_200_OK)
        return JsonResponse(userdata.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
class lmsDeleteUser(APIView):  # API view to delete a user
    def delete(self, request, number):
        lmsUser.objects.filter(number=number).delete()
        message = {"message": "User deleted successfully"}
        return JsonResponse(message, status=status.HTTP_204_NO_CONTENT)  # Return success message after deletion
    
