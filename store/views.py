from .models import Box
from .utils.filters import BoxFilter
from django.core.exceptions import ObjectDoesNotExist
from .serializers import BoxSerializer,StaffBoxSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .utils.isValid import IsValid
from rest_framework.decorators import api_view , permission_classes , authentication_classes


#Add New Box

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def add_box(request):
    box = Box(created_by=request.user)
    serializer = StaffBoxSerializer(box, data=request.data,partial=True)
    if serializer.is_valid() and IsValid(request.user):
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# display all box

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
def list_all_box(request):
    box_queryset = Box.objects.all()
    boxes = BoxFilter(request.GET,queryset=box_queryset).qs
    if (request.user.is_staff):
        serializer = StaffBoxSerializer(boxes, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    serializer = BoxSerializer(boxes, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

#Display boxes according to logged in user 

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def my_list_box(request):
    box_queryset = Box.objects.filter(created_by=request.user)
    boxes = BoxFilter(request.GET,queryset=box_queryset).qs
    serializer = StaffBoxSerializer(boxes, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


#Update box with given id of box

@api_view(['PUT'])
@permission_classes([IsAdminUser])
@authentication_classes([BasicAuthentication])
def update_box(request,pk):
    try:
        box = Box.objects.get(pk=pk)
    except Box.DoesNotExist:
        data = {'error':'Box does not exist'}
        return Response(data,status=status.HTTP_404_NOT_FOUND)

    serializer = StaffBoxSerializer(box, data=request.data,partial=True)
    if serializer.is_valid() and IsValid(request.user):
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Delete box with given id of box

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
@authentication_classes([BasicAuthentication])
def delete_box(request,pk):
    try:
        box = Box.objects.get(pk=pk)
        if request.user == box.created_by :
            box.delete()
            data = {'sucess':'Sucessfully Deleted'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            data = {'error':'you are not authorised.'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_200_OK)

    except Box.DoesNotExist:
        data = {'error':'Box does not exist'}
        return Response(data,status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




