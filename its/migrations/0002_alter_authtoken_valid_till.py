# Generated by Django 4.2.4 on 2024-02-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('its', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtoken',
            name='valid_till',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
