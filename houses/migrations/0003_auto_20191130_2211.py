# Generated by Django 2.2.2 on 2019-11-30 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20191130_2157'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Collections',
            new_name='Browse',
        ),
        migrations.RenameModel(
            old_name='Browses',
            new_name='Collection',
        ),
        migrations.RenameModel(
            old_name='Deals',
            new_name='Deal',
        ),
        migrations.RenameModel(
            old_name='Houses',
            new_name='House',
        ),
        migrations.RenameModel(
            old_name='Traders',
            new_name='Trader',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.RenameModel(
            old_name='Villages',
            new_name='Village',
        ),
    ]