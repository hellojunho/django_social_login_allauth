from django.contrib import admin
from django.urls import path, include
from .views import google_profile, kakao_profile, instagram_profile


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/google/profile/', google_profile, name="google_profile"),
    path('accounts/kakao/profile/', kakao_profile, name="kakao_profile"),
    path('accounts/instagram/profile/', instagram_profile, name='instagram_profile'),
]
