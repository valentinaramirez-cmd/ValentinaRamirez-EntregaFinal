# Generated by Django 5.1.3 on 2024-12-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appchat', '0002_chatroom_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='chat',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='mensajes',
            field=models.ManyToManyField(to='appchat.mensaje'),
        ),
    ]
