from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from user.models import User


class Snack(models.Model):
    name = models.CharField('NAME', max_length=50, unique=True)
    image = models.ImageField('IMAGE', upload_to='snack/images/')
    url = models.URLField('URL', max_length=500)

    class Meta:
        verbose_name = 'snack'
        verbose_name_plural = 'snacks'
        db_table = 'snack_snacks'
        ordering = ['-id']

    def __str__(self):
        return self.name


class SnackRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="snackRequests")
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE, related_name="snackRequests")
    description = models.CharField('DESCRIPTION', max_length=300, blank=True, help_text=' 예) 5개 주문해주세요!')
    is_accepted = models.BooleanField('IS_ACCEPTED', default=False)
    supply_year = models.PositiveSmallIntegerField('SUPPLY_YEAR', null=True, blank=True, help_text=' 예) 2023')
    supply_month = models.PositiveSmallIntegerField(
        'SUPPLY_MONTH', null=True, blank=True,
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1),
        ],
        help_text=' 예) 7'
    )
    create_dt = models.DateField('CREATE_DT', auto_now_add=True)  # 생성될 때 시각을 자동으로 기록

    @property
    def likes(self):
        return SnackEmotion.objects.filter(snack_request=self, name="like").count()

    @property
    def dislikes(self):
        return SnackEmotion.objects.filter(snack_request=self, name="dislike").count()


    class Meta:
        verbose_name = 'snack_request'
        verbose_name_plural = 'snack_requests'
        db_table = 'snack_snack_requests'
        ordering = ['-id']


class SnackEmotion(models.Model):
    class EmotionCategory(models.TextChoices):
        LIKE = 'like', '좋아요'
        DISLIKE = 'dislike', '싫어요'

    name = models.CharField('name', max_length=50, choices=EmotionCategory.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="snackEmotions")
    snack_request = models.ForeignKey(SnackRequest, on_delete=models.CASCADE, related_name="snackEmotions")
