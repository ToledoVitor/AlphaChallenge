from rest_framework import serializers

from app.models import Ativo


class AtivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ativo
        fields = (
            'id',
            'name',
            'code',
            'table',
            'last_price',
            'last_day_price',
            'variation',
            'pretty_updated_at',
        )
