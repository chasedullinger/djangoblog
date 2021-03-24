from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post
from blogging.urls import detail_view


class LatestEntriesFeed(Feed):
    title = "Latest blog entries"
    link = "/sitenews/"
    description = "Updates on changes and additions to my blog!"

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return "/posts/{}".format(item.pk)
