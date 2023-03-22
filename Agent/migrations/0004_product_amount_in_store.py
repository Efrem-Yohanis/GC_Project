# Generated by Django 2.2.1 on 2022-06-17 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0003_agent_store_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Amount_in_Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('george', models.IntegerField(blank=True, default=0, null=True)),
                ('castel', models.IntegerField(blank=True, default=0, null=True)),
                ('doppel', models.IntegerField(blank=True, default=0, null=True)),
                ('senq', models.IntegerField(blank=True, default=0, null=True)),
                ('store', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Agent.Agent_Store')),
            ],
        ),
    ]