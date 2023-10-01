from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # SAFE_METHODS is shortcut of saying if the request is either ('GET', 'HEAD', 'OPTIONS')
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed if the requesting 'obj' is requested by the 'request.user' or the superuser
        return obj == request.user or request.user.is_superuser
