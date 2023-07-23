# Generated by Django 4.2.3 on 2023-07-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prereg_name', models.CharField(max_length=100)),
                ('prereg_email', models.EmailField(max_length=254)),
                ('prereg_mob', models.CharField(max_length=15)),
                ('districtd', models.PositiveIntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2')])),
            ],
        ),
    ]
