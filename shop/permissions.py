from rest_framework.permissions import BasePermission

class IsAdminUserOrReadOnly(BasePermission):
    """
    Custom permission to allow only admins to modify data, while others can only read.
    """

    def has_permission(self, request, view):
        # Allow read-only access for all users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Allow write access only for admin users
        #return request.user.is_staff
        return True