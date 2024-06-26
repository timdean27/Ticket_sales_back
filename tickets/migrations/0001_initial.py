# Generated by Django 4.2.5 on 2024-04-29 12:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('concert', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('date_of_purchase', models.DateField()),
                ('tickets', models.JSONField(default=dict)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_sold', models.BooleanField(default=False)),
                ('seat_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(400)])),
                ('price', models.DecimalField(decimal_places=2, default=40, max_digits=5)),
                ('price_type', models.CharField(choices=[('premium', 'Premium'), ('standard', 'Standard'), ('student', 'Student')], default='standard', max_length=20)),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickets.concert')),
            ],
        ),
    ]
