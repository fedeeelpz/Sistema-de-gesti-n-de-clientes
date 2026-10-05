from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def total_pendiente(self):
        return sum(d.monto for d in self.deudas.filter(estado='pendiente'))


class Deuda(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='deudas')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"{self.cliente} - ${self.monto}"
