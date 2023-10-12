from user.models import CustomUser
from . serializers import UserSerializer
from . permissions import CustomIsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView

# If you are creating an object, just POST to /api/ URL. 
# You cannot access to api/create URL.
# Accessing requires GET
class CustomUserCreate(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer 

class CustomUserRetrieve(RetrieveAPIView, CustomIsAuthenticated):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomIsAuthenticated]

class CustomUserDestroy(RetrieveDestroyAPIView, CustomIsAuthenticated):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomIsAuthenticated]

class CustomUserUpdate(RetrieveUpdateAPIView, CustomIsAuthenticated):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomIsAuthenticated]

    # update() in View deals more with HTTP Response part