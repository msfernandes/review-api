from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Review(models.Model):
    rating = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=10000)
    ip = models.GenericIPAddressField(protocol='both')
    submission_date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey('core.Company',
                                related_name='reviews',
                                on_delete=models.CASCADE)
    reviewer = models.ForeignKey('auth.User',
                                 related_name='reviews',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
