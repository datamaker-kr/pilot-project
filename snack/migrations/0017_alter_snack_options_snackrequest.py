# Generated by Django 4.1.6 on 2023-03-08 14:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snack', '0016_alter_snack_options_alter_snack_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snack',
            options={'ordering': ['-id'], 'verbose_name': 'snack', 'verbose_name_plural': 'snacks'},
        ),
        migrations.CreateModel(
            name='SnackRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, help_text=' 예) 5개 주문해주세요!', max_length=300, verbose_name='DESCRIPTION')),
                ('is_accepted', models.BooleanField(default=False, verbose_name='IS_ACCEPTED')),
                ('supply_year', models.PositiveSmallIntegerField(help_text=' 예) 2023', null=True, verbose_name='SUPPLY_YEAR')),
                ('supply_month', models.PositiveSmallIntegerField(help_text=' 예) 7', null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)], verbose_name='SUPPLY_MONTH')),
                ('create_dt', models.DateField(auto_now_add=True, verbose_name='CREATE_DT')),
                ('snack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snack.snack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
