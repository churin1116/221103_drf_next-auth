from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from uuid import uuid4
from django.utils import timezone


class CustomUserManager(BaseUserManager):
	
	use_in_migrations = True

	def _create_user(self, request_data, password, **extra_fields):
		if not request_data['email']:
			raise ValueError('emailを入力してください')
		if not request_data['username']:
			raise ValueError('usernameを入力してください')
		email = self.normalize_email(request_data['email'])
		user = self.model(
			username=request_data['username'],
			email=email,
			image_url=request_data['image_url'],
			**extra_fields
		)
		user.set_password(password)
		user.save(using=self.db)
		return user

	def create_user(self, request_data, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(request_data, password, **extra_fields)
	
	def create_superuser(self, username, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		if extra_fields.get('is_staff') is not True:
			raise ValueError('staffがTrueではないです')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('is_superuserがTrueではないです')
		if not email:
			raise ValueError('emailを入力してください')
		if not username:
			raise ValueError('usernameを入力してください')
		email = self.normalize_email(email)
		user = self.model(username=username, email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self.db)
		return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    userId = models.CharField(max_length=255, default=uuid4, primary_key=True, editable=False)
    username = models.CharField('名前', max_length=255, unique=True)
    email = models.EmailField('メールアドレス', unique=True)
    image_url = models.URLField('imageUrl', blank=True, max_length=200)
    date_joined = models.DateTimeField('date_joined', default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return 'id: '+self.userId+'　　　'+self.email