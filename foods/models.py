from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(_('name'), max_length=100, help_text=_('This is the help text'))
    # price = models.PositiveIntegerField(_('price'), default=0)
    # category = models.CharField(_('Category'), max_length=30, null=True, blank=True) 
    # meal = models.CharField(_('Meal'), max_length=30, null=True, blank=True) 

    def __str__(self):
        return self.name 
        
    class Meta:
        verbose_name = _('Food Item')
        verbose_name_plural = _('Food Items')
