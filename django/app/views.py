from django.views.generic import (
    DetailView,
    ListView,
)
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import CreateAvisoPrecoForm
from .models import Cotacao


class SignupView(CreateView):
    template_name = 'core/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('cotacoes.list')

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(SignupView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('cotacoes.list')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'core/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('cotacoes.list')


class CotacoesDeleteView(DeleteView):
    model = Cotacao
    success_url = '/cotacoes/'
    template_name = 'app/cotacoes-delete.html'


class CotacoesListView(LoginRequiredMixin, ListView):
    model = Cotacao
    context_object_name = "cotacoes"
    template_name = "app/cotacoes_list.html"
    login_url = "login"

    def get_queryset(self):
        return Cotacao.objects.all()


class CotacoesDetailView(DetailView, SingleObjectMixin):
    model = Cotacao
    context_object_name = "cotacao"
    template_name = "app/cotacoes_detail.html"

    def get_queryset(self):
        return super().get_queryset()


class CreateAvisoPrecoView(CreateView):
    form_class = CreateAvisoPrecoForm
    template_name = 'app/create_aviso_preco.html'
    success_url = '/cotacoes/'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('cotacoes.list')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        cotacao = self.request.POST['cotacao_code']
        if not Cotacao.objects.filter(code=cotacao).exists():
            return super().form_invalid(form)

        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        # cotacao_code = request.POST['cotacao_code']
        return super().post(request, *args, **kwargs)
