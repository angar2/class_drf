# Generated by Django 4.0.5 on 2022-06-23 08:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_article_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='노출 종료일'),
        ),
        migrations.AlterField(
            model_name='article',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='노출 시작일'),
        ),
    ]
