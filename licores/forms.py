from django import forms
from .models import Customer, Category, Product, Sale

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nummber_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'identification_card': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'birth_date': 'Fecha de Nacimiento',
            'nummber_phone': 'Teléfono',
            'identification_card': 'Cédula de Identidad'
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'sweetness': forms.Select(attrs={'class': 'form-control'}),
            'percentage': forms.Select(attrs={'class': 'form-control'}),
            'tasting': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nombre de la Categoría',
            'type': 'Tipo',
            'sweetness': 'Dulzura',
            'percentage': 'Porcentaje de Alcohol',
            'tasting': 'Tipo de Cata',
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'name': 'Nombre del Producto',
            'price': 'Precio',
            'amount': 'Cantidad',
            'category': 'Categoría',
            'picture': 'Imagen del Producto',
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'date']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'customer': 'Cliente',
            'date': 'Fecha',
        }

class SaleProductForm(forms.Form):
    select = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    product_id = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly': 'readonly', 'class': 'form-control'}))
    product_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}))
    quantity = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.HiddenInput())

# Creación de un formset para manejar múltiples productos en la venta
from django.forms import formset_factory
SaleProductFormSet = formset_factory(SaleProductForm, extra=0) # No se agregarán formularios adicionales automáticamente