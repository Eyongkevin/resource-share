import logging
from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest, *args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        logging.info(request.path)

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request: HttpRequest, view_func, view_args, view_kwargs) -> None | HttpResponse:
        """
        # Is called just before Django calls the view
        NOTE: Accessing request.POST inside middleware before the view runs or in process_view()
        will prevent any view running after the middleware from being able to modify the upload
        handlers for the request, and should normally be avoided.
        """
        return None

    def process_exception(self, request: HttpRequest, exception: Exception) -> None | HttpResponse:
        """
        Django calls process_exception() when a view raises an exception.
        process_exception() should return either None or an HttpResponse object.
        If it returns an HttpResponse object, the template response and response middleware will be applied and
        the resulting response returned to the browser. Otherwise, default exception handling kicks in.
        """
        return None

    def process_template_response(self, request: HttpRequest, response: TemplateResponse):
        """
        request is an HttpRequest object. response is the TemplateResponse object
        (or equivalent) returned by a Django view or by a middleware.
        process_template_response() is called just after the view has finished executing,
        if the response instance has a render() method, indicating that it is a TemplateResponse or equivalent.
        It must return a response object that implements a render method. It could alter the given response by changing
        response.template_name and response.context_data, or it could create and return a brand-new TemplateResponse
        or equivalent.
        """
        return response
