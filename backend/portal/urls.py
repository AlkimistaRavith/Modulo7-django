
from django.urls import path
from .views import *


urlpatterns = [
    path("lista_regiones/", RegionListView.as_view() , name="region_list"),
    path("crear_region/", RegionCreateView.as_view() , name="region_create"),
    path("actualizar_region/<int:pk>", RegionUpdateView.as_view() , name="region_update"),
    path("borrar_region/<int:pk>", RegionDeleteView.as_view() , name="region_delete"),
##############################################################################################
    path("lista_comunas/", ComunaListView.as_view() , name="comuna_list"),
    path("crear_comuna/", ComunaCreateView.as_view() , name="comuna_create"),
    path("actualizar_comuna/<int:pk>", ComunaUpdateView.as_view() , name="comuna_update"),
    path("borrar_comuna/<int:pk>", ComunaDeleteView.as_view() , name="comuna_delete"),
##############################################################################################
    path("lista_inmuebles/", InmuebleListView.as_view() , name="inmueble_list"),
    path("crear_inmueble/", InmuebleCreateView.as_view() , name="inmueble_create"),
    path("actualizar_inmueble/<int:pk>", InmuebleUpdateView.as_view() , name="inmueble_update"),
    path("borrar_inmueble/<int:pk>", InmuebleDeleteView.as_view() , name="inmueble_delete"),
##############################################################################################

# clase 01/09/25
    #path("", home , name="home"),
    path("accounts/login/",  login_view,  name="login"),
    path("accounts/logout/", logout_view, name="logout"),
    path("accounts/register/", register_view, name="register"),
]