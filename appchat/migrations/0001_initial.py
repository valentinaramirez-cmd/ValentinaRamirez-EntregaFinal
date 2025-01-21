# Generated by Django 5.1.3 on 2024-12-27 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appuser', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.ManyToManyField(to='appuser.user')),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Enviado')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appchat.chatroom', verbose_name='Chat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appuser.user')),
            ],
        ),
    ]
