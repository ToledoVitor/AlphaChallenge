from django.urls import path

from app.views import (
    CotacoesDeleteView,
    CotacoesDetailView,
    CotacoesListView,
    CreateAvisoPrecoView,
    SignupView,
    LoginInterfaceView,
    LogoutInterfaceView,
)

urlpatterns = [
    path('', CotacoesListView.as_view(), name="cotacoes.list"),
    path('<int:pk>', CotacoesDetailView.as_view(), name="cotacoes.detail"),
    path('<int:pk>/delete', CotacoesDeleteView.as_view(), name="cotacoes.delete"),
    path('avisos/new', CreateAvisoPrecoView.as_view(), name="aviso.new"),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginInterfaceView.as_view(), name='login'),
    path('logout', LogoutInterfaceView.as_view(next_page='login'), name='logout'),
]
