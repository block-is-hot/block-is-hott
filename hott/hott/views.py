from django.views.generic import TemplateView
from shopper_products.models import Photo


class HomeView(TemplateView):
    template_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['message'] = 'Hello World'
        # import pdb; pdb.set_trace()

        return context
        