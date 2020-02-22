from django.db import models
from django.utils import timezone
from services.models import AbstractUser, ModelMixin

# Create your models here.
class User(AbstractUser, ModelMixin):

    # device_token = models.CharField(max_length=255, blank=True, null=False)
    nickname = models.CharField(max_length=16)
    # phone_auth = models.OneToOneField(PhoneAuth, models.SET_NULL, null=True, blank=True, default=None,
    #                                   help_text="유저가 회원가입 시 사용한 PhoneAuth 객체. 없으면 인증받지 않았음을 의미")

    def __str__(self):
        return self.phone

    @property
    def is_store_owner(self):
        try:
            return self.store is not None
        except Store.DoesNotExist:
            return False
