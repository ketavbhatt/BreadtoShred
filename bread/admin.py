# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Food,Exercise,user_calorie


admin.site.register(Food)
admin.site.register(Exercise)
admin.site.register(user_calorie)




# Register your models here.
