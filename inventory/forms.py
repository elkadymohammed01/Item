from django.forms import ModelForm

from help_tools.form import BootstrapForm
from .models import *


class ItemForm(ModelForm, BootstrapForm):
    class Meta:
        model = Item
        exclude = []


class InventoryTypeForm(ModelForm, BootstrapForm):

    class Meta:
        model = InventoryType
        exclude = []


class InventoryForm(ModelForm, BootstrapForm):

    class Meta:
        model = Inventory
        exclude = []
