import jwt
from django.http import JsonResponse
from ..models import StudentModel

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of paths that require token validation
        secured_paths = ['/each_course/<int:course_id>/']

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
                decoded_token = jwt.decode(token, 'rajtupe987', algorithms=['HS256'])
                user_id = decoded_token.get('userId')
                user = StudentModel.objects.filter(id=user_id).first()

                if not user:
                    return JsonResponse({"message": "User not found", "ok": False}, status=401)

                request.user = user

            except jwt.ExpiredSignatureError:
                return JsonResponse({"message": "Token has expired"}, status=401)
            except jwt.DecodeError:
                return JsonResponse({"message": "Token is invalid"}, status=401)

        response = self.get_response(request)
        return response