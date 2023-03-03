from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    ItemSerializer,
    MessageSerializer,
    NotificationSerializer,
    TradeSerializer,
)
from server.models import (
    Item,
    Message,
    Notification,
    Trade,
)


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class ItemViewSet(BaseViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filterset_fields = ['name', 'description', 'user', 'state', 'category']


class MessageViewSet(BaseViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class NotificationViewSet(BaseViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class TradeViewSet(BaseViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer


register_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['username', 'password', 'email'],
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(type=openapi.TYPE_STRING),
    }
)

register_responses = {
    200: openapi.Response(description='Success'),
    400: openapi.Response(description='Bad request'),
    401: openapi.Response(description='Unauthorized'),
}


@swagger_auto_schema(method='post', request_body=register_request_schema, responses=register_responses)
@api_view(['POST'])
def register_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if any(elem is None for elem in [username, password, email]):
        return JsonResponse({'error': 'Username, password, email required.'}, status=400)

    user_model = get_user_model()
    try:
        user_model.objects.create_user(username=username, password=password, email=email)
    except Exception as e:
        return JsonResponse({'error': f'Unable to create user. {str(e)}'}, status=400)

    return JsonResponse({'success': 'User created successfully.'}, status=201)