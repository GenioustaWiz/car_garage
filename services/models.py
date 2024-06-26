from django.db import models
from PIL import Image
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    date = models.DateField()
    time = models.TimeField()
    service = models.ForeignKey('ServiceOffered', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class ServiceCategory(models.Model):
    category_name = models.CharField(default='Engine services', max_length=200, null=False)
    cat_description = models.TextField(
        default='CaT- Lorem ipsum dolor sit amet, consectetur adipisicingpra esentium eveniet eum libero assumenda.',
        null=False
    )
    img_icon = models.ImageField(default='service_default.png', upload_to='services_Icons',null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)  # Add a slug field

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        # Automatically generate the slug based on the category_name
        if not self.slug:
            self.slug = slugify(self.category_name)
        super(ServiceCategory, self).save(*args, **kwargs)
        
        img = Image.open(self.img_icon.path)
        if img.height > 100 or img.width > 110:
            output_size = (110, 100)
            img.thumbnail(output_size)
            img.save(self.img_icon.path)
class ServiceOffered(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    service_name = models.CharField(default='Dental Services', max_length=100, null=False)
    description = models.TextField(
        default='Lorem ipsum dolor sit amet, consectetur adipisicingpra esentium eveniet eum libero assumenda.',
        null=False
    )
    def __str__(self):
        return self.service_name

    def save(self, *args, **kwargs):
        super(ServiceOffered, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Perform any necessary cleanup before deleting (if applicable)
        super(ServiceOffered, self).delete(*args, **kwargs)

