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
from .models import StudentModel,Expertise,Course
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

# Create your views here.

from django.conf import settings


# this is for checking user is admin or not

# just basic checking route
def welcome_path(request):
    return HttpResponse("Welcome to the Django Greetings App!")




            #  ALL ABOUT STUDENT PART #





# ALL about student  

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





            

# ALL about instructor

from .models import Instructor
from .serializers import InstructorSerializer,ExpertiseSerializer
   

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








# ALL about Admin


@api_view(['POST'])
def create_expertise(request):
    if request.method == 'POST':
        serializer = ExpertiseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

@api_view(['POST'])
def create_instructor(request):
    if request.method == 'POST':
        data = request.data.copy()  # Create a copy of the data to manipulate
        password = data.pop('password')  # Remove the password from data

        email = data.get('email')
        if Instructor.objects.filter(email=email).exists():
            return Response({"error": "An instructor with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Hash the password using Django's make_password function
        hashed_password = make_password(password)

        # Add the hashed password back to the data
        data['password'] = hashed_password

        serializer = InstructorSerializer(data=data)
        if serializer.is_valid():
            instructor = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_all_expertise(request):
    if request.method == 'GET':
        expertise = Expertise.objects.all()
        serializer = ExpertiseSerializer(expertise, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['DELETE'])
def delete_student(request, student_id):

    try:
        student = StudentModel.objects.get(id=student_id)
    except StudentModel.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    student.delete()
    return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



from rest_framework.decorators import api_view
from .models import Department
from .serializers import DepartmentSerializer,getcourseSerialiser

@api_view(['POST'])
def create_department(request):
    serializer = DepartmentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Department created successfully."}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .serializers import CourseSerializer

@api_view(['POST'])
def create_course(request):
    serializer = CourseSerializer(data=request.data)

    if serializer.is_valid():
        title = serializer.validated_data.get('title')
        existing_course = Course.objects.filter(title=title).first()

        if existing_course:
            return Response({"message": "Course with the same title already exists."}, status=status.HTTP_400_BAD_REQUEST)

        instructors_ids = serializer.validated_data.pop('instructors')
        course = serializer.save()

        # Add instructors to the course
        course.instructors.set(instructors_ids)

        return Response({"message": "Course created successfully."}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def update_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course, data=request.data, partial=True)

    if serializer.is_valid():
        instructors_ids = serializer.validated_data.get('instructors')
        if instructors_ids is not None:
            course.instructors.set(instructors_ids)

        serializer.save()
        return Response({"message": "Course updated successfully."}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def delete_course(request, course_id):


    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

    course.delete()
    return Response({"message": "Course deleted successfully."}, status=status.HTTP_204_NO_CONTENT)




from .models import Department
from .serializers import DepartmentSerializer

@api_view(['GET'])
def get_departments_with_courses(request):
    departments = Department.objects.all()
    departments_data = []
    
    for department in departments:
        department_data = DepartmentSerializer(department).data
        department_data['courses'] = getcourseSerialiser(department.course_set.all(), many=True).data
        departments_data.append(department_data)
    
    return Response(departments_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_courses(request):
    page = int(request.GET.get('page', 1))  # Get the requested page number (default: 1)
    items_per_page = 6  # Number of courses per page

    total_courses = Course.objects.count()
    total_pages = (total_courses + items_per_page - 1) // items_per_page

    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    courses = Course.objects.all()[start_index:end_index]
    serializer = getcourseSerialiser(courses, many=True)

    response_data = {
        'results': serializer.data,
        'page': page,
        'total_pages': total_pages
    }

    return Response(response_data, status=status.HTTP_200_OK)

