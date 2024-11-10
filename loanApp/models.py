from django.db import models
from django.contrib.auth.models import User
from loginApp.models import CustomerSignUp
import uuid

class loanRequest(models.Model):
    customer = models.ForeignKey(CustomerSignUp, on_delete=models.CASCADE, related_name='loan_customer')
    category = models.CharField(max_length=100, null=True, blank=True)
    request_date = models.DateField(auto_now_add=True)
    status_date = models.CharField(max_length=150, null=True, blank=True, default=None)
    reason = models.TextField()
    status = models.CharField(max_length=100, default='En cours de traitement')
    amount = models.PositiveIntegerField(default=0)
    year = models.PositiveIntegerField(default=1)
    advance_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_proof = models.ImageField(upload_to='payment_proofs/', null=True, blank=True)

    def __str__(self):
        return self.customer.user.username

    def save(self, *args, **kwargs):
        print(f"Saving loan request: {self.customer.user.username}, Category: {self.category}, Amount: {self.amount}, Advance Payment: {self.advance_payment}")
        super().save(*args, **kwargs)

class CustomerLoan(models.Model):
    customer = models.ForeignKey(CustomerSignUp, on_delete=models.CASCADE, related_name='loan_user')
    total_loan = models.PositiveIntegerField(default=0)
    payable_loan = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.customer.user.username

class loanTransaction(models.Model):
    customer = models.ForeignKey(CustomerSignUp, on_delete=models.CASCADE, related_name='transaction_customer')
    transaction = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment = models.PositiveIntegerField(default=0)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer.user.username