# Generated by Django 5.0.4 on 2024-04-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0003_vacationrequest_days_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacationrequest',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='комментарий'),
        ),
    ]