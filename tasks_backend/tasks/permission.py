from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Allow access if user is owner OR admin
    """

    def has_object_permission(self, request, view, obj):
        return (
            obj.created_by == request.user
            or request.user.is_staff
            or request.user.is_superuser
        )
