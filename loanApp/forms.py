from django import forms
from .models import loanRequest, loanTransaction

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = loanRequest
        fields = ('category', 'reason', 'amount', 'year', 'payment_proof', 'advance_payment')

    def clean(self):
        cleaned_data = super().clean()
        print(f"Cleaned data: {cleaned_data}")  # Affiche les données nettoyées après validation
        return cleaned_data

class LoanTransactionForm(forms.ModelForm):
    class Meta:
        model = loanTransaction
        fields = ('payment',)
