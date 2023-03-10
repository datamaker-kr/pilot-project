# Generated by Django 4.1.6 on 2023-03-14 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack', '0022_alter_snackemotion_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snackemotion',
            name='name',
            field=models.CharField(choices=[('like', '좋아요'), ('dislike', '싫어요')], max_length=50, verbose_name='name'),
        ),
        migrations.AddConstraint(
            model_name='snackemotion',
            constraint=models.UniqueConstraint(fields=('user', 'snack_request'), name='user_snack_request_unique_constraint'),
        ),
    ]
