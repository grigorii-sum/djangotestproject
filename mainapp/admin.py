from django.contrib import admin
from django import forms

from .models import Option, Answer, Question, Test


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_per_page = 10
    search_fields = ('name',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'user_id', 'is_right')
    list_per_page = 10
    search_fields = ('answer', 'user_id')
    list_filter = ('user_id', )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('article', 'type', 'right_answer')
    list_editable = ('type', 'right_answer')
    list_per_page = 10
    search_fields = ('article', )


# class TestForm(forms.ModelForm):
#     class Meta:
#         model = Test
#         fields = "__all__"
#
#     def clean_amount_of_questions(self):
#         print(len(self.cleaned_data["questions"]))
#         if self.amount_of_questions != len(self.questions):
#             raise forms.ValidationError("Количество выбранных Вами вопросов должно совпадать с количеством в поле 'amount_of_questions'")
#         return self.cleaned_data["amount_of_questions"]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount_of_questions', 'is_active')
    ordering = ('-is_active', 'name')
    list_editable = ('is_active', )
    list_per_page = 10
    search_fields = ('name', )
    list_filter = ('users', 'is_active')
