# Generated by Django 4.1 on 2022-09-05 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petcareapp', '0013_foodcare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booknowform',
            name='address',
            field=models.CharField(default=datetime.datetime(2022, 9, 5, 7, 26, 43, 394882, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booknowform',
            name='email_id',
            field=models.EmailField(default=datetime.datetime(2022, 9, 5, 7, 26, 51, 688987, tzinfo=datetime.timezone.utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booknowform',
            name='firstname',
            field=models.CharField(default=datetime.datetime(2022, 9, 5, 7, 27, 0, 18335, tzinfo=datetime.timezone.utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booknowform',
            name='lastname',
            field=models.CharField(default=datetime.datetime(2022, 9, 5, 7, 27, 12, 877874, tzinfo=datetime.timezone.utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booknowform',
            name='phone_no',
            field=models.CharField(default=datetime.datetime(2022, 9, 5, 7, 27, 22, 605111, tzinfo=datetime.timezone.utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='address',
            field=models.CharField(default=datetime.datetime(2022, 9, 5, 7, 27, 29, 747228, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email_id',
            field=models.EmailField(default=datetime.datetime(2022, 9, 5, 7, 27, 37, 141520, tzinfo=datetime.timezone.utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='firstname',
            field=models.CharField(default=datetime.datetime(2022, 9, 5, 7, 27, 45, 641611, tzinfo=datetime.timezone.utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='lastname',
            field=models.CharField(default=datetime.datetime(2022, 9, 5, 7, 27, 51, 958589, tzinfo=datetime.timezone.utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='phone_no',
            field=models.CharField(default=datetime.datetime(2022, 9, 5, 7, 28, 3, 532938, tzinfo=datetime.timezone.utc), max_length=10),
            preserve_default=False,
        ),
    ]