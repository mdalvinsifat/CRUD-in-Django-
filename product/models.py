from django.db import models
from category.models import Category
# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, related_name="product")
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=25 ,decimal_places=2)
    image = models.ImageField(upload_to='images/', default='images/default_image.jpg')
    video = models.FileField(upload_to='videos/', default='videos/default_video.mp4')
    create_at = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return self.name