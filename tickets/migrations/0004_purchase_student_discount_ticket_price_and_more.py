# Generated by Django 4.2.5 on 2024-03-19 14:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_ticket_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='student_discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(default=uuid.uuid4, max_length=10, unique=True),
        ),
    ]
