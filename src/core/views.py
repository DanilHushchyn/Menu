from django.db.models import Prefetch
from django.http import Http404
from django.views.generic import ListView, DetailView

from src.core.models import Page, Menu, MenuItem


# Create your views here.
class PageDetailView(DetailView):
    """
       Created to display a specific page and its menus
    """
    model = Page
    template_name = 'core/page.html'

    def get_object(self, queryset=None):
        """
        Method gets specific Page instance for rendering
        """
        pg_id = self.kwargs.get('pk')
        try:
            page = (Page.objects
            .prefetch_related(Prefetch(
                'menus',
                queryset=Menu.objects
                .prefetch_related(Prefetch(
                    'items',
                    queryset=MenuItem.objects
                    .select_related('page', 'parent')
                ))
            ))
            ).get(pk=pg_id)
        except Page.DoesNotExist:
            raise Http404(f"Page with id {pg_id}, not found")
        return page


class PagesListView(ListView):
    """
       Created to display all pages
    """
    template_name = 'core/pages.html'
    model = Page
    context_object_name = 'pages'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        """
           Some specific context for pagination
        """
        context = (super(PagesListView, self)
                   .get_context_data(**kwargs))
        context['current_page'] = context.pop('page_obj', None)
        return context
