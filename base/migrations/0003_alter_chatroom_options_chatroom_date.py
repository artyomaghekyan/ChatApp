# Generated by Django 4.1.5 on 2023-03-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_chatmessages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatroom',
            options={'ordering': ('date',)},
        ),
        migrations.AddField(
            model_name='chatroom',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
