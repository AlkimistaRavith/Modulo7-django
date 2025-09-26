
from django.urls import path, include
from .views import *


urlpatterns = [
### REGIONES ################################################################################
    path("lista_regiones/", RegionListView.as_view() , name="region_list"),
    path("crear_region/", RegionCreateView.as_view() , name="region_create"),
    path("actualizar_region/<int:pk>", RegionUpdateView.as_view() , name="region_update"),
    path("borrar_region/<int:pk>", RegionDeleteView.as_view() , name="region_delete"),
### COMUNAS #################################################################################
    path("lista_comunas/", ComunaListView.as_view() , name="comuna_list"),
    path("crear_comuna/", ComunaCreateView.as_view() , name="comuna_create"),
    path("actualizar_comuna/<int:pk>", ComunaUpdateView.as_view() , name="comuna_update"),
    path("borrar_comuna/<int:pk>", ComunaDeleteView.as_view() , name="comuna_delete"),
### INMUEBLES ################################################################################
    path("lista_inmuebles/", InmuebleListView.as_view() , name="inmueble_list"),
    path("crear_inmueble/", InmuebleCreateView.as_view() , name="inmueble_create"),
    path("actualizar_inmueble/<int:pk>", InmuebleUpdateView.as_view() , name="inmueble_update"),
    path("borrar_inmueble/<int:pk>", InmuebleDeleteView.as_view() , name="inmueble_delete"),
    path("lista_inmuebles/<int:pk>/", InmuebleDetailView.as_view(), name="inmueble_detail"),
### SOLICITUDES ###############################################################################
    path("lista_solicitudes/", SolicitudArriendoListView.as_view() , name="solicitud_list"),
    path("crear_solicitud/", SolicitudArriendoCreateView.as_view() , name="solicitud_create"),
    path("actualizar_solicitud/<int:pk>", SolicitudArriendoUpdateView.as_view() , name="solicitud_update"),
    path("borrar_solicitud/<int:pk>", SolicitudArriendoDeleteView.as_view() , name="solicitud_delete"),
### PERFIL USER ###############################################################################
    path("actualizar_perfil/<int:pk>", PerfilUserUpdateView.as_view() , name="perfil_update"),

### LOGIN-LOGOUT ###############################################################################
    path("accounts/login/",  login_view,  name="login"),
    
    path("accounts/logout/", logout_view, name="logout"),
    path("accounts/register/", register_view, name="register"),

### LAYOUTS ###############################################################################
    path("", home , name="home"),
    path("acerca/", acerca_view, name="acerca"),
    path("contacto/", contacto_view, name="contacto"),
]