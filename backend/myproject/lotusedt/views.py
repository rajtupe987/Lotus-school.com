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
from decouple import config

# Create your views here.

from django.conf import settings

from .serializers import  EnrollmentSerializer,AssignmentSerializer
# this is for checking user is admin or not

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
        
from datetime import datetime, timedelta  # Import datetime and timedelta

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

            
            if not check_password(password, user.pass_hash):  # Compare the passwords
                return JsonResponse({"ok": False, "msg": "Invalid email or password"})

            # Calculate the expiration time (1 minute from the current time)
            expiration_time = datetime.utcnow() + timedelta(minutes=10)

            # Calculate the expiration time for the refresh token (e.g., 7 days from the current time)
            refresh_token_expiration = datetime.utcnow() + timedelta(days=7)

            payload = { "userId": user.id,
                       "userName": user.name,
                       "exp": expiration_time
                 }
            
            # Create the payload for the refresh token
            refresh_token_payload = {
                "userId": user.id,
                "exp": refresh_token_expiration  # Set the refresh token expiration time
            }
           
           
           
             # Replace with your actual secret key
            token = jwt.encode(payload, config('SECRET_KEY'), algorithm='HS256').decode('utf-8')  # Decode the bytes to string
            refresh_token = jwt.encode(refresh_token_payload,config('SECRET_KEY'), algorithm='HS256').decode('utf-8')

            response = {
                "ok": True,
                "token": token,
                "refresh_token": refresh_token,
                "msg": "Login Successful",

            }

            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok": False, "msg": str(e)})



@api_view(['POST'])
def enroll_student(request):
    serializer = EnrollmentSerializer(data=request.data)
    if serializer.is_valid():
        student = serializer.validated_data['student']
        course = serializer.validated_data['course']

        # Check if the student is already enrolled in the same course
        existing_enrollment = Enrollment.objects.filter(student=student, course=course).first()
        if existing_enrollment:
            return Response({"message": "You are already enrolled in this course."}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({"message": "Enrollment successful."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_course_details(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"message": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = getcourseSerialiser(course)
    return Response(serializer.data, status=status.HTTP_200_OK)

            

@api_view(['GET'])
def enrolled_students_with_courses_and_departments(request):
    if request.method == 'GET':
        enrolled_students = StudentModel.objects.filter(enrollment__isnull=False).distinct()
        total_enrolled_students = enrolled_students.count()  # Calculate the total count
        serializer = StudentEnrollmentSerializer(enrolled_students, many=True)
        response_data = {
            'total_enrolled_students': total_enrolled_students,
            'enrolled_students': serializer.data
        }
        return Response(response_data)

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import StudentModel, Enrollment

def student_enrollments(request, student_id):
    # Retrieve the student based on the student_id
    student = get_object_or_404(StudentModel, id=student_id)

    # Retrieve all enrollments for the student
    enrollments = Enrollment.objects.filter(student=student)

    # Create a list of enrollment details
    enrollment_list = []
    for enrollment in enrollments:
        enrollment_info = {
            'course_title': enrollment.course.title,
            'enrollment_date': enrollment.enrollment_date.strftime('%Y-%m-%d'),
            'instructors': [f"{instructor.first_name} {instructor.last_name}" for instructor in enrollment.course.instructors.all()],
            'department': enrollment.course.department.name,
        }
        enrollment_list.append(enrollment_info)

    # Return the enrollment details as JSON response
    return JsonResponse({'enrollments': enrollment_list})



from .models import Instructor,Enrollment
from .serializers import InstructorSerializer,ExpertiseSerializer,StudentEnrollmentSerializer
   

def instructor_profile(request, instructor_id):
    try:
        instructor = Instructor.objects.get(id=instructor_id)
        courses = instructor.course_set.all()

        if courses:
            # Assuming the instructor is associated with at least one course
            department = courses[0].department.name
        else:
            department = "Not assigned to any department"  # Handle the case when there are no courses

        # Create a dictionary with the required instructor details
        instructor_data = {
            'first_name': instructor.first_name,
            'last_name': instructor.last_name,
            'email': instructor.email,
            'department': department,
            'courses': [course.title for course in courses]
        }

        return JsonResponse(instructor_data)
    except Instructor.DoesNotExist:
        return JsonResponse({'error': 'Instructor not found'}, status=404)


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

            # Calculate the expiration time (1 minute from the current time)
            expiration_time = datetime.utcnow() + timedelta(minutes=10)

            payload = {"instructorId": user.id,"instructorName": user.first_name,
                       "exp": expiration_time}
            
            # Replace with your actual secret key
            token = jwt.encode(payload, config('SECRET_KEY_Intructor'), algorithm='HS256').decode('utf-8')  # Decode the bytes to string

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



@api_view(['POST'])
def create_assignment(request):
    serializer = AssignmentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Assignment created successfully."}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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

@api_view(['GET'])
def get_all_instructors(request):
    instructors = Instructor.objects.all()
    serializer = InstructorSerializer(instructors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


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







from rest_framework import views, status
from rest_framework.response import Response
import requests

import requests
import json

class ChatbotView(views.APIView):
    def post(self, request):
        user_message = request.data.get('message')

        gpt_api_key = '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'  # Replace with your GPT-3 API key
        gpt3_url = 'https://api.openai.com/v1/engines/davinci/completions'

        headers = {
            'Authorization': f'Bearer {gpt_api_key}',
        }

        # Provide a clear instruction to GPT-3
        instruction = "The Lotus School website is an educational management platform built using Django, a popular Python web framework. This platform is designed to manage various aspects of a school, including students, instructors, departments, courses, enrollments, assignments, submissions, and announcements. It provides a comprehensive solution for administrators, teachers, and students to interact with the school's data and services."

        # Combine the instruction and user's message
        prompt = f"{instruction} On the basis of this only answer this: {user_message} otherwise just say i can not answer any irrelevent quations"

        data = {
            'prompt': prompt,
            'max_tokens': 50,
        }

        try:
            # Log the request data
            print(f"Request to GPT-3: {json.dumps(data)}")

            response = requests.post(gpt3_url, headers=headers, json=data)

            # Log the GPT-3 response
            print(f"Response from GPT-3: {response.text}")

            if response.status_code == 200:
                chatbot_response = response.json().get('choices')[0].get('text')
                return Response({'response': chatbot_response}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Chatbot request failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(f"Error: {str(e)}")
            return Response({'error': 'Chatbot request failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
