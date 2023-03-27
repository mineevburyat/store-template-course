from django.views.generic.base import TemplateView
from common.mixins import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'catalog/index.html'
    title = "Магазин Store - главная"
