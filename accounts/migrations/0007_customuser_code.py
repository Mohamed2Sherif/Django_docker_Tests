# Generated by Django 4.0.10 on 2023-03-05 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_user_customuser_alter_customuser_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='code',
            field=models.IntegerField(null=True),
        ),
    ]