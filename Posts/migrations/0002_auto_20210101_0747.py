# Generated by Django 2.2 on 2021-01-01 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='JoinDate',
            new_name='joinDate',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='Username',
            new_name='memberName',
        ),
    ]
