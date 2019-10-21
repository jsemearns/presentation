from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"


class SnakeTemplateView(TemplateView):
    template_name = "canvas.html"


class TetrisTemplateView(TemplateView):
    template_name = "tetris.html"
