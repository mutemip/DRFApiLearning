# Generated by Django 3.2.8 on 2021-10-21 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobBoard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
