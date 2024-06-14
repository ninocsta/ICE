from django.db import models



class Client(models.Model):
    name = models.CharField(max_length=120)
    cpfcnpj = models.CharField(max_length=20, null=True, blank=True, unique=True)    
    fone = models.CharField(max_length=20, null=True, blank=True)
    adress = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.name}'