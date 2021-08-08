# Generated by Django 3.2.3 on 2021-07-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_score',
            new_name='product_review_score',
        ),
        migrations.AddField(
            model_name='review',
            name='takeout_review_score',
            field=models.FloatField(default=0),
        ),
    ]
