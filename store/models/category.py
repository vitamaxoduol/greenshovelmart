from django.db import models

# Create models
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    @staticmethod
    def get_categories_by_id(ids):
        return Category.objects.filter(id__in=ids)
    
    def __str__(self):
        return f"Category: {self.name}"
    

