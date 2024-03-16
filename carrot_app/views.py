from django.shortcuts import render
from .models import * 
from .forms import * 
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, DeleteView, UpdateView


# Create your views here.

def home(request):
    return render(request, 'carrot_app/index.html')

#____________________Tortas_______________________
def tortas(request):
    return render(request, 'carrot_app/tortas.html')

def tortas_pedidos(request):
    tortas = Tortas.objects.all()
    contexto = {'tortas': tortas}
    return render(request, 'carrot_app/tortas_pedidos.html', contexto)



#____________________Pasteleria_______________________

def pasteleria(request):
    return render(request, 'carrot_app/pasteleria.html')

def pasteleria_pedidos(request):
    pasteleria = Pasteleria.objects.all()
    contexto = {'pasteleria': pasteleria}
    return render(request, 'carrot_app/pasteleria_pedidos.html', contexto)

#____________________Catering_______________________

def catering(request):
    return render(request, 'carrot_app/catering.html')

def catering_eventos(request):
    catering = Catering.objects.all()
    contexto = {'catering': catering}
    return render(request, 'carrot_app/catering_eventos.html', contexto)

#____________________Capacitaciones_______________________

def capacitaciones(request):
    return render(request, 'carrot_app/capacitaciones.html')

def capacitaciones_curso(request):
    capacitaciones = Capacitaciones.objects.all()
    contexto = {'capacitaciones': capacitaciones}
    return render(request, 'carrot_app/capacitaciones_curso.html', contexto)

#____________________________________________________________________________________________________________

#____________________Tortas_______________________

class TortasForm(FormView):

    form_class = TortasForm
    template_name = 'carrot_app/tortas_form.html'
    success_url = reverse_lazy('tortas')

class TortasCreate(CreateView):
    model = Tortas
    fields = '__all__'
    success_url = reverse_lazy('tortas_pedidos')

class TortasUpdate(UpdateView):
    model = Tortas
    fields = '__all__'
    success_url = reverse_lazy('tortas_pedidos')
    template_name = 'carrot_app/tortas_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        torta = self.get_object()  
        context['torta'] = torta   
        return context

class TortasDelete(DeleteView):
    model = Tortas
    success_url = reverse_lazy('tortas_pedidos')

#____________________Pasteleria_______________________

class PasteleriaForm(FormView):

    form_class = PasteleriaForm
    template_name = 'carrot_app/pasteleria_form.html'
    success_url = reverse_lazy('pasteleria')

class PasteleriaCreate(CreateView):
    model = Pasteleria
    fields = '__all__'
    success_url = reverse_lazy('pasteleria_pedidos')

class PasteleriaUpdate(UpdateView):
    model = Pasteleria
    fields = '__all__'
    success_url = reverse_lazy('pasteleria_pedidos')

class PasteleriaDelete(DeleteView):
    model = Pasteleria
    success_url = reverse_lazy('pasteleria_pedidos')


#____________________Catering_______________________
    
class CateringForm(FormView):

    form_class = CateringForm
    template_name = 'carrot_app/catering_form.html'
    success_url = reverse_lazy('catering')

class CateringCreate(CreateView):
    model = Catering
    fields = '__all__'
    success_url = reverse_lazy('catering_eventos')

class CateringUpdate(UpdateView):
    model = Catering
    fields = '__all__'
    success_url = reverse_lazy('catering_eventos')

class CateringDelete(DeleteView):
    model = Catering
    success_url = reverse_lazy('catering_eventos')

#____________________Capacitaciones_______________________

class CapacitacionesForm(FormView):

    form_class = CapacitacionesForm
    template_name = 'carrot_app/capacitaciones_form.html'
    success_url = reverse_lazy('capacitaciones')

class CapacitacionesCreate(CreateView):
    model = Capacitaciones
    fields = '__all__'
    success_url = reverse_lazy('capacitaciones_curso')

class CapacitacionesUpdate(UpdateView):
    model = Capacitaciones
    fields = '__all__'
    success_url = reverse_lazy('capacitaciones_curso')


class CapacitacionesDelete(DeleteView):
    model = Capacitaciones
    success_url = reverse_lazy('capacitaciones_curso')


