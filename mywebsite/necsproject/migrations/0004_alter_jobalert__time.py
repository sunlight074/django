# Generated by Django 4.2.1 on 2023-07-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('necsproject', '0003_alter_jobalert_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobalert',
            name='_time',
            field=models.DateTimeField(),
        ),
    ]
