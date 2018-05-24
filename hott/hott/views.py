from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'generic/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['message'] = 'Hello World'
        # import pdb; pdb.set_trace()

        return context
