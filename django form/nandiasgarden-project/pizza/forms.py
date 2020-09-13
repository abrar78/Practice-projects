from django import forms
from .models import Pizza,Size


# class PizzaForm (forms.Form):
#     toping1=forms.CharField(label='Topping 1',max_length=100)
#     toping2=forms.CharField(label='Topping 2',max_length=100)
    # toppings=forms.MultipleChoiceField(choices=[('pep','Pepperoni'),('cheese','Cheese'),('olive','Olive')],widget=forms.CheckboxSelectMultiple)
    # size=forms.ChoiceField(label='Size',choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])

class PizzaForm(forms.ModelForm):

#    size=forms.ModelChoiceField(queryset=Size.objects , empty_label=None ,
#                             widget=forms.RadioSelect)
#    image=forms.ImageField()
# email=forms.EmailField()
   class Meta:
       model = Pizza
       fields = ['toping1','toping2','size']
       labels={'toping1':'Topping 1','toping2':'Topping 2'}
    #    widgets={'size':forms.CheckboxSelectMultiple}
    
class MultiplePizzaForm(forms.Form):
    number=forms.IntegerField(min_value=2, max_value=6)