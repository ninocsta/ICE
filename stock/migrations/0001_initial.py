# Generated by Django 5.0.6 on 2024-06-14 22:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_pricetable_product_cost_productprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('average_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='products.product')),
            ],
            options={
                'verbose_name': 'Estoque',
                'verbose_name_plural': 'Estoque',
            },
        ),
    ]
