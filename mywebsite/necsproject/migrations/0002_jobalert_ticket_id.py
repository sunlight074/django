# Generated by Django 4.2.1 on 2023-08-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('necsproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobalert',
            name='ticket_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
