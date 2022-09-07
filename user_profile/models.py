from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.







class User(AbstractUser):
    name = models.CharField(max_length=100, unique=True)
    date_joined = models.DateTimeField( auto_now_add=True)
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        
    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse('user_profile:profile')
    # def get_absolute_url(self):
    #     return f'/profile/{self.id}' 








class Quality(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор объявления')

    class Meta:
            verbose_name = "Quality"
            verbose_name_plural = "Qualities"
            
    def __str__(self):
        return str(self.name)




