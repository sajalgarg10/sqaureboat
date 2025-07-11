from django.shortcuts import render
from applications.models import Jobs , Applications 
from applications.serializers import JobSerializers , ApplicantSerializer
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from users.models import User
from rest_framework.status import HTTP_200_OK , HTTP_400_BAD_REQUEST
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_jobs(request):
    jobs = Jobs.objects.all()
    serializer = JobSerializers(jobs , many = True )
    return Response(serializer.data , HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated , IsAdminUser])
def list_jobs_applicants(request):
    applications = Applications.objects.all()
    serializer = ApplicantSerializer(applications , many = True )
    return Response(serializer.data , HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated , IsAdminUser])
def post_jobs(request):
    serializer = JobSerializers(data = request.data)
    if not serializer.is_valid():
        return Response(serializer.errors , HTTP_400_BAD_REQUEST)
    job = Jobs(**serializer.validated_data)
    job.save()
    return Response({"response":"job created successfully"} , HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_job(request, pk):
    try:
        job = Jobs.objects.get(id = pk)
    except Jobs.DoesNotExist:
        return Response("job not found" , HTTP_400_BAD_REQUEST)
    application = Applications(job = job , user = request.user)
    application.save()
    return Response({"response":"Application is created"} , HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_application(request , pk):
    applications = Applications.objects.filter(job_id = pk)
    serializer = ApplicantSerializer(applications , many = True)
    return Response(serializer.data , HTTP_200_OK)




        
    
        





