# Generated by Django 5.1.3 on 2025-01-20 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appchat', '0005_alter_mensaje_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='mensajes',
            field=models.ManyToManyField(blank=True, null=True, to='appchat.mensaje'),
        ),
    ]
