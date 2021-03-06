# Generated by Django 3.1.3 on 2020-11-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpr_db', '0004_auto_20201126_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='description',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='state',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='zip',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
