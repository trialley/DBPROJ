# Generated by Django 2.2.2 on 2019-11-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Browses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=50)),
                ('house_id', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=50)),
                ('house_id', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('deal_id', models.AutoField(primary_key=True, serialize=False)),
                ('house_id', models.IntegerField(max_length=50)),
                ('buyer_id', models.IntegerField(max_length=50)),
                ('seller_id', models.IntegerField(max_length=50)),
                ('trader_id', models.IntegerField(max_length=50)),
                ('deal_price', models.DecimalField(decimal_places=3, max_digits=20)),
                ('deal_fee', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Traders',
            fields=[
                ('trader_id', models.AutoField(primary_key=True, serialize=False)),
                ('trader_name', models.CharField(max_length=50)),
                ('trader_sex', models.CharField(max_length=50)),
                ('trader_age', models.SmallIntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('user_sex', models.CharField(max_length=50)),
                ('user_age', models.SmallIntegerField(max_length=4)),
                ('user_tel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Villages',
            fields=[
                ('village_id', models.AutoField(primary_key=True, serialize=False)),
                ('village_position', models.DecimalField(decimal_places=3, max_digits=10)),
                ('village_name', models.CharField(max_length=50)),
                ('village_introduce', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='House',
            new_name='Houses',
        ),
    ]