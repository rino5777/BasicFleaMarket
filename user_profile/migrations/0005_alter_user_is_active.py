# Generated by Django 3.2.10 on 2022-08-24 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Прошел активацию?'),
        ),
    ]
