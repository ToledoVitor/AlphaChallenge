from django.http import JsonResponse
from django.views.decorators.http import require_GET

from app.models import Ativo
from app.forms_validator import (
    GetAtivosForm, GetAtivoByCodeForm, GetAtivoByTableForm
)
from app.serializers.ativos_serializer import AtivoSerializer


@require_GET
def get_ativos(request):
    form = GetAtivosForm.parse_obj(request.GET.dict())

    ativos = Ativo.objects.all()
    if form.order_by:
        ativos = ativos.order_by(form.order_by)
    if form.name:
        ativos = ativos.filter(name__icontains=form.name)
    if form.code:
        ativos = ativos.filter(code__icontains=form.code)
    if form.table:
        ativos = ativos.filter(table=form.table)
    if form.limit:
        ativos = ativos[:form.limit]

    serializer = AtivoSerializer(ativos, many=True)
    return JsonResponse(serializer.data, safe=False)


@require_GET
def get_ativo_history_by_code(request, code):
    form = GetAtivoByCodeForm.parse_obj(request.GET.dict())

    ativos = Ativo.objects.filter(code__icontains=code)
    if form.order_by:
        ativos = ativos.order_by(form.order_by)
    if form.limit:
        ativos = ativos[:form.limit]

    serializer = AtivoSerializer(ativos, many=True)
    return JsonResponse(serializer.data, safe=False)


@require_GET
def get_ativo_history_by_table(request, table):
    form = GetAtivoByTableForm.parse_obj(request.GET.dict())

    ativos = Ativo.objects.filter(table__icontains=table)
    if form.order_by:
        ativos = ativos.order_by(form.order_by)
    if form.limit:
        ativos = ativos[:form.limit]

    serializer = AtivoSerializer(ativos, many=True)
    return JsonResponse(serializer.data, safe=False)
