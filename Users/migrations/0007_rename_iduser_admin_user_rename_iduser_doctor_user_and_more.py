# Generated by Django 5.0 on 2024-01-05 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_user_banned'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='idUser',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='idUser',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='idUser',
            new_name='User',
        ),
    ]
