from django.urls import reverse_lazy
from .models import (
    Region
)
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView
)
from .form import (
    RegionForm
)





# Create your views here.

# CRUD para regiones

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