from django.urls import path
from . import views
from .views import register,login,varifyintructor,create_expertise,get_all_expertise

urlpatterns = [
    path("",views.welcome_path,name="welcome"),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('students/<int:student_id>', views.delete_student, name='delete-student'),
    path('create-instructor', views.create_instructor, name='create-instructor'),
    path('verify-intructor',varifyintructor,name="verify-intructor"),
    path('create-expertise/', create_expertise, name='create-expertise'),
    path('get-all-expertise/', get_all_expertise, name='get-all-expertise')
    # path("get_all_users/",views.get_all_users,name="get_all_users")
    # path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair')
]