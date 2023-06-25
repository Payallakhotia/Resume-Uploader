from django.shortcuts import render
from rest_framework.response import Response
from app1.models import *
from api.serializer import ResumeSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status' : 200,
            'message' : 'Yes! Django rest framework is working!!!!',
            'method_called' : 'You called GET method'
        })
    elif request.method == 'POST':
        return Response({
            'status' : 200,
            'message' : 'Yes! Django rest framework is working!!!!',
            'method_called' : 'You called POST method'
        })
    else:
        return Response({
            'status' : 400,
            'message' : 'Yes! Django rest framework is working!!!!',
            'method_called' : 'You called invalid method'
        })

class ResumeView(APIView):
    def post(self,request,format=None):
        serializer=ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'Resume uploaded successfully',
                'status':'success',
                'candidate':serializer.data
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self,request,format=None):
        candidates=Resume.objects.all()
        serializer=ResumeSerializer(candidates,many=True)
        return Response({
            'status':'success',
            'candidates':serializer.data
        },status=status.HTTP_200_OK)
