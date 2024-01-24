from rest_framework.permissions import BasePermission

class IsSuperuser(BasePermission):
    """
    A base class from which all permission classes should inherit.
    """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return bool(request.user and request.user.is_superuser)