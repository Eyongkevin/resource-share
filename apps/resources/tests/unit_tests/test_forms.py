from django.test import TestCase
from apps.resources.forms import PostResourceForm


class TestPostResourceForm(TestCase):

    # def setUp(self) -> None:
    #     pass

    def test_valid_form_success(self):
        data = {
            'title': 'Test title',
            'link': 'https://test-link.com',
            'description': 'test description',
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
