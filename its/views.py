from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, generics, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import  permission_classes
from rest_framework import filters
from rest_framework.decorators import api_view
import re
# permissions
from core.permissions import default_authenticated_user

# serializers
from .serializers import *

from datetime import datetime, timedelta
#------
# auth_token |
#------
class auth_token_list_view(viewsets.ModelViewSet):
    permission_classes = [default_authenticated_user]
    queryset = AuthToken.objects.all()
    serializer_class = AuthTokenSerializer
    
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    # filterset_fields = [ 'type','registration']
    # search_fields = ["name", "registration",'created_at']

    def list(self, request,*args, **kwargs):
        if not request.user.has_perm('cheque.view_authtoken'):
            response = Response(
                    {'detail':('User do not has permission')},
                    status=status.HTTP_403_FORBIDDEN)
            return response
        
        instance = super().list(request, *args, **kwargs)

        return instance

    def create(self, request,*args, **kwargs):
        # if not request.user.has_perm('cheque.add_authtoken'):
        #     response = Response(
        #             {'detail':('User do not has permission')},
        #             status=status.HTTP_403_FORBIDDEN)
        #     return response
        
        # request.data['created_by']=request.user.id
        # today = datetime.now()
        # tmp = today + timedelta(hours=6)
        # dt_str = tmp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        # request.data['valid_till'] = dt_str
        try:
            instance = super().create(request, *args, **kwargs)
            return instance
        except Exception as e:
            print(e)

    def retrieve(self, request, pk=None,*args, **kwargs):
        if not request.user.has_perm('cheque.view_authtoken'):
            response = Response(
                    {'detail':('User do not has permission')},
                    status=status.HTTP_403_FORBIDDEN)
            return response
        instance = super().retrieve(request, *args, **kwargs)
        return instance

    def update(self, request, pk=None,*args, **kwargs):
        if not request.user.has_perm('cheque.change_authtoken'):
            response = Response(
                    {'detail':('User do not has permission')},
                    status=status.HTTP_403_FORBIDDEN)
            return response
        request.data['updated_by']=request.user.id
        updated_instance = super().update(request, *args, **kwargs)
        return updated_instance

    def partial_update(self, request, pk=None,*args, **kwargs):
        if not request.user.has_perm('cheque.change_authtoken'):
            response = Response(
                    {'detail':('User do not has permission')},
                    status=status.HTTP_403_FORBIDDEN)
            return response
        request.data['updated_by']=request.user.id
        updated_instance = super().partial_update(request, *args, **kwargs)
        return updated_instance

    def destroy(self, request, *args, **kwargs):
        if not request.user.has_perm('cheque.delete_authtoken'):
            response = Response(
                    {'detail':('User do not has permission')},
                    status=status.HTTP_403_FORBIDDEN)
            return response
        return super().destroy(request, *args, **kwargs)
    


""" 
def destroy(self, request, pk=None,*args, **kwargs):
        if not request.user.has_perm('cheque.delete_authtoken'):
            response = Response(
                    {'detail':('User do not has permission')},
                    status=status.HTTP_403_FORBIDDEN)
            return response
        try:
            obj = AuthToken.objects.get(id=pk)
            obj.deleted=True
            obj.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response("Wrong Credentials", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 """
