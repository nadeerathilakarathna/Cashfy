# Generated by Django 5.0 on 2023-12-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashfy', '0002_account_category_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.IntegerField(),
        ),
    ]