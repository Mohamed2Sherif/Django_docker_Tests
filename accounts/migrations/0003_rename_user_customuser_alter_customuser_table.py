# Generated by Django 4.0.10 on 2023-03-05 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0002_user_address_user_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='Cutomuser',
        ),
    ]
