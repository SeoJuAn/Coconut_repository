# Generated by Django 3.2.4 on 2021-07-06 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(default='', max_length=200)),
                ('point', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('nickname', models.CharField(default='', max_length=200)),
                ('user_name', models.CharField(default='', max_length=200)),
                ('address', models.CharField(default='', max_length=200)),
                ('phonenumber', models.CharField(default='', max_length=200)),
                ('subdate', models.CharField(default='', max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(default='', max_length=200)),
                ('coupon', models.IntegerField(default=0)),
                ('photo', models.CharField(default='', max_length=200)),
                ('sns', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(default='', max_length=200)),
                ('phonenumber', models.CharField(default='', max_length=200)),
                ('accountnumber', models.CharField(default='', max_length=200)),
                ('companyname', models.CharField(default='', max_length=200)),
                ('productcategory', models.CharField(default='', max_length=200)),
                ('address', models.CharField(default='', max_length=200)),
                ('operationtime', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StoreOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(default='', max_length=200)),
                ('point', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('nickname', models.CharField(default='', max_length=200)),
                ('user_name', models.CharField(default='', max_length=200)),
                ('phonenumber', models.CharField(default='', max_length=200)),
                ('subdate', models.CharField(default='', max_length=200)),
                ('sns', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
