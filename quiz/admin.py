from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'imagem')


admin.site.register(Category, CategoryAdmin)


class RespostaInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'level', 'question_type')
    list_filter = ('level', 'question_type', 'category', 'country')
    inlines = [RespostaInline, ]


admin.site.register(Question, QuestionAdmin)


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'question', 'answer', 'correta')
    list_filter = ('usuario', 'correta')


admin.site.register(UserAnswer, UserAnswerAdmin)
