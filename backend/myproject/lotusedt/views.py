from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
import json
import jwt
from rest_framework.decorators import api_view
from .models import StudentModel
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

# Create your views here.

from django.conf import settings


# this is for checking user is admin or not
def is_admin(user):
    if user.role != 'admin':
        # return JsonResponse("erre")
        raise PermissionDenied("You must be an admin to access this page.")
    return True

def is_user(user):
    if user.role != "user":
        raise PermissionDenied("You must be an user to do this task")
    return True


# just basic checking route
def welcome_path(request):
    return HttpResponse("Welcome to the Django Greetings App!")




            #  ALL ABOUT STUDENT PART #
# register route
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            name = data.get('name')
            email = data.get('email')
            password = data.get('pass')
            role = data.get('role', 'student')  # Default to 'user' if role is not provided


             # Validate required fields
            if not all([name, email, password]):
                return JsonResponse({"ok": False, "msg": "All fields are required to fill"})
            
            # Check if user already exists
            if StudentModel.objects.filter(email=email).exists():
                return JsonResponse({"ok": False, "msg": "User already exists"})

            # Hash the password
            pass_hash = make_password(password)

            user = StudentModel(name=name, email=email, pass_hash=pass_hash, role=role)
            user.save()

            return JsonResponse({"ok": True, "msg": "Registered Successfully"})
        except Exception as e:
            return JsonResponse({"ok": False, "msg": str(e)})
        

# login route
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            email = data.get('email')
            password = data.get('pass')  # Get the user-entered password

           
            user = StudentModel.objects.filter(email=email).first()

             # Validate required fields
            if not all([email, password]):
                return JsonResponse({"ok": False, "msg": "All fields are required to fill"})
            
            if not user:
                return JsonResponse({"ok": False, "msg": "User with this email not found"})

               
            stored_hashed_password = user.pass_hash
            hashed_entered_password = make_password(password)

    
            if not check_password(password, user.pass_hash):  # Compare the passwords
                return JsonResponse({"ok": False, "msg": "Invalid email or password"})

            payload = {"userId": user.id}
            secret_key = "rajtupe987"  # Replace with your actual secret key
            token = jwt.encode(payload, secret_key, algorithm='HS256').decode('utf-8')  # Decode the bytes to string

            response = {
                "ok": True,
                "token": token,
                "msg": "Login Successful",
                "id": user.id,
                "userName": user.name,
                "role":user.role
            }

            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok": False, "msg": str(e)})



@api_view(['DELETE'])
def delete_student(request, student_id):

    try:
        student = StudentModel.objects.get(id=student_id)
    except StudentModel.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    student.delete()
    return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)





            

# ALL about instructor



from .models import Instructor
from .serializers import InstructorSerializer

@api_view(['POST'])
def create_instructor(request):

    if request.method == 'POST':
        data = request.data.copy()  # Create a copy of the data to manipulate
        password = data.pop('password')  # Remove the password from data
        
         # Check if an instructor with the provided email already exists
        email = data.get('email')
        if Instructor.objects.filter(email=email).exists():
            return Response({"error": "An instructor with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Hash the password using Django's make_password function
        hashed_password = make_password(password)

        # Add the hashed password back to the data
        data['password'] = hashed_password

        serializer = InstructorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



# login route
@api_view(['POST'])
def varifyintructor(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            email = data.get('email')
            password = data.get('password')  # Get the user-entered password

           
            user = Instructor.objects.filter(email=email).first()

             # Validate required fields
            if not all([email, password]):
                return JsonResponse({"ok": False, "msg": "All fields are required to fill"})
            
            if not user:
                return JsonResponse({"ok": False, "msg": "User with this email not found"})

               
            stored_hashed_password = user.password
            hashed_entered_password = make_password(password)

    
            if not check_password(password, user.password):  # Compare the passwords
                return JsonResponse({"ok": False, "msg": "Invalid email or password"})

            payload = {"userId": user.id}
            secret_key = "rajtupe987"  # Replace with your actual secret key
            token = jwt.encode(payload, secret_key, algorithm='HS256').decode('utf-8')  # Decode the bytes to string

            response = {
                "ok": True,
                "token": token,
                "msg": "Login Successful",
                "id": user.id,
                "name": user.first_name
            }

            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok": False, "msg": str(e)})
