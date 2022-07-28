from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from main.utils import collect_weather_from_db, collect_events_from_db


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = 'authorization'
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Main'
        return context

    def get(self, request, *args, **kwargs):
        guest_name = request.user.name

        weather_for_guest = collect_weather_from_db()
        events_for_guest = collect_events_from_db(request.user.checkout_date)
        context = self.get_context_data(weather=weather_for_guest,
                                        events=events_for_guest,
                                        guest_name=guest_name,
                                        **kwargs)
        return self.render_to_response(context)
