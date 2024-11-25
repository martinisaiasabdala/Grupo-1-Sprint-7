from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Customer
from cuentas.models import CustomerAccount

@login_required
def customer_detail(request):
    customer = Customer.objects.get(user=request.user)
    cuenta = CustomerAccount.objects.get(fk_customer_account_customer=customer)
    return render(request, 'detail.html', {'customer': customer, 'cuenta': cuenta})