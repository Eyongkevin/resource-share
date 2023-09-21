from django.test import TestCase
from apps.resources.forms import PostResourceForm
from apps.resources.models import Tag


class TestPostResourceForm(TestCase):

    def setUp(self) -> None:
        self.python_tag = Tag.objects.create(name='python')
        self.java_tag = Tag.objects.create(name='java')

    def test_valid_form_success(self):
        data = {
            'title': 'Test title',
            'link': 'https://test-link.com',
            'description': 'test description',
            'tags': [self.python_tag.id, self.java_tag.id]
        }

        form = PostResourceForm(data=data)

        assert form.is_valid()

    def test_form_link_not_valid(self):
        data = {
            'title': 'Test title',
            'description': 'test description',
        }

        form = PostResourceForm(data=data)
        form.is_valid()

        assert len(form.errors) > 0
