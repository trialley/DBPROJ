# Generated by Django 2.2.2 on 2019-12-01 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_auto_20191130_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browse',
            name='house_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='browse',
            name='user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='collection',
            name='house_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='collection',
            name='user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='deal',
            name='buyer_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='deal',
            name='house_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='deal',
            name='seller_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='deal',
            name='trader_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trader',
            name='trader_age',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_age',
            field=models.SmallIntegerField(),
        ),
    ]