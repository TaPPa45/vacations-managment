# Generated by Django 5.0.4 on 2024-04-18 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationrequest',
            name='status',
            field=models.CharField(choices=[('На рассмотрении', 'На рассмотрении'), ('Одобрено', 'Одобрено'), ('Отклонено', 'Отклонено')], default='На рассмотрении', max_length=15),
        ),
    ]
