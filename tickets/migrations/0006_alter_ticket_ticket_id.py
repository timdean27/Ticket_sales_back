# Generated by Django 4.2.5 on 2024-04-12 12:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_alter_ticket_ticket_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]