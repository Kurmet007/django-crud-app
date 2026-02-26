from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView

# ---------------------------
# Transactions
# ---------------------------
@login_required
def index(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')
    total = sum(t.amount for t in transactions)
    return render(request, 'index.html', {'transactions': transactions, 'total': total})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        title = request.POST['title']
        amount = request.POST['amount']
        Transaction.objects.create(user=request.user, title=title, amount=amount)
        return redirect('index')
    return render(request, 'add.html')

@login_required
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.title = request.POST['title']
        transaction.amount = request.POST['amount']
        transaction.save()
        return redirect('index')
    return render(request, 'edit.html', {'transaction': transaction})

@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    transaction.delete()
    return redirect('index')

# ---------------------------
# User registration
# ---------------------------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})