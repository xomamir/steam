# Generated by Django 4.2.2 on 2023-07-21 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_game_imgor_alter_invitecard_expiration_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='imgor',
            new_name='mane_imgor',
        ),
        migrations.AlterField(
            model_name='invitecard',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 20, 19, 28, 33, 133497), verbose_name='дата истечения'),
        ),
    ]
