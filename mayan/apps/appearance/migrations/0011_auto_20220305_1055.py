# Generated by Django 2.2.24 on 2022-03-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0010_auto_20220305_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='logofile',
            field=models.ImageField(blank=True, null=True, upload_to='static/appearance/images'),
        ),
    ]
