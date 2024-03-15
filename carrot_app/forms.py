from django.forms import ModelForm 
from .models import * 

class TortasForm (ModelForm):
    
    class Meta:

     model = Tortas
     fields = '__all__'

class CateringForm(ModelForm):

    class Meta:

     model = Catering
     fields = '__all__'

class PasteleriaForm(ModelForm):
   
   class Meta:

     model = Pasteleria
     fields = '__all__'
    
   
class CapacitacionesForm(ModelForm):
   
   class Meta:

     model = Capacitaciones
     fields = '__all__'
    