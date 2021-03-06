from rest_framework import permissions


class IsAdmOrIsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if obj.email == request.user.email or request.user.is_superuser:
                return True
        return False


class SpecialistsOnlyPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role == 2:
                return True
        return False


class SpecialistOrAdminPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role == 2 or request.user.role == 1:
                return True
        return False

