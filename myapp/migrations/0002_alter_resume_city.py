# Generated by Django 4.1.6 on 2023-08-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='city',
            field=models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Biratnagar', 'Biratnagar'), ('Pokhara', 'Pokhara'), ('Dharan', 'Dharan'), ('Chitwan', 'Chitwan'), ('Janakpur', 'Janakpur')], max_length=30),
        ),
    ]
