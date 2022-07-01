from django.db import models


class Email(models.Model):
    email = models.CharField(max_length=90, verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    ip_address = models.TextField(max_length=100, null=True, verbose_name='Id')


from django.db import models

# Create your models here.
