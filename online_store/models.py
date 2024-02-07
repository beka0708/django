from django.db import models


class Store(models.Model):
    STORE_TYPE = (
        ('Холодильник', "Холодильник"),
        ("Газовая плита", "Газовая плита"),
        ("Стиральная машина", "Стиральная машина"),
        ("Пылесос", "Пылесос"),
        ("Телевизор", "Телевизор"),
        ("Утюг", "Утюг"),
        ("Фэн", "Фэн"),
        ("Ноутбук", "Ноутбук"),
    )
    title = models.CharField("Название техники", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField(upload_to='')
    store_type = models.CharField(max_length=100, choices=STORE_TYPE)
    created_data = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
    video = models.URLField

    def __str__(self):
        return self.title


class CommentStore(models.Model):
    RATING = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****')
    )
    store_choices_comment = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='comment_object')
    text = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=RATING)
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rate_stars
