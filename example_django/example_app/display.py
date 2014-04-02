import django_tables2 as tables
from django_tables2.utils import A
#from django_tables2_simplefilter import F
import HotDisplay
import models as m
from rest_framework import serializers
import settings
from django.core.urlresolvers import reverse

class Shop(HotDisplay.ModelDisplay):
    model = m.Shop
    index = 1
#     attached_tables = [{'name':'OrderGroup', 'populate':'order_group', 'title':'Order Groups'}]

    class DjangoTable(HotDisplay.Table):
        name = HotDisplay.SelfLinkColumn()
        class Meta(HotDisplay.ModelDisplayMeta):
            pass

    class HotTable(HotDisplay.ModelSerialiser):
        class Meta:
            fields = ('id', 'name', 'description')