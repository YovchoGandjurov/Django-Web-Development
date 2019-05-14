from rest_framework.permissions import BasePermission, IsAdminUser, \
        IsAuthenticated, SAFE_METHODS

from .models import Doctor


class DoctorPermission(BasePermission):

    def has_permission(self, request, view):
        doctor = Doctor.objects.all().filter(user__pk=request.user.id).exists()
        # import pdb; pdb.set_trace()

        if request.user.is_superuser:
            return True
        elif request.method == 'DELETE' or request.method == 'POST':
            return False
        elif doctor or request.method == 'GET':
            return True
        else:
            return False


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        return request.user == obj.user
