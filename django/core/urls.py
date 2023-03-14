from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ativos/', views.get_ativos),
    path('ativos/code/<str:code>', views.get_ativo_history_by_code),
    path('ativos/table/<str:table>', views.get_ativo_history_by_table),
]
