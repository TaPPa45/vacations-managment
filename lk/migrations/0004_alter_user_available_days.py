# Generated by Django 5.0.4 on 2024-04-18 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0003_user_is_14_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='available_days',
            field=models.IntegerField(blank=True, default=28, null=True),
        ),
    ]
