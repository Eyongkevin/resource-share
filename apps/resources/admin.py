from django.contrib import admin
from apps.resources.models import Resources, Tag, Review, Category, Rating, ResourcesTag


class ResourcesAdmin(admin.ModelAdmin):
    list_display = ("username", "title", "description", "all_tags", "link")

    def username(self, obj):
        return obj.user_id.username

    def all_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("username", "resources", "get_body")

    def username(self, obj):
        return f"{obj.user_id.username}"

    def resources(self, obj):
        return f"{obj.resource_id.title}"

    @admin.display(description="body")
    def get_body(self, obj):
        return f"{obj.body if len(obj.body) < 50 else obj.body[:50] + '...'}"


class ResourcesTagAdmin(admin.ModelAdmin):
    list_display = ("resources", "tag")

    def resources(self, obj):
        return f"{obj.resources_id.title}"

    def tag(self, obj):
        return f"{obj.tag_id.name}"


class RatingAdmin(admin.ModelAdmin):
    list_display = ("user", "resources", "rating")

    @admin.display(description="resources title")
    def resources(self, obj):
        return obj.resource_id

    def user(self, obj):
        return f"{obj.user_id.username}"

    def rating(self, obj):
        return obj.rate


admin.site.register(Resources, ResourcesAdmin)
admin.site.register(Tag)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category)
admin.site.register(Rating, RatingAdmin)
admin.site.register(ResourcesTag, ResourcesTagAdmin)
