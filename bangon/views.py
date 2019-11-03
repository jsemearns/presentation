from django.views.generic import TemplateView
from django.http import Http404
from bangon.models import City, Area, Item, Donation


# Create your views here.
class BangonHomePageView(TemplateView):
    template_name = "bangon_index.html"

    def get_context_data(self, **kwargs):
        context = super(BangonHomePageView, self).get_context_data(**kwargs)
        context["cities"] = City.objects.all().order_by("name")

        return context


class BangonAreaTemplateView(TemplateView):
    template_name = "areas.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BangonAreaTemplateView, self).get_context_data(*args, **kwargs)

        try:
            city = City.objects.get(id=kwargs.get("city"))
            context["areas"] = Area.objects.filter(city=city).order_by("name")
            context["city_name"] = city.name
        except City.DoesNotExist:
            raise Http404

        return context


class BangonAreaDetailTemplateView(TemplateView):
    template_name = "area_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BangonAreaDetailTemplateView, self).get_context_data(
            *args, **kwargs
        )

        try:
            area = Area.objects.get(id=kwargs.get("area"))
            items_needed = Item.objects.filter(area=area).order_by("name")
            donations = Donation.objects.filter(area=area).order_by("date")

            context["area"] = area
            context["items_needed"] = items_needed
            context["donations"] = donations
        except Area.DoesNotExist:
            raise Http404

        return context
