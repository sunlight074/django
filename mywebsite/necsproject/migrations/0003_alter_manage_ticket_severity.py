# Generated by Django 4.2.1 on 2023-07-05 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('necsproject', '0002_manage_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manage_ticket',
            name='severity',
            field=models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], max_length=200),
        ),
    ]
