from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        i=0
        for form in self.forms:            
            cleaned_data = form.cleaned_data
            if cleaned_data.get('is_main'):
                i += 1
            else:
                continue         
            
        if i == 0:
            raise ValidationError('Выберите главную тему')
        elif i > 1:    
            raise ValidationError('Главня тема может быть только одна!')
        
        return super().clean()  # вызываем базовый код переопределяемого метода
    

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    inlines = [ScopeInline]
    
    
    
@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'article', 'is_main']    
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']    


