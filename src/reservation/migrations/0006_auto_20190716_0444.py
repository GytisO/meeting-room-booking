# Generated by Django 2.2.3 on 2019-07-16 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_auto_20190716_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='r_number',
            field=models.IntegerField(),
        ),
    ]
