from django.contrib import admin
from .models import CaseStudy, BlogPost


# ── Case Study Admin ──────────────────────────────────────────────────────────

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'client', 'location', 'date', 'is_published', 'order')
    list_filter   = ('category', 'is_published')
    search_fields = ('title', 'summary', 'client', 'location')
    list_editable = ('is_published', 'order')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'
    ordering = ('order', '-date')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'category', 'date', 'is_published', 'order')
        }),
        ('Content', {
            'fields': ('summary', 'content')
        }),
        ('Project Details', {
            'fields': ('client', 'location')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# ── Blog Post Admin ───────────────────────────────────────────────────────────

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'author', 'published_at', 'read_time', 'is_published', 'order')
    list_filter   = ('category', 'is_published')
    search_fields = ('title', 'excerpt', 'author')
    list_editable = ('is_published', 'order')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ('order', '-published_at')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'category', 'published_at', 'author', 'read_time', 'is_published', 'order')
        }),
        ('Content', {
            'fields': ('excerpt', 'content')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
