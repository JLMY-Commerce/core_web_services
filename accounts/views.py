from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from accounts.forms import ClienteCreateForm


class CustomLoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("produto-list")


    def form_invalid(self, form):
        messages.error(self.request, "Nome de usuário ou senha incorretos.")
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Você saiu com sucesso.")
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    template_name = 'user_form.html'
    form_class = ClienteCreateForm
    success_url = reverse_lazy('user_list')

    def form_invalid(self, form):
        messages.error(self.request, 'Houve um erro ao criar o usuário.')
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_form.html'
    form_class = ClienteCreateForm
    success_url = reverse_lazy('user_list')

    def form_invalid(self, form):
        messages.error(self.request, 'Houve um erro ao atualizar o usuário.')
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            messages.error(request, 'Houve um erro ao excluir o usuário: ' + str(e))
            return reverse_lazy('user_list')