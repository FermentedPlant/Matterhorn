from rest_framework.permissions import SAFE_METHODS, BasePermission

# Check account POST, GET, RETRIEVE, DESTROY request for authentication
class CustomIsAuthenticated(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed if the requesting 'obj' is requested by the 'request.user' or the superuser
        return obj == request.user or request.user.is_superuser
