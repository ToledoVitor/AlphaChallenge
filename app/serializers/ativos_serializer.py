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
            'last_evaluation',
            'last_day_evaluation',
            'variation',

            'pretty_updated_at',
        )
