from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from complaints.views import ComplaintViewSet

router = DefaultRouter()
router.register(r'complaints', ComplaintViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
