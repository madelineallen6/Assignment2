# Generated by Django 2.2.6 on 2020-02-29 02:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('organization', models.CharField(blank=True, max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('bldgroom', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('account_number', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('setup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('cleanup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('service_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('cust_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='crm.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('p_description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('pickup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('cust_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='crm.Customer')),
            ],
        ),
    ]
