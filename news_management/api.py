from django.contrib.auth.decorators import permission_required


def article_wrapper(request):
    pass


def get_checked_article(**kwargs):
    pass


@permission_required('news_management.add_checkedarticle')
def post_checked_article(**kwargs):
    pass


@permission_required('')
def delete_checked_article(**kwargs):
    pass

