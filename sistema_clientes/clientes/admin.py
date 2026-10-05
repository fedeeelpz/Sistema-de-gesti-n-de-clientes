from django.contrib import admin
from .models import Cliente, Deuda


class DeudaInline(admin.TabularInline):
    model = Deuda
    extra = 1


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'total_pendiente')
    inlines = [DeudaInline]


admin.site.register(Cliente, ClienteAdmin)
