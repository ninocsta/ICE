# Generated by Django 5.0.6 on 2024-06-13 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricetables', '0001_initial'),
        ('products', '0003_alter_product_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricetable',
            name='title',
        ),
        migrations.AddField(
            model_name='pricetable',
            name='table_name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pricetable',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='products.product'),
        ),
    ]