from django.contrib import admin
from app_watchlist.models import StreamPlatform, WatchList, Review

# Register your models here.

# admin.site.register(StreamPlatform)
# admin.site.register(WatchList)
# admin.site.register(Review)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "rating", "watchlist", "updated", "active")
    readonly_fields = ("id", "updated", "created")

    # Optional: Display the watchlist title instead of the default __str__
    # @admin.display(description="Watchlist Title")
    # def watchlist_title(self, obj):
    #     return obj.watchlist.title


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ["id", "platform", "title", "storyline", "active", "created"]
    readonly_fields = ["id", "created"]


@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "about", "website"]
    readonly_fields = ["id"]
