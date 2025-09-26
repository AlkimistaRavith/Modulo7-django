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
    Inmueble,
    SolicitudArriendo,
    PerfilUser,
    ContactData
)
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .form import (
    RegionForm,
    ComunaForm,
    InmuebleForm,
    SolicitudArriendoForm,
    PerfilUserForm,
    ContactDataForm
)



# Create your views here.

#######################################################################################
#TEMPLATE: INMUEBLE
#######################################################################################

###CRUD PARA REGION
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

###CRUD PARA COMUNA
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

###CRUD PARA INMUEBLE
class InmuebleListView(ListView):
    model = Inmueble
    template_name = "inmueble/inmueble_list.html"
    context_object_name = "inmuebles"
    
    def get_queryset(self):
        queryset = super().get_queryset()

        region_id = self.request.GET.get("region")
        comuna_id = self.request.GET.get("comuna")
        tipo = self.request.GET.get("tipo")
        precio_min = self.request.GET.get("precio_min")
        precio_max = self.request.GET.get("precio_max")

        if region_id:
            queryset = queryset.filter(comuna__region_id=region_id)
        if comuna_id:
            queryset = queryset.filter(comuna_id=comuna_id)
        if tipo:
            queryset = queryset.filter(tipo_inmueble=tipo)
        if precio_min:
            queryset = queryset.filter(arriendo_mensual__gte=precio_min)
        if precio_max:
            queryset = queryset.filter(arriendo_mensual__lte=precio_max)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        region_id = self.request.GET.get("region")

        context["regiones"] = Region.objects.all()
        context["tipos_inmueble"] = Inmueble.Tipo_Inmueble.choices

        if region_id:
            context["comunas"] = Comuna.objects.filter(region_id=region_id)
        else:
            context["comunas"] = Comuna.objects.none()

        return context

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

class InmuebleDetailView(DetailView):
    model = Inmueble
    template_name = "inmueble/inmueble_detail.html"
    context_object_name = "inmueble"

###CRUD PARA SOLICITUDES DE ARRIENDO
class SolicitudArriendoListView(ListView):
    model = SolicitudArriendo
    template_name = "inmueble/solicitud_list.html"
    context_object_name = "solicitudes"
    
class SolicitudArriendoCreateView(CreateView):
    model = SolicitudArriendo
    form_class = SolicitudArriendoForm
    template_name = "inmueble/solicitud_form.html"
    success_url = reverse_lazy("solicitud_list")
    
    def get_initial(self):
        """Prellenar el campo inmueble si viene en querystring"""
        initial = super().get_initial()
        inmueble_id = self.request.GET.get("inmueble_id")
        if inmueble_id:
            initial["inmueble"] = inmueble_id
            return initial

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.arrendatario = self.request.user
            return super().form_valid(form)
        else:
            # si no está logeado, no debería poder llegar acá
            form.add_error(None, "Debes iniciar sesión para enviar la solicitud.")
            return self.form_invalid(form)

class SolicitudArriendoUpdateView(UpdateView):
    model = SolicitudArriendo
    form_class = SolicitudArriendoForm
    template_name = "inmueble/solicitud_form.html"
    success_url = reverse_lazy("solicitud_list")

class SolicitudArriendoDeleteView(DeleteView):
    model = SolicitudArriendo
    template_name = "inmueble/solicitud_confirm_delete.html"
    success_url = reverse_lazy("solicitud_list")

###CRUD PARA SOLICITUDES DE ARRIENDO
class PerfilUserUpdateView(UpdateView):
    model = PerfilUser
    form_class = PerfilUserForm
    template_name = "usuario/perfil_form.html"
    success_url = reverse_lazy("solicitud_list")

#######################################################################################
# TEMPLATES: REGISTER
#######################################################################################

###Register
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
###LOGIN
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
###LOGOUT
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect("login")

#######################################################################################
#TEMPLATES: WEB
#######################################################################################
def home(request):
    inmuebles = Inmueble.objects.all()[:5]
    return render(request, "web/home.html", {"inmuebles": inmuebles})


def acerca_view(request):
    return render(request, "web/acerca.html")

def contacto_view(request):
    if request.method == "POST":
        form = ContactDataForm(request.POST)
        if form.is_valid():
            ContactData.objects.create(
                customer_email=form.cleaned_data['customer_email'],
                customer_name=form.cleaned_data['customer_name'],
                message=form.cleaned_data['message']
            )
            messages.success(request, "Tu mensaje ha sido enviado con éxito. ¡Gracias por contactarnos!")
            return redirect('contacto')
    else:
        form = ContactDataForm()

    return render(request, "web/contacto.html", {"form": form})