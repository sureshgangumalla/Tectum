# Generated by Django 2.0.7 on 2018-08-08 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apartments', '0002_userclicks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userclicks',
            name='apartment_id',
        ),
        migrations.RemoveField(
            model_name='userclicks',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='userClicks',
        ),
    ]