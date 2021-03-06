# Generated by Django 3.2.4 on 2021-06-08 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='product.customer'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='"customers"',
        ),
        migrations.AlterModelTable(
            name='product',
            table='"products"',
        ),
    ]
