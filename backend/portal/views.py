# clase 01/09/25
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .form import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_protect

from .models import (
    Region,
    Comuna,
    Inmueble
)
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .form import (
    RegionForm,
    ComunaForm,
    InmuebleForm
)



# Create your views here.

#########################################################################
# CRUD PARA REGION
#########################################################################
class RegionListView(ListView):
    model = Region
    template_name = "inmueble/region_list.html"
    context_object_name = "regiones"

class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm
    template_name = "inmueble/region_form.html"
    success_url = reverse_lazy("region_list")

class RegionUpdateView(UpdateView):
    model = Region
    form_class = RegionForm
    template_name = "inmueble/region_form.html"
    success_url = reverse_lazy("region_list")

class RegionDeleteView(DeleteView):
    model = Region
    template_name = "inmueble/region_confirm_delete.html"
    success_url = reverse_lazy("region_list")

#########################################################################
# CRUD PARA COMUNA
#########################################################################
class ComunaListView(ListView):
    model = Comuna
    template_name = "inmueble/comuna_list.html"
    context_object_name = "comunas"
    
class ComunaCreateView(CreateView):
    model = Comuna
    form_class = ComunaForm
    template_name = "inmueble/comuna_form.html"
    success_url = reverse_lazy("comuna_list")

class ComunaUpdateView(UpdateView):
    model = Comuna
    form_class = ComunaForm
    template_name = "inmueble/comuna_form.html"
    success_url = reverse_lazy("comuna_list")

class ComunaDeleteView(DeleteView):
    model = Comuna
    template_name = "inmueble/comuna_confirm_delete.html"
    success_url = reverse_lazy("comuna_list")

#########################################################################
# CRUD PARA INMUEBLE
#########################################################################
class InmuebleListView(ListView):
    model = Inmueble
    template_name = "inmueble/inmueble_list.html"
    context_object_name = "inmuebles"
    
class InmuebleCreateView(CreateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = "inmueble/inmueble_form.html"
    success_url = reverse_lazy("inmueble_list")

class InmuebleUpdateView(UpdateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = "inmueble/inmueble_form.html"
    success_url = reverse_lazy("inmueble_list")

class InmuebleDeleteView(DeleteView):
    model = Inmueble
    template_name = "inmueble/inmueble_confirm_delete.html"
    success_url = reverse_lazy("inmueble_list")




# clase 01/09/25
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cuenta creada correctamente.")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "Has iniciado sesión.")
        return redirect("home")
    return render(request, "registration/login.html", {"form": form})
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect("login")