from rest_framework import serializers
from .models import Instructor,Expertise,StudentModel, Department,Assignment, Enrollment

class InstructorSerializer(serializers.ModelSerializer):
    expertise = serializers.PrimaryKeyRelatedField(queryset=Expertise.objects.all(), many=True)

    class Meta:
        model = Instructor
        fields = ['id', 'first_name', 'last_name', 'expertise', 'email', 'password', 'created_at']


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = ['id', 'name']







from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['id', 'title','description','instructors','department','created_at']



class getcourseSerialiser(serializers.ModelSerializer):
    instructors = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructors', 'department', 'created_at']

    def get_instructors(self, obj):
        instructors = obj.instructors.all()
        instructor_data = []
        for instructor in instructors:
            instructor_data.append({
                'id': instructor.id,
                'name': f"{instructor.first_name} {instructor.last_name}",
                'email': instructor.email,
                'expertise': [expertise.name for expertise in instructor.expertise.all()]
            })
        return instructor_data

    def get_department(self, obj):
        department = obj.department
        return {
            'id': department.id,
            'name': department.name
        }
    
class DepartmentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)  # Use your getcourseSerialiser here

    class Meta:
        model = Department
        fields = ['id', 'name', 'created_at', 'courses']



class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'





class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'



class StudentEnrollmentSerializer(serializers.ModelSerializer):
    enrollment_set = EnrollmentSerializer(many=True, read_only=True)
    department = serializers.SerializerMethodField()

    class Meta:
        model = StudentModel
        fields = ('name', 'enrollment_set', 'department')

    def get_department(self, obj):
        # Assuming you have a department associated with the student's enrollment.
        # You may need to adjust this logic based on your actual data structure.
        if obj.enrollment_set.exists():
            return obj.enrollment_set.first().course.department.name
        return None