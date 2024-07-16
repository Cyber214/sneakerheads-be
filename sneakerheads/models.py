from django.db import models
# from django.contrib.auth.models import User

class Sneaker(models.Model):
  brand = models.CharField(max_length=200)
  model = models.CharField(max_length=100)
  size = models.DecimalField(max_digits=4, decimal_places=1, default=9.5)
  colorway = models.CharField(max_length=100, default="white")
  posted_at = models.DateTimeField(auto_now_add=True)
  # user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.brand}"