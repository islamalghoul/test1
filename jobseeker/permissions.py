from rest_framework.permissions import BasePermission

class Jobseeker(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and not request.user.is_company)