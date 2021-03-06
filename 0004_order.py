# Generated by Django 3.0.6 on 2020-06-01 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5200)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=505)),
                ('zip_code', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
