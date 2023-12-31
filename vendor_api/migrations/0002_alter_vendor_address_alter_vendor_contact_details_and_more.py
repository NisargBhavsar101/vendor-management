# Generated by Django 4.2.7 on 2023-12-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.TextField(default='action'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='contact_details',
            field=models.TextField(default='action'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(default='action', max_length=255),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(default='action', max_length=50, unique=True),
        ),
    ]
