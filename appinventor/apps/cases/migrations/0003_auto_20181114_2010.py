# Generated by Django 2.0.1 on 2018-11-14 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_cases_submitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='cases_front_image',
            field=models.ImageField(blank=True, null=True, upload_to='Cases/fronts/', verbose_name='封面图'),
        ),
    ]