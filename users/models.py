from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER,"Other")
    )

    LANG_ENGLISH = "en"
    LANG_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANG_ENGLISH, "Emnglish"),
        (LANG_KOREAN, "Korean")
    )

    CURRENCY_USD = "usd"
    CURRENCY_KOR = "krw"

    CURRENCY_CHOCIES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KOR, "KRW")
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True,  blank=True)
    bio = models.TextField(default="",  blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True)
    currency = models.CharField(
        choices = CURRENCY_CHOCIES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)
