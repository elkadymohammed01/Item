from django.db import models

class MainModel(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="الإسم")
    def __str__(self):
        return self.name
    class Meta :
        abstract = True


class InventoryType(MainModel):

    class Meta:
        verbose_name = "نوع المخزن"
        verbose_name_plural = "نوع المخازن"


class Inventory(MainModel):
    type = models.ForeignKey(InventoryType, models.CASCADE, related_name= "inventory", db_index=True, verbose_name="النوع")
    class Meta:
        verbose_name = "المخزن"
        verbose_name_plural = "المخازن"


class Item(MainModel):
    description = models.TextField(db_index=True, verbose_name="الوصف")
    quantity = models.IntegerField(db_index=True, verbose_name="الكمية")
    price = models.FloatField(db_index=True, verbose_name="السعر")
    inventory = models.ForeignKey(Inventory, models.CASCADE, related_name="items", db_index=True, verbose_name="المخزن")
    class Meta:
        verbose_name = "المنتج"
        verbose_name_plural = "المنتجات"
