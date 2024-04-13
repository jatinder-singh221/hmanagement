from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('security.urls')),
<<<<<<< HEAD
    path("account/", include("django.contrib.auth.urls")),
=======
>>>>>>> 56daa069d5064fc7c5df6c6b0b2c522aadc897c4
    path('', include('management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )


