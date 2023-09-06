import jwt
from django.http import JsonResponse
from ..models import StudentModel,Instructor

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of paths that require token validation
        secured_paths = ['/each_course']

        # Check if the current path requires token validation
        requires_auth = any(request.path.startswith(path) for path in secured_paths)

        if requires_auth:
            # Extract token from Authorization header
            auth_header = request.META.get('HTTP_AUTHORIZATION', '')
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
            else:
                return JsonResponse({"message": "Authorization header format is invalid"}, status=401)

            try:
                # Verify and decode the token
                print("hi")
                decoded_token = jwt.decode(token, 'rajtupe987', algorithms=['HS256'])
                user_id = decoded_token.get('userId')
                user_name = decoded_token.get('userName')  # Extract the user's name

                user = StudentModel.objects.filter(id=user_id).first()
        
                if not user:
                    return JsonResponse({"message": "User not found", "ok": False}, status=401)

                 # Attach the user and user's name to the request object for later use
                request.user = user
                request.user_name = user_name
                print(user_id)
                print(user_name)

            except jwt.ExpiredSignatureError:
                return JsonResponse({"message": "Token has expired"}, status=401)
            except jwt.DecodeError:
                return JsonResponse({"message": "Token is invalid"}, status=401)

        response = self.get_response(request)
        return response
    


class JWTInstructorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of paths that require instructor token validation
        secured_paths = ['/instructors_profile']

        # Check if the current path requires instructor token validation
        requires_auth = any(request.path.startswith(path) for path in secured_paths)

        if requires_auth:
            # Extract token from Authorization header
            auth_header = request.META.get('HTTP_AUTHORIZATION', '')
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
            else:
                return JsonResponse({"message": "Authorization header format is invalid"}, status=401)

            try:
                # Verify and decode the token
                decoded_token = jwt.decode(token, 'lotusschoole', algorithms=['HS256'])
                instructor_id = decoded_token.get('instructorId')
                instructor_name = decoded_token.get('instructorName')  # Extract the instructor's name

                instructor = Instructor.objects.filter(id=instructor_id).first()
        
                if not instructor:
                    return JsonResponse({"message": "Instructor not found", "ok": False}, status=401)

                # Attach the instructor and instructor's name to the request object for later use
                request.instructor = instructor
                request.instructor_name = instructor_name

            except jwt.ExpiredSignatureError:
                return JsonResponse({"message": "Token has expired"}, status=401)
            except jwt.DecodeError:
                return JsonResponse({"message": "Token is invalid"}, status=401)

        response = self.get_response(request)
        return response   