from django.db import models
from apps.core.models import CreatedModifiedDateTimeBase
from apps.resources.validators import check_rating_range
from apps.user.models import User


class Tag(CreatedModifiedDateTimeBase):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(CreatedModifiedDateTimeBase):
    cat = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.cat


class Resources(CreatedModifiedDateTimeBase):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500)
    tags = models.ManyToManyField(Tag, through="ResourcesTag")
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    cat_id = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Resources"

    def __str__(self):
        return self.title


class ResourcesTag(CreatedModifiedDateTimeBase):
    modified_at = None
    resources_id = models.ForeignKey(Resources, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.resources_id.title}: {self.tag_id.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                "resources_id",
                "tag_id",
                name="resources_tag_unique",
                violation_error_message="Tag already exist for resources"
            )
        ]


class Review(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    resource_id = models.ForeignKey(Resources, on_delete=models.CASCADE)
    body = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user_id.username} - {self.resource_id.title}"


class Rating(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    resource_id = models.ForeignKey(Resources, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[check_rating_range])

    def __str__(self):
        return f"{self.user_id.username} {self.rate}"
