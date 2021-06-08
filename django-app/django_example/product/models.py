from django.db import models

# Create your models here.

class Customer(models.Model):
    class Meta:
        db_table = 'customers'
        
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

    
class Product(models.Model):
    class Meta:
        db_table = 'products'
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE,related_name='customers')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    

    


      