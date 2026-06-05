from django.contrib import admin
from django.urls import include,path
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView
from apps.accounts.views import SHMSTokenObtainPairView
urlpatterns=[path('admin/',admin.site.urls),path('api/schema/',SpectacularAPIView.as_view(),name='schema'),path('api/docs/',SpectacularSwaggerView.as_view(url_name='schema')),path('api/v1/auth/login/',SHMSTokenObtainPairView.as_view()),path('api/v1/auth/refresh/',TokenRefreshView.as_view()),path('api/v1/auth/verify/',TokenVerifyView.as_view()),path('api/v1/accounts/',include('apps.accounts.urls')),
    path('equipment/', include('apps.equipment.urls')),
    path('projects/', include('apps.projects.urls')),
    path('subscriptions/', include('apps.subscriptions.urls')),
    path('wifi/', include('apps.wifi.urls')),
    path('feedback/', include('apps.feedback.urls')),
    path('filetransfer/', include('apps.filetransfer.urls')),
    path('fmreport/', include('apps.fmreport.urls')),
    path('calls/', include('apps.calls.urls')),
    path('radio/', include('apps.radio.urls')),
    path('news/', include('apps.news.urls')),
    path('videography/', include('apps.videography.urls')),
path('v1/dashboard/',include('apps.dashboard.urls'))]
