# Generated by Django 2.2 on 2021-01-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_auto_20210101_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.BigIntegerField(default=0, verbose_name=' Like Count')),
                ('group', models.ManyToManyField(to='Posts.Group')),
            ],
        ),
    ]