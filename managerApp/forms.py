from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
#from loanApp.models import loanCategory


"""class LoanCategoryForm(forms.ModelForm):
    class Meta:
        model = loanCategory
        fields = ('loan_name',)
"""

"""class LoanCategoryForm(forms.ModelForm):
    class Meta:
        model = loanCategory
        fields = ['loan_name', 'herbicide_name', 'unit_cost', 'labor_cost_per_ha', 'file_fee_fcfa']  # Ajout des nouveaux champs
        widgets = {
            'loan_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'herbicide_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'unit_cost': forms.NumberInput(attrs={'class': 'form-control', 'required': 'true'}),
            'labor_cost_per_ha': forms.NumberInput(attrs={'class': 'form-control', 'required': 'true'}),
            'file_fee_fcfa': forms.NumberInput(attrs={'class': 'form-control', 'required': 'true'}),
        }
"""

"""class LoanCategoryForm(forms.ModelForm):
    class Meta:
        model = loanCategory
        fields = ['herbicide_name', 'unit_cost', 'labor_cost_per_ha', 'file_fee_fcfa']  # Champs du modèle LoanCategory

        # Ajouter des widgets pour personnaliser l'apparence des champs, si nécessaire
        widgets = {
            'herbicide_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom de l\'herbicide'}),
            'unit_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Coût unitaire herbicide (en FCFA)'}),
            'labor_cost_per_ha': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Coût de travail par ha (en FCFA)'}),
            'file_fee_fcfa': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Frais de dossier (en FCFA)'}),
        }
"""

        

class AdminLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
