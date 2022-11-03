from django.db import models
from django.utils import timezone
from django.conf import settings 
# settings.AUTH_USER_MODELからとってきた方が食い違いなどのリスク減らせる

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="ユーザー",on_delete=models.SET_NULL,null=True)
    index = models.IntegerField('index')
    phase = models.IntegerField('phase')
    note = models.CharField(max_length=500)
    created_at = models.DateTimeField('作成日',default=timezone.now)

    def __str__(self):
        return f'{str(self.index)}-{str(self.phase)}  {self.note}'