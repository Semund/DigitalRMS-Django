# Generated by Django 4.0.5 on 2022-07-07 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='checkout_date',
            field=models.DateField(),
        ),
    ]
