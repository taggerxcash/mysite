from django.contrib import admin

from .models import Question, Choise

class ChoiceAdmin(admin.StackedInline):
    fieldsets = [
        ("Вариант ответа", {"fields": ["text", "votes"]})
    ]
    model = Choise
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Текст вопроса", {"fields" : ["text"]}),
        ("Дата публикации", {"fields" : ["pub_Date"]}),
    ]
    inlines = [ChoiceAdmin]
    list_filter = ["pub_Date"]
    search_fields = ["text"]

# register(модель, связанная админская панель (панель))
admin.site.register(Question, QuestionAdmin)
