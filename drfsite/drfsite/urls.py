from django.contrib import admin
from django.urls import path, include, re_path
from warehouse.views import *
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'userlist', UserViewSet)
# print(router.urls)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/userlist/', UserAPIList.as_view()),
    path('api/v1/userlist/<int:pk>/', UserAPIUpdate.as_view()),
    path('api/v1/userdelete/<int:pk>/', UserAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
