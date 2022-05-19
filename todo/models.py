from django.db import models

class News(models.Model):
    """
    Это модель описывает структуру новости в бвзе данных
    """
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_created=True)
    author = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    def __str__(self):
        return f'id:{self.id} {self.title}'

