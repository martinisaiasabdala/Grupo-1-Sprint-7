from django.db import models

# Create your models here.
from clientes.models import Customer  # Importar relaciones externas

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_payment = models.CharField(max_length=50)
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    fk_loan_customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='fk_loan_customer_id')

    class Meta:
        db_table = 'Loan'

    def __str__(self):
        return f"Préstamo {self.loan_id} - Total: {self.loan_total}"