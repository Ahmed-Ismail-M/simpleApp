# Generated by Django 3.2.10 on 2022-01-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
