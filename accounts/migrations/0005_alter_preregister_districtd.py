# Generated by Django 4.2.3 on 2023-07-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_data_cas_cat_alter_data_districtd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preregister',
            name='districtd',
            field=models.PositiveIntegerField(choices=[(1, 'Thiruvananthapuram'), (2, 'Kollam'), (3, 'Pathanamthitta'), (4, 'Alappuzha'), (5, 'Kottayam'), (6, 'Idukki'), (7, 'Ernakulam'), (8, 'Thrissur'), (9, 'Palakkad'), (10, 'Malappuram'), (11, 'Kozhikode'), (12, 'Wayanad'), (13, 'Kannur'), (14, 'Kasaragod')]),
        ),
    ]
