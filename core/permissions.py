from rest_framework.permissions import BasePermission

from rest_framework.permissions import IsAuthenticated

class default_authenticated_user(BasePermission):

    def has_permission(self, request, view):
        print('Auth Check')
        return True