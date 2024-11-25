# Generated by Django 5.1.2 on 2024-11-24 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_payment', models.CharField(max_length=50)),
                ('loan_date', models.DateField()),
                ('loan_total', models.IntegerField()),
                ('fk_loan_customer', models.ForeignKey(db_column='fk_loan_customer_id', on_delete=django.db.models.deletion.CASCADE, to='clientes.customer')),
            ],
            options={
                'db_table': 'Loan',
            },
        ),
    ]
