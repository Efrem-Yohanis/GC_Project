# Generated by Django 3.2.9 on 2022-11-10 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0008_remove_productnew_price_in_creates_custom_recom'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RenameField(
            model_name='product_amount_in_store',
            old_name='castel',
            new_name='Castle',
        ),
        migrations.RenameField(
            model_name='product_amount_in_store',
            old_name='doppel',
            new_name='Doppel',
        ),
        migrations.RenameField(
            model_name='product_amount_in_store',
            old_name='george',
            new_name='George',
        ),
        migrations.RenameField(
            model_name='product_amount_in_store',
            old_name='senq',
            new_name="Sen'q",
        ),
    ]