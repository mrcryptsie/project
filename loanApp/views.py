from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoanRequestForm, LoanTransactionForm
from .models import loanRequest, loanTransaction, CustomerLoan
from django.db.models import Sum

# @login_required(login_url='/account/login-customer')
def home(request):
    return render(request, 'home.html', context={})

herbicide_categories = [
    {
        'id': 1,
        'name': 'Herbicide A',
        'unit_cost': 100.00,
        'labor_cost_per_ha': 50.00,
        'file_fee_fcfa': 20.00,
    },
    {
        'id': 2,
        'name': 'Herbicide B',
        'unit_cost': 150.00,
        'labor_cost_per_ha': 75.00,
        'file_fee_fcfa': 30.00,
    },
    # Ajoutez d'autres catégories ici
]

@login_required(login_url='/account/login-customer')
def LoanRequest(request):
    if request.method == 'POST':
        form = LoanRequestForm(request.POST, request.FILES)
        print(f"Form data received: {request.POST}")  # Affiche les données du formulaire reçues
        if form.is_valid():
            print(f"Form is valid: {form.cleaned_data}")  # Affiche les données nettoyées du formulaire
            loan_obj = form.save(commit=False)
            loan_obj.customer = request.user.customer
            category_id = form.cleaned_data.get('category')
            category_name = next((category['name'] for category in herbicide_categories if category['id'] == int(category_id)), None)
            loan_obj.category = category_name
            advance_payment = form.cleaned_data.get('advance_payment')
            print(f"Advance Payment received: {advance_payment}")  # Affiche le montant de l'avance reçu
            loan_obj.advance_payment = advance_payment
            print(f"Category ID: {category_id}, Category Name: {category_name}")  # Affiche la catégorie sélectionnée
            print(f"Advance Payment: {advance_payment}")  # Affiche le montant de l'avance
            loan_obj.save()
            print(f"Loan request saved: {loan_obj.id}")  # Affiche l'ID de la demande de crédit enregistrée
            return redirect('/?success=true')
        else:
            print(f"Form is not valid: {form.errors}")  # Affiche les erreurs de validation du formulaire
    else:
        form = LoanRequestForm()

    return render(request, 'loanApp/loanrequest.html', context={'form': form, 'categories': herbicide_categories})




@login_required(login_url='/account/login-customer')
def LoanPayment(request):
    form = LoanTransactionForm()
    if request.method == 'POST':
        form = LoanTransactionForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.customer = request.user.customer
            payment.save()
            return redirect('/')

    return render(request, 'loanApp/payment.html', context={'form': form})

@login_required(login_url='/account/login-customer')
def UserTransaction(request):
    transactions = loanTransaction.objects.filter(customer=request.user.customer)
    return render(request, 'loanApp/user_transaction.html', context={'transactions': transactions})

@login_required(login_url='/account/login-customer')
def UserLoanHistory(request):
    loans = loanRequest.objects.filter(customer=request.user.customer)
    print(f"Loan history for user {request.user.username}: {loans}")
    return render(request, 'loanApp/user_loan_history.html', context={'loans': loans})

@login_required(login_url='/account/login-customer')
def UserDashboard(request):
    requestLoan = loanRequest.objects.filter(customer=request.user.customer).count()
    approved = loanRequest.objects.filter(customer=request.user.customer, status='approved').count()
    rejected = loanRequest.objects.filter(customer=request.user.customer, status='rejected').count()
    totalLoan = CustomerLoan.objects.filter(customer=request.user.customer).aggregate(Sum('total_loan'))['total_loan__sum'] or 0
    totalPayable = CustomerLoan.objects.filter(customer=request.user.customer).aggregate(Sum('payable_loan'))['payable_loan__sum'] or 0
    totalPaid = loanTransaction.objects.filter(customer=request.user.customer).aggregate(Sum('payment'))['payment__sum'] or 0

    dict = {
        'request': requestLoan,
        'approved': approved,
        'rejected': rejected,
        'totalLoan': totalLoan,
        'totalPayable': totalPayable,
        'totalPaid': totalPaid,
    }

    return render(request, 'loanApp/user_dashboard.html', context=dict)

def error_404_view(request, exception):
    return render(request, 'notFound.html')