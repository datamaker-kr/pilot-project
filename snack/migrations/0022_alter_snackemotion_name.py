# Generated by Django 4.1.6 on 2023-03-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack', '0021_alter_snackrequest_snack_alter_snackrequest_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snackemotion',
            name='name',
            field=models.CharField(choices=[('likes', '좋아요'), ('dislikes', '싫어요')], max_length=50, verbose_name='name'),
        ),
    ]
