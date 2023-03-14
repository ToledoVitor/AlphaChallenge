from django.http import JsonResponse

from app.models import Ativo
from app.serializers.ativos_serializer import AtivoSerializer


def get_ativos(request):
    ativos = Ativo.objects.order_by('-updated_at')[:100]
    serializer = AtivoSerializer(ativos, many=True)
    return JsonResponse(serializer.data, safe=False)
