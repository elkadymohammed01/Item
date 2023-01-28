from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import *
from django.views.generic import *

from inventory.forms import *
from .models import *

class BaseMaxIn(ContextMixin):

    def get_user(self):
        return self.request.user

    def get_request(self):
        try:
            return self.request.GET['query']
        except:
            return None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BaseMaxIn, self).get_context_data()
        context['user'] = self.get_user()
        return context

    def filter_by_name(self, objects):
        return objects.filter(name__icontains=self.get_request())

class ItemView(CreateView, BaseMaxIn):
    template_name = 'items.html'
    form_class = ItemForm
    success_url = "/inventory/succ/"
    model = Item

    def get_queryset(self):
        if self.get_request():
            return Item.objects.filter(Q(name__icontains=self.get_request())|Q(description__icontains=self.get_request())|Q(inventory__name__icontains=self.get_request()))
        return Item.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data()
        context["item"] = self.get_queryset()
        context["form"] = ItemForm()
        return context

class InventoryView(CreateView, BaseMaxIn):
    template_name = 'inventory.html'
    form_class = InventoryForm
    success_url = "/inventory/succ/"
    model = Inventory

    def get_queryset(self):
        if self.get_request():
            return Inventory.objects.filter(name__icontains=self.get_request())
        return Inventory.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InventoryView, self).get_context_data()
        context["inventory"] = self.get_queryset()
        context["form"] = InventoryForm()
        return context

class InventoryTypeView(CreateView, BaseMaxIn):
    template_name = 'inventory_type.html'
    form_class = InventoryTypeForm
    success_url = "/inventory/succ/"
    model = InventoryType

    def get_queryset(self):
        if self.get_request():
            return Inventory.objects.filter(name__icontains=self.get_request())
        return InventoryType.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InventoryTypeView, self).get_context_data()
        context["inventory_type"] = self.get_queryset()
        context["form"] = InventoryTypeForm()
        return context

class UpdateItem(UpdateView, DetailView):
    model = Item
    form_class = ItemForm
    template_name = 'update_item.html'
    success_url = "/inventory/succ/"

class SuccPage(TemplateView):
    template_name = 'succ_page.html'