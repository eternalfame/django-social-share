from django.template import Context, Template
from django.test import TestCase


class TemplateTagsTest(TestCase):
    def setUp(self):
        self.context = Context({
            'url': 'http://example.com',
            'text': 'example'
        })

    def test_twitter(self):
        template = Template("{% load social_share %} {% post_to_twitter url text %}")
        result = template.render(self.context)
        expected = ' <div class="tweet-this">\n    <a href="http://twitter.com/intent/tweet?text=http%3A//example.com%20example.comexample" class="meta-act-link meta-tweet">Post to Twitter</a>\n</div>\n'
        self.assertEqual(result, expected)

    def test_facebook(self):
        template = Template("{% load social_share %} {% post_to_facebook url text %}")
        result = template.render(self.context)
        expected = ' <div class="facebook-this">\n    <a href="http://www.facebook.com/sharer/sharer.php?u=http%3A//example.com" target="_blank">example</a>\n</div>\n'
        self.assertEqual(result, expected)

    def test_gplus(self):
        template = Template("{% load social_share %} {% post_to_gplus url text %}")
        result = template.render(self.context)
        expected = ' <div class="gplus-this">\n    <a href="http://plus.google.com/share?url=http%3A//example.com" target="_blank">example</a>\n</div>\n'
        self.assertEqual(result, expected)
