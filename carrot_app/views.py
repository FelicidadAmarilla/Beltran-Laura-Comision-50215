from django.shortcuts import render
from .models import * 
from .forms import * 
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, DeleteView, UpdateView


# Create your views here.

def home(request):
    return render(request, 'carrot_app/index.html')

def tortas(request):
    return render(request, 'carrot_app/tortas.html')

def tortas_pedidos(request):
    tortas = Tortas.objects.all()
    contexto = {'tortas': tortas}
    return render(request, 'carrot_app/tortas_pedidos.html', contexto)

def search_pedidos(request):
    search_query = request.GET.get('search', '')
    tortas = Tortas.objects.filter(nombre__icontains=search_query)
    return render(request, 'tortas_pedidos.html', {'tortas': tortas})

def pasteleria(request):
    return render(request, 'carrot_app/pasteleria.html')

def catering(request):
    return render(request, 'carrot_app/catering.html')

def capacitaciones(request):
    return render(request, 'carrot_app/capacitaciones.html')


#____________________ Forms ____________________

class TortasForm(FormView):

    form_class = TortasForm
    template_name = 'carrot_app/tortas_form.html'
    success_url = reverse_lazy('tortas')

class TortasCreate(CreateView):
    model = Tortas
    fields = '__all__'
    success_url = reverse_lazy('tortas')

class TortaUpdate(UpdateView):
    model = Tortas
    fields = '__all__'
    success_url = reverse_lazy('tortas_pedidos')

class TortasDelete(DeleteView):
    model = Tortas
    success_url = reverse_lazy('tortas_pedidos')

class PasteleriaForm(FormView):

    form_class = PasteleriaForm
    template_name = 'carrot_app/pasteleria_form.html'
    success_url = reverse_lazy('pasteleria')

class PasteleriaCreateView(CreateView):
    model = Pasteleria
    form_class = PasteleriaForm
    template_name = 'pasteleria_form.html'
    success_url = reverse_lazy('pasteleria')

class PasteleriaUpdateView(UpdateView):
    model = Pasteleria
    form_class = PasteleriaForm
    template_name = 'pasteleria_form.html'
    success_url = reverse_lazy('pasteleria')

class CateringForm(FormView):

    form_class = CateringForm
    template_name = 'carrot_app/catering_form.html'
    success_url = reverse_lazy('catering')

class CateringCreateView(CreateView):
    model = Catering
    form_class = CateringForm
    template_name = 'catering_form.html'
    success_url = reverse_lazy('catering')

class CateringUpdateView(UpdateView):
    model = Catering
    form_class = CateringForm
    template_name = 'catering_form.html'
    success_url = reverse_lazy('catering')

class CapacitacionesForm(FormView):

    form_class = CapacitacionesForm
    template_name = 'carrot_app/capacitaciones_form.html'
    success_url = reverse_lazy('capacitaciones')

class CapacitacionesCreateView(CreateView):
    model = Capacitaciones
    form_class = CapacitacionesForm
    template_name = 'capacitaciones_form.html'
    success_url = reverse_lazy('capacitaciones')

class CapacitacionesUpdateView(UpdateView):
    model = Capacitaciones
    form_class = CapacitacionesForm
    template_name = 'capacitacioness_form.html'
    success_url = reverse_lazy('capacitaciones')


