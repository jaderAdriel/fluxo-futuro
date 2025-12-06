from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm

# Listar transações
def index(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'pages/finance/index.html', {'transactions': transactions})

# Detalhar transação
def detail(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    return render(request, 'pages/finance/detail.html', {'transaction': transaction})

# Criar nova transação
def create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-finances')
    else:
        form = TransactionForm()
    context = {"form": form, "is_create": True}
    return render(request, 'pages/finance/form.html', context)

# Editar transação
def edit(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('list-finances')
    else:
        form = TransactionForm(instance=transaction)
    context = {"form": form, "is_edit": True}
    return render(request, 'pages/finance/form.html', context)

# Deletar transação
def delete(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    if request.method == 'POST':
        transaction.delete()
        return redirect('list-finances')
    context = {"transaction": transaction, "is_delete": True}
    return render(request, 'pages/finance/form.html', context)
