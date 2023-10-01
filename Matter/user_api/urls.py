from django.urls import path, include
from .views import CustomUserCreate, CustomUserRetrieve, CustomUserDestroy, CustomUserUpdate

app_name = 'user_api'

urlpatterns = [
    path('create', CustomUserCreate.as_view(), name='usercreate'),
    path('retrieve/<int:pk>', CustomUserRetrieve.as_view(), name='userretrieve'),
    path('delete/<int:pk>', CustomUserDestroy.as_view(), name='userdestroy'),
    path('update/<int:pk>', CustomUserUpdate.as_view(), name='userupdate'),
]