from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction

def index(request):
    transactions = Transaction.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'transactions': transactions})

def add_transaction(request):
    if request.method == 'POST':
        title = request.POST['title']
        amount = request.POST['amount']
        Transaction.objects.create(title=title, amount=amount)
        return redirect('/')
    return render(request, 'add.html')

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('/')