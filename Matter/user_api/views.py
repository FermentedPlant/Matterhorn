from user.models import CustomUser
from . serializers import UserSerializer
from . permissions import IsOwnerOrReadOnly
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView

# If you are creating an object, just POST to /api/ URL. 
# You cannot access to api/create URL.
# Accessing requires GET
class CustomUserCreate(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer 

class CustomUserRetrieve(RetrieveAPIView, IsOwnerOrReadOnly):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

class CustomUserDestroy(RetrieveDestroyAPIView, IsOwnerOrReadOnly):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

class CustomUserUpdate(RetrieveUpdateAPIView, IsOwnerOrReadOnly):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # update() in View deals more with HTTP Response part