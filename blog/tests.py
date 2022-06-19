from django.test import TestCase
from django.contrib.auth.models import User
from .models import post
from django.shortcuts import reverse

class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='user1')
        cls.post1 = post.objects.create(
            title='post1',
            text='this is the description post 1',
            status=post.STATUS_CHOICES[0][0],
            outher=user,
        )
        cls.post2 = post.objects.create(
            title='post2',
            text='this is the description post 2',
            status=post.STATUS_CHOICES[1][0],
            outher=user,
        )

    # def setUp(self):

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)


    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)


    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)


    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)


    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)


    def test_post_detailes_on_blog_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)


    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)


    def test_draft_post_not_show_in_post_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)







