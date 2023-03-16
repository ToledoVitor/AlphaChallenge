from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import CreateAvisoPrecoForm
from .models import AvisoPreco, Cotacao


class SignupView(CreateView):
    template_name = 'core/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('cotacoes.list')

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


class CotacoesListView(LoginRequiredMixin, ListView):
    model = Cotacao
    context_object_name = 'cotacoes'
    template_name = 'app/cotacoes_list.html'
    login_url = 'login'

    def get_queryset(self):
        return (
            Cotacao
            .objects
            .order_by("code", "-updated_at")
            .distinct("code")
            .all()
        )


class AvisoPrecoListView(LoginRequiredMixin, ListView):
    model = AvisoPreco
    context_object_name = 'avisos'
    template_name = 'app/avisos_list.html'
    login_url = 'login'

    def get_queryset(self):
        return super().get_queryset()


class AvisoPrecoCreateView(CreateView):
    form_class = CreateAvisoPrecoForm
    template_name = 'app/avisos_create.html'
    success_url = '/cotacoes/avisos'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('cotacoes.list')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        cotacao = self.request.POST['cotacao_code']
        if not Cotacao.objects.filter(code=cotacao).exists():
            return super().form_invalid(form)

        return super().form_valid(form)
