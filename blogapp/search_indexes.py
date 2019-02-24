import datetime
from haystack import indexes
from blogapp.models import Blog


class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/blog_text.txt')
    body = indexes.CharField(model_attr='title')
    title = indexes.CharField(model_attr='body')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()