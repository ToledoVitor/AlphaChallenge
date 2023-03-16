from rest_framework import serializers

from app.models import Cotacao


class CotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotacao
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
