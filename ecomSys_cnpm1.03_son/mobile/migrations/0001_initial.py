# Generated by Django 3.1.12 on 2024-04-20 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('cpu', models.CharField(max_length=100)),
                ('ram', models.IntegerField()),
                ('release_date', models.DateField()),
                ('display_size', models.FloatField()),
                ('storage_capacity', models.PositiveIntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.mobilebrand')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('product.product',),
        ),
    ]
