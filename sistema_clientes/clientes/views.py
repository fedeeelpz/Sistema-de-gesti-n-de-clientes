from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Deuda
from .forms import ClienteForm, DeudaForm


def lista_clientes(request):
    query = request.GET.get('q', '')
    if query:
        clientes = Cliente.objects.filter(nombre__icontains=query) | Cliente.objects.filter(apellido__icontains=query)
    else:
        clientes = Cliente.objects.all()
    clientes = clientes.order_by('apellido', 'nombre')
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/nuevo_cliente.html', {'form': form})


def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect('lista_clientes')


def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    deudas = cliente.deudas.all().order_by('-fecha')

    if request.method == 'POST':
        form = DeudaForm(request.POST)
        if form.is_valid():
            nueva_deuda = form.save(commit=False)
            nueva_deuda.cliente = cliente
            nueva_deuda.save()
            return redirect('detalle_cliente', cliente_id=cliente.id)
    else:
        form = DeudaForm()

    return render(request, 'clientes/detalle_cliente.html', {
        'cliente': cliente,
        'deudas': deudas,
        'form': form,
    })


def editar_deuda(request, deuda_id):
    deuda = get_object_or_404(Deuda, id=deuda_id)

    if request.method == 'POST':
        deuda.monto = request.POST.get('monto')
        deuda.estado = request.POST.get('estado')
        deuda.save()

    return redirect('detalle_cliente', cliente_id=deuda.cliente.id)


def eliminar_deuda(request, deuda_id):
    deuda = get_object_or_404(Deuda, id=deuda_id)
    cliente_id = deuda.cliente.id
    deuda.delete()
    return redirect('detalle_cliente', cliente_id=cliente_id)