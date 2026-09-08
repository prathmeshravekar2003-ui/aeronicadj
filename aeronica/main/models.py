from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


# ── Case Study Model ──────────────────────────────────────────────────────────

class CaseStudy(models.Model):

    CATEGORY_CHOICES = [
        ('agriculture',    'Agriculture'),
        ('government',     'Government'),
        ('infrastructure', 'Infrastructure'),
        ('defense',        'Defense'),
        ('mining',         'Mining'),
        ('smart-city',     'Smart City'),
        ('utility',        'Utility'),
        ('locust-control', 'Locust Control'),
    ]

    title        = models.CharField(max_length=255)
    slug         = models.SlugField(unique=True, blank=True, max_length=300)
    category     = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    summary      = models.TextField(help_text="Short description shown on the listing card")
    content      = models.TextField(help_text="Full detail content — supports plain text or HTML")
    client       = models.CharField(max_length=255, blank=True)
    location     = models.CharField(max_length=255, blank=True)
    date         = models.DateField()
    is_published = models.BooleanField(default=True, help_text="Uncheck to hide from website")
    order        = models.PositiveIntegerField(default=0, help_text="Lower number = shown first")

    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-date']
        verbose_name = 'Case Study'
        verbose_name_plural = 'Case Studies'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while CaseStudy.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


# ── Blog Post Model ───────────────────────────────────────────────────────────

class BlogPost(models.Model):

    CATEGORY_CHOICES = [
        ('agriculture',  'Agriculture'),
        ('infrastructure','Infrastructure'),
        ('regulatory',   'Regulatory'),
        ('technology',   'Technology'),
        ('industry',     'Industry News'),
        ('general',      'General'),
    ]

    title        = models.CharField(max_length=255)
    slug         = models.SlugField(unique=True, blank=True, max_length=300)
    category     = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='general')
    excerpt      = models.TextField(help_text="Short preview shown on the blog listing page")
    content      = models.TextField(help_text="Full article content — supports plain text or HTML")
    author       = models.CharField(max_length=255, blank=True, default='Aeronica Team')
    read_time    = models.PositiveIntegerField(default=5, help_text="Estimated read time in minutes")
    is_published = models.BooleanField(default=True, help_text="Uncheck to hide from website")
    order        = models.PositiveIntegerField(default=0, help_text="Lower number = shown first")
    published_at = models.DateField(help_text="Publication date shown on the article")

    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-published_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


# ── Cache Signals ─────────────────────────────────────────────────────────────
# Automatically clears the cache whenever a CaseStudy or BlogPost is
# saved or deleted via the Admin panel.

@receiver(post_save, sender=CaseStudy)
@receiver(post_delete, sender=CaseStudy)
def clear_case_study_cache(sender, **kwargs):
    cache.delete('case_studies_all')
    cache.delete_many([f'case_studies_cat_{c[0]}' for c in CaseStudy.CATEGORY_CHOICES])


@receiver(post_save, sender=BlogPost)
@receiver(post_delete, sender=BlogPost)
def clear_blog_cache(sender, **kwargs):
    cache.delete('blog_posts_all')
    cache.delete_many([f'blog_posts_cat_{c[0]}' for c in BlogPost.CATEGORY_CHOICES])
