# Generated by Django 4.0.10 on 2023-03-05 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0004_alter_customuser_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='User',
        ),
        migrations.AlterModelTable(
            name='user',
            table='auth_User',
        ),
    ]
