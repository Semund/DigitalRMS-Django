# Generated by Django 4.0.5 on 2022-06-28 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_remove_booking_guest_booking_guests'),
        ('room_automation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomautomation',
            name='room_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.room', verbose_name='Номер'),
        ),
    ]