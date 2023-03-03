from rest_framework import serializers

from server.models import (
    Item,
    Message,
    Notification,
    Trade,
)


class AutoUserSetSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True, source='user.login')

    def create(self, validated_data):
        request = self.context['request']
        validated_data['user'] = request.user

        return super().create(validated_data)


class ItemSerializer(AutoUserSetSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class MessageSerializer(AutoUserSetSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class NotificationSerializer(AutoUserSetSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class TradeSerializer(AutoUserSetSerializer):
    class Meta:
        model = Trade
        fields = '__all__'
