# Generated by Django 3.2.4 on 2021-06-08 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210608_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='customer_id',
            new_name='customer',
        ),
    ]
