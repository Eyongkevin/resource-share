import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Avg
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from apps.resources.forms import PostResourceForm
from apps.resources.models import Resources, Review
from apps.user.models import User

logger = logging.getLogger("resources.views")


class HomePageView(TemplateView):
    template_name = "resources/home-page.html"

    def get_context_data(self, **kwargs):
        resource_counts = Resources.objects.values('cat_id__cat').annotate(total=Count('cat_id'))
        context = super().get_context_data(**kwargs)
        context['title'] = "Welcome to ResourceShare"
        context['res_count'] = Resources.objects.all().count()
        context['active_users_count'] = User.objects.filter(is_active=True).count()
        context['categories_count'] = resource_counts
        return context


class DetailResourceView(LoginRequiredMixin, View):
    max_viewed_resources = 5

    def get(self, request, id):
        viewed_resources = request.session.get('viewed_resources', [])

        resource = Resources.objects.get(pk=id)
        review = Review.objects.filter(resource_id_id=id)
        average = resource.rating_set.aggregate(Avg('rate'))

        viewed_resource = [id, resource.title]

        if viewed_resource in viewed_resources:
            viewed_resources.remove(viewed_resource)

        viewed_resources.insert(0, viewed_resource)
        viewed_resources = viewed_resources[:DetailResourceView.max_viewed_resources]
        request.session['viewed_resources'] = viewed_resources

        return render(request, "resources/detail-resource.html", {
            "res": resource,
            "tags": resource.tags.all(),
            "review_count": review.count(),
            "average": average['rate__avg'],
        })


class AllResourcesView(LoginRequiredMixin, ListView):
    model = Resources
    template_name = 'resources/all_resource.html'
    context_object_name = 'resources'


def resource_post(request):
    if request.method == "GET":
        form = PostResourceForm()
        return render(request, "resources/resource-post.html", {
            "form": form
        })

    else:
        form = PostResourceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return render(request, 'resources/home-page.html')
        return render(request, 'resources/home-page.html', {
            'form': form
        })
