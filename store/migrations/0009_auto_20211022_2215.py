# Generated by Django 3.2.8 on 2021-10-22 17:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20211018_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.cart'),
        ),
    ]
