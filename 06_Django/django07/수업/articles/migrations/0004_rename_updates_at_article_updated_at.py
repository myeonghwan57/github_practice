# Generated by Django 3.2.13 on 2022-10-04 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20221004_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='updates_at',
            new_name='updated_at',
        ),
    ]
