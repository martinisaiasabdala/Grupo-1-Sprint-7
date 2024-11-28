from django.db import models
from clientes.models import Customer 
from django.utils.timezone import now

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
     # Tipo de préstamo
    loan_type = models.CharField(
        max_length=20,
        choices=[
            ('BLACK', 'Black'),
            ('GOLD', 'Gold'),
            ('CLASSIC', 'Classic'),
        ],
        default='CLASSIC'
    ) 
    loan_date = models.DateField()  # Fecha de inicio
    loan_total = models.IntegerField()  # Monto solicitado
    # Estado prestado
    loan_status = models.CharField(
        max_length=20,
        choices=[
            ('APPROVED', 'Aprobado'),
            ('REJECTED', 'Rechazado'),
            ('PENDING', 'Pendiente'),
        ],
        default='PENDING'
    )  
    # Relaacion con el cliente
    fk_loan_customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        db_column='fk_loan_customer_id'
    )  
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creacion

    class Meta:
        db_table = 'Loan'

    def _str_(self):
        return f"Préstamo {self.loan_id} - {self.loan_total} ({self.loan_status})"