# Generated by Django 3.2.13 on 2022-06-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessclass',
            name='instructor',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
