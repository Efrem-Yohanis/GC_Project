# Generated by Django 4.1.3 on 2022-11-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0003_product_amount_in_store_adis_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_store',
            name='OnMap',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='coverArea',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]