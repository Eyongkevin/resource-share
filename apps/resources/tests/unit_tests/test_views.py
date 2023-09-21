from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from apps.resources import views
from apps.user.models import User
from apps.resources.models import Resources, Tag, Category


class TestResourcesView(TestCase):

    def setUp(self) -> None:
        self.client = Client()

        self.tag = Tag.objects.create(name='test tag')

        self.user = User.objects.create(username='test',
                                        password='password1A#',
                                        first_name='mark',
                                        last_name='koren',
                                        email='test@email.com',
                                        bio='test bio',
                                        title='test title')

        self.category = Category.objects.create(cat='test category')

        self.resource = Resources.objects.create(title='test title',
                                                 description='test description',
                                                 link='https://test.com',
                                                 user_id=self.user,
                                                 cat_id=self.category)

        self.resource.tags.set([self.tag])

        self.resource.save()

    def test_home_page_return_200_status(self):
        response = self.client.get(reverse('home'), HTTP_USER_AGENT='Mozilla/5.0')
        assert response.status_code == 200

    def test_home_page_view_user_count(self):
        expected_user_count = 1
        response = self.client.get(reverse('home'), HTTP_USER_AGENT='Mozilla/5.0')
        assert response.context['active_users_count'] == expected_user_count

    def test_home_page_view_resources_count(self):
        expected_resources_count = 1
        response = self.client.get(reverse('home'), HTTP_USER_AGENT='Mozilla/5.0')
        assert response.context['res_count'] == expected_resources_count

    def test_home_page_view_category_count(self):
        expected_categories_count = 1
        response = self.client.get(reverse('home'), HTTP_USER_AGENT='Mozilla/5.0')
        assert len(response.context['categories_count']) == expected_categories_count

    def test_resource_detail_view_redirect_for_unauthenticated_user(self):
        response = self.client.get(reverse('resources-detail', kwargs={'id': self.resource.id}),
                                   HTTP_USER_AGENT='Mozilla/5.0')
        assert response.status_code == 302

    # def test_resources_detail_status_ok_for_authenticated_user(self):
    #     response = self.client.get(reverse("resources-detail", kwargs={'id': self.resource.id}),
    #                                HTTP_USER_AGENT='Mozilla/5.0')
    #
    #     self.client.login(username=self.user.username, password=self.user.password)
    #     assert response.status_code == 200
