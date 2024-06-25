# Generated by Django 5.0.6 on 2024-06-24 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_pricetable_product_cost_productprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]