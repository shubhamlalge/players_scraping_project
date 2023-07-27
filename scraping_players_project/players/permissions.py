from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    """
    Custom permission class that allows CRUD operations for superusers,
    read-only access for authenticated users, and denies access for non-authenticated users.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            # Deny access for non-authenticated users
            return False

        if request.user.is_superuser:
            # Allow CRUD operations for superusers
            return True

        if request.method in ['GET']:
            # Allow read-only access for authenticated users
            return True

        # Deny access for any other request methods
        return False

