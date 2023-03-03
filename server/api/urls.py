from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions, routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

import server.api.generic.views as views


schema_view = get_schema_view(
    openapi.Info(
        title='v1 API',
        default_version='v1',
        description='v1 API',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'item', views.ItemViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'notification', views.NotificationViewSet)
router.register(r'trade', views.TradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', views.register_view, name='register'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
