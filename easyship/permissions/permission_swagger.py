from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET','POST')

class SwaggerPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_admin
        )