from django.contrib import admin
from .models.marvel_models import Character, Comic, Series, CharacterInComic, CharacterInSeries
from .models.comment_models import SeriesComment, ComicComment

# Register your models here.
admin.site.register(Character)
admin.site.register(Comic)
admin.site.register(Series)
admin.site.register(CharacterInComic)
admin.site.register(CharacterInSeries)


@admin.register(SeriesComment)
class SeriesCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_comment', 'series', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'email', 'user_comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(ComicComment)
class ComicCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_comment', 'comic', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user__username', 'email', 'user_comment')  # Note the use of user__username to search by username
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)