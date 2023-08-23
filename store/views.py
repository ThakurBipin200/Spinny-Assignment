from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions, authentication
from rest_framework.filters import BaseFilterBackend
from django_filters import rest_framework as django_filters
from .models import Box
from .serializers import BoxSerializer, StaffBoxSerializer
from .utils.isValid import IsValid
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .utils.filters import BoxFilter  

class AddBoxView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        box = Box(created_by=request.user)
        serializer = StaffBoxSerializer(box, data=request.data, partial=True)
        if serializer.is_valid() and IsValid(request.user):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListAllBoxView(APIView):
    authentication_classes = [authentication.BasicAuthentication]

    def get(self, request):
        box_queryset = Box.objects.all()
        boxes = BoxFilter(request.GET, queryset=box_queryset).qs
        if request.user.is_staff:
            serializer = StaffBoxSerializer(boxes, many=True)
        else:
            serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MyListBoxView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        box_queryset = Box.objects.filter(created_by=request.user)
        boxes = BoxFilter(request.GET, queryset=box_queryset).qs
        serializer = StaffBoxSerializer(boxes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateBoxView(APIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.BasicAuthentication]

    def put(self, request, pk):
        try:
            box = Box.objects.get(pk=pk)
        except Box.DoesNotExist:
            data = {'error': 'Box does not exist'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        serializer = StaffBoxSerializer(box, data=request.data, partial=True)
        if serializer.is_valid() and IsValid(request.user):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteBoxView(APIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.BasicAuthentication]

    def delete(self, request, pk):
        try:
            box = Box.objects.get(pk=pk)
            if request.user == box.created_by:
                box.delete()
                data = {'success': 'Successfully Deleted'}
                return Response(data, status=status.HTTP_204_NO_CONTENT)
            else:
                data = {'error': 'You are not authorized.'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
        except Box.DoesNotExist:
            data = {'error': 'Box does not exist'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
