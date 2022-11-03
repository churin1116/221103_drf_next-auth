from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('testapp.urls')),
    path("api/auth/", include("dj_rest_auth.urls")),  # 追加
    path("api/social/login/", include("accounts.urls")),  # 追加
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
