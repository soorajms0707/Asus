# Generated by Django 4.1.4 on 2023-02-22 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asus', '0005_alter_pmodel_pdescription_alter_pmodel_pname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmodel',
            name='pdescription',
            field=models.CharField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='pmodel',
            name='pname',
            field=models.CharField(max_length=500),
        ),
    ]
