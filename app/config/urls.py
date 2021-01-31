from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('contactus/', include('contactus.urls')),
    # path('courses/', include('courses.urls')),
    # path('users/', include('users.urls')),
]
