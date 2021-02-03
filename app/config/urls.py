from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('courses.urls')),
    path('admin/', admin.site.urls),
    # path('contactus/', include('contactus.urls')),
    # path('users/', include('users.urls')),
]
