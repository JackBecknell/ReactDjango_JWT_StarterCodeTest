from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from projects.models import Project
from .serializers import ProjectSerializer
from authentication.models import User


class ProjectList(APIView, AllowAny):

    def get(self, request, project_id):
        print(f'this is project_id: {project_id}')
        projects = Project.objects.filter(id = project_id)
        print(f'line 16: {projects}')
        serializer = ProjectSerializer(projects, many=True)
        print(f'line 18:  {serializer}')
        # print(f'line 21:  {serializer.data}')
        return Response(serializer.data, status=status.HTTP_200_OK)
