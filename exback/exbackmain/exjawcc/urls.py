from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # path('release/<int:pk>', ReleaseRetrieveView.as_view()),
    path('release/<slug>', ReleaseRetrieveView.as_view()),
    path('release/update/<int:pk>', ReleaseUpdateView.as_view()),
    path('release/create', ReleaseCreateView.as_view()),
    path('release/all', ReleaseListView.as_view()),

    path('platform/<int:pk>', PlatformRetrieveView.as_view()),
    path('platform/update/<int:pk>', PlatformUpdateView.as_view()),
    path('platform/create', PlatformCreateView.as_view()),
    path('platform/all', PlatformListView.as_view()),

    path('link/<int:pk>', LinkRetrieveView.as_view()),
    path('link/update/<int:pk>', LinkUpdateView.as_view()),
    path('link/create', LinkCreateView.as_view()),
    path('link/all', LinkListView.as_view()),
]
