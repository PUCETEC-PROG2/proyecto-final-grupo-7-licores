from django.core.validators import RegexValidator
from django.db import models
 
class Customer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)
    
    phone_validator = RegexValidator(
        regex=r'^09\d{8}$',
        message="El número de celular debe tener exactamente 10 numeros y comenzar con '09'."
    )
    nummber_phone = models.CharField(validators=[phone_validator], max_length=10, null=False)
    
    id_card_validator = RegexValidator(
        regex=r'^\d{10}$',
        message="El número de cédula ecuatoriana debe tener exactamente 10 numeros."
    )
    identification_card = models.CharField(
        validators=[id_card_validator],
        max_length=10,
        null=False
    )
 
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    TYPE_CHOICES = [
        ('Destilado', 'Destilado'),
        ('Vino', 'Vino'),
        ('Cerveza', 'Cerveza'),
        ('Licor', 'Licor'),
        ('Espirituoso', 'Espirituoso'),
        ('Aperitivo', 'Aperitivo'),
    ]
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, null=False)
    
    SWEETNESS_CHOICES = [
        ('Seco', 'Seco'),
        ('Semi-seco', 'Semi-seco'),
        ('Dulce', 'Dulce'),
    ]
    sweetness = models.CharField(max_length=30, choices=SWEETNESS_CHOICES, null=False)
    
    PERCENTAGE_CHOICES = [
        ('Baja graduacion', 'Baja graduación'),
        ('Media graduacion', 'Media graduación'),
        ('Alta graduacion', 'Alta graduación'),
    ]
    percentage = models.CharField(max_length=30, choices=PERCENTAGE_CHOICES, null=False)
    
    TASTING_CHOICES = [
        ('Para Cócteles', 'Para Cócteles'),
        ('Para Degustación', 'Para Degustación'),
    ]
    tasting = models.CharField(max_length=30, choices=TASTING_CHOICES, null=False)
 
    def __str__(self):
        return f"{self.name} ({self.type})"
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(null=False, default=1, max_digits=4, decimal_places=2)
    amount = models.IntegerField(default=1, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='product_images')
 
    def __str__(self):
        return f"{self.name}"
    
class Sale(models.Model):
    date = models.DateTimeField(null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.date} {self.customer} {self.price}"