# Generated by Django 3.0.2 on 2020-12-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
    ]