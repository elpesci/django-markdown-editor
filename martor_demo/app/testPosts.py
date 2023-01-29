# app/testPosts.py

from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="My Title", description="My description", wiki="Test post body")
        self.assertEqual(post.title, "My Title")
        self.assertEqual(post.description, "My description")
        self.assertEqual(post.wiki, "Test post body")
