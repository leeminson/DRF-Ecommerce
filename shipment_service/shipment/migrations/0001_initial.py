# Generated by Django 3.1.12 on 2024-05-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('method', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('payment_id', models.IntegerField()),
            ],
        ),
    ]
