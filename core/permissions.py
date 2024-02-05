from rest_framework.permissions import BasePermission
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from its.models import *
class default_authenticated_user(BasePermission):

    def has_permission(self, request, view):
        print(request.headers['Authorization'].split(' ')[1])
        header_token = request.headers['Authorization'].split(' ')[1]
        db_token = None
        try:   
            db_token = AuthToken.objects.get(token=header_token)
        except Exception as e:
            return False
        if db_token:
            #if db_token.valid_till < datetime.now():
            return True
        return False

# if request.user.is_authenticated:
#             return True