# Generated by Django 4.2.1 on 2023-08-04 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='jobAlert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_id', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField()),
                ('search_name', models.CharField(max_length=200, null=True)),
                ('result_link', models.CharField(max_length=200, null=True)),
                ('results', models.TextField(null=True)),
                ('severity', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], max_length=200)),
                ('status', models.CharField(choices=[('Escalation', 'Escalation'), ('In progress', 'In progress'), ('Close', 'Close')], max_length=200)),
                ('app', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('assign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign', to=settings.AUTH_USER_MODEL)),
                ('report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_text', models.CharField(max_length=200, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('comment_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_person', to=settings.AUTH_USER_MODEL)),
                ('job_detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_detail_id', to='necsproject.jobalert')),
            ],
        ),
    ]
