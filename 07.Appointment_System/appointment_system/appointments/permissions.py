from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Patient


class PatientChecker(BasePermission):

    def has_permission(self, request, view):
        patient = Patient.objects.filter(user__pk=request.user.id).exists()

        if request.method in SAFE_METHODS or patient or \
                request.user.is_superuser:
            return True
        return False


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        return request.user == obj.patient.user and obj.status == 'P'
