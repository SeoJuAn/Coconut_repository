# Generated by Django 3.2.4 on 2021-08-17 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.community')),
            ],
        ),
    ]
