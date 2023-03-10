# Generated by Django 4.1.6 on 2023-02-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack', '0005_alter_snack_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='description',
            field=models.CharField(blank=True, help_text=' (개수 등 설명 추가)', max_length=300, verbose_name='DESCRIPTION'),
        ),
        migrations.AlterField(
            model_name='snack',
            name='url',
            field=models.URLField(max_length=500, verbose_name='URL'),
        ),
    ]
