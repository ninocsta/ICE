# Generated by Django 5.0.6 on 2024-06-18 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['quantity'], 'verbose_name': 'Estoque', 'verbose_name_plural': 'Estoque'},
        ),
    ]