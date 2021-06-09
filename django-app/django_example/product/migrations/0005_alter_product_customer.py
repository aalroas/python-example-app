# Generated by Django 3.2.4 on 2021-06-09 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_customer_id_product_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', related_query_name='customer_name', to='product.customer'),
        ),
    ]
