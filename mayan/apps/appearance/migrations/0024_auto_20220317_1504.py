# Generated by Django 2.2.24 on 2022-03-17 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0023_auto_20220317_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'ordering': ('label',), 'verbose_name': 'Theme', 'verbose_name_plural': 'Themes'},
        ),
    ]
