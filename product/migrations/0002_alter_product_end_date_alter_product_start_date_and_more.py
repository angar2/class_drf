# Generated by Django 4.0.5 on 2022-06-23 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='노출 종료일'),
        ),
        migrations.AlterField(
            model_name='product',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='노출 시작일'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.FileField(upload_to='img/', verbose_name='썸네일'),
        ),
    ]
