
from django.urls import path
from .views import *



urlpatterns = [
    path("lista_regiones/", RegionListView.as_view() , name="region_list"),
    path("crear_region/", RegionCreateView.as_view() , name="region_create"),
    path("actualizar_region/<int:pk>", RegionUpdateView.as_view() , name="region_update"),

]