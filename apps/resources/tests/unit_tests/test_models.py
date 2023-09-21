from django.db import DataError
from django.test import TestCase

from apps.resources import models


class TestTagModel(TestCase):

    def setUp(self) -> None:
        self.tag_name = 'Python'
        self.tag = models.Tag(name=self.tag_name)

    def test_create_tag_object_successful(self):
        assert isinstance(self.tag, models.Tag)

    def test_dunder_str(self):
        assert str(self.tag) == self.tag_name


class TestCategoryModel(TestCase):
    def setUp(self) -> None:
        self.category_name = 'Programing Languages'
        self.category = models.Category(cat=self.category_name)

    def test_create_category_object_successful(self):
        assert isinstance(self.category, models.Category)

    def test_dunder_str(self):
        assert str(self.category) == self.category_name

    def test_verbose_plural_name(self):
        assert self.category._meta.verbose_name_plural == 'Categories'

    def test_name_max_length_error(self):
        category_name = "test" * 100
        category = models.Category(cat=category_name)
        with self.assertRaises(DataError):
            category.save()




