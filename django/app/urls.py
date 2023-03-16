from django.urls import path

from app.views import (
    AvisoPrecoCreateView,
    AvisoPrecoListView,
    CotacoesListView,
    SignupView,
    LoginInterfaceView,
    LogoutInterfaceView,
)

urlpatterns = [
    path('', CotacoesListView.as_view(), name='cotacoes.list'),
    path('avisos/', AvisoPrecoListView.as_view(), name='avisos.list'),
    path('avisos/new', AvisoPrecoCreateView.as_view(), name='avisos.new'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginInterfaceView.as_view(), name='login'),
    path(
        'logout', LogoutInterfaceView.as_view(next_page='login'), name='logout'
    ),
]
