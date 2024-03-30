from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import * 
from .forms import * 

from django.views.generic import FormView, CreateView, DeleteView, UpdateView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render(request, 'carrot_app/index.html')

#____________________Tortas_______________________

@login_required
def tortas(request):
    return render(request, 'carrot_app/tortas.html')
@login_required
def tortas_pedidos(request):
    tortas = Tortas.objects.all()
    contexto = {'tortas': tortas}
    return render(request, 'carrot_app/tortas_pedidos.html', contexto)
@login_required
def search_pedidos_tor(request):
    search_query = request.GET.get('search', '')
    tortas = Tortas.objects.filter(nombre__icontains=search_query)
    return render(request, 'carrot_app/tortas_pedidos.html', {'tortas': tortas})

#____________________Pasteleria_______________________
@login_required
def pasteleria(request):
    return render(request, 'carrot_app/pasteleria.html')
@login_required
def pasteleria_pedidos(request):
    pasteleria = Pasteleria.objects.all()
    contexto = {'pasteleria': pasteleria}
    return render(request, 'carrot_app/pasteleria_pedidos.html', contexto)
@login_required
def search_pedidos_past(request):
    search_query = request.GET.get('search_past', '')
    productos = Pasteleria.objects.filter(producto__icontains=search_query)
    return render(request, 'carrot_app/pasteleria_pedidos.html', {'productos': productos})

#____________________Catering_______________________
@login_required
def catering(request):
    return render(request, 'carrot_app/catering.html')
@login_required
def catering_eventos(request):
    catering = Catering.objects.all()
    contexto = {'catering': catering}
    return render(request, 'carrot_app/catering_eventos.html', contexto)
@login_required
def search_eventos(request):
    search_query = request.GET.get('search', '')
    eventos = Catering.objects.filter(evento__icontains=search_query)
    return render(request, 'carrot_app/catering_eventos.html', {'eventos': eventos})


#____________________Capacitaciones_______________________
@login_required
def capacitaciones(request):
    return render(request, 'carrot_app/capacitaciones.html')
@login_required
def capacitaciones_curso(request):
    capacitaciones = Capacitaciones.objects.all()
    contexto = {'capacitaciones': capacitaciones}
    return render(request, 'carrot_app/capacitaciones_curso.html', contexto)
@login_required
def search_curso(request):
    search_query = request.GET.get('search', '')
    curso = Tortas.objects.filter(nombre__icontains=search_query)
    return render(request, 'carrot_app/catering_curso.html', {'curso': curso})


#____________________________________________________________________________________________________________

#____________________Tortas_______________________


class TortasForm(LoginRequiredMixin,FormView):

    form_class = TortasForm
    template_name = 'carrot_app/tortas_form.html'
    success_url = reverse_lazy('tortas')

class TortasCreate(LoginRequiredMixin,CreateView):
    model = Tortas
    fields = '__all__'
    success_url = reverse_lazy('tortas_pedidos')

class TortasUpdate(LoginRequiredMixin,UpdateView):
    model = Tortas
    fields = '__all__'
    success_url = reverse_lazy('tortas_pedidos')
    template_name = 'carrot_app/tortas_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        torta = self.get_object()  
        context['torta'] = torta   
        return context    

class TortasDelete(LoginRequiredMixin,DeleteView):
    model = Tortas
    success_url = reverse_lazy('tortas_pedidos')


#____________________Pasteleria_______________________

class PasteleriaForm(LoginRequiredMixin,FormView):

    form_class = PasteleriaForm
    template_name = 'carrot_app/pasteleria_form.html'
    success_url = reverse_lazy('pasteleria')

class PasteleriaCreate(LoginRequiredMixin,CreateView):
    model = Pasteleria
    fields = '__all__'
    success_url = reverse_lazy('pasteleria_pedidos')

class PasteleriaUpdate(UpdateView):
    model = Pasteleria
    fields = '__all__'
    success_url = reverse_lazy('pasteleria_pedidos')
    template_name = 'carrot_app/pasteleria_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto = self.get_object()  
        context['producto'] = producto   
        return context

class PasteleriaDelete(DeleteView):
    model = Pasteleria
    success_url = reverse_lazy('pasteleria_pedidos')


#____________________Catering_______________________
    
class CateringForm(LoginRequiredMixin,FormView):

    form_class = CateringForm
    template_name = 'carrot_app/catering_form.html'
    success_url = reverse_lazy('catering')

class CateringCreate(LoginRequiredMixin,CreateView):
    model = Catering
    fields = '__all__'
    success_url = reverse_lazy('catering_eventos')

class CateringUpdate(LoginRequiredMixin,UpdateView):
    model = Catering
    fields = '__all__'
    success_url = reverse_lazy('catering_eventos')
    template_name = 'carrot_app/catering_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        evento = self.get_object()  
        context['evento'] = evento   
        return context

class CateringDelete(LoginRequiredMixin,DeleteView):
    
    model = Catering
    success_url = reverse_lazy('catering_eventos')

#____________________Capacitaciones_______________________

class CapacitacionesForm(LoginRequiredMixin,FormView):

    form_class = CapacitacionesForm
    template_name = 'carrot_app/capacitaciones_form.html'
    success_url = reverse_lazy('capacitaciones')

class CapacitacionesCreate(LoginRequiredMixin,CreateView):
    model = Capacitaciones
    fields = '__all__'
    success_url = reverse_lazy('capacitaciones_curso')

class CapacitacionesUpdate(LoginRequiredMixin,UpdateView):
    model = Capacitaciones
    fields = '__all__'
    success_url = reverse_lazy('capacitaciones_curso')
    template_name = 'carrot_app/capacitaciones_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curso = self.get_object()  
        context['curso'] = curso   
        return context

class CapacitacionesDelete(LoginRequiredMixin,DeleteView):
    model = Capacitaciones
    success_url = reverse_lazy('capacitaciones_curso')

#____________________Registro_______________________

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    else:
        form = RegistroForm()
    return render(request, 'carrot_app/registro.html', {'form': form})

#____________________Login, Logout, Avatar_______________________

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['password']
        user = authenticate(request, username=username, password=contraseña)
        if user is not None:
            login(request, user)
            return render(request, 'carrot_app/index.html')
        else:
            return redirect(reverse_lazy('login'))
        
        

    else:
        form = AuthenticationForm()
        return render(request, 'carrot_app/login.html', {'form': form})

@login_required
def logout_request(request):
    logout(request)
    return redirect(reverse_lazy('login'))