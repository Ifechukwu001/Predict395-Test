from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model


from .views import post_create, post_detail, post_list, post_update, post_delete
from .forms import PostForm
from .models import Post


User = get_user_model()


class BlogViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")
        self.queryset = Post.objects.all()
        Post.objects.create(
            title="Test title", content="Test content", author=self.user
        )

    def test_post_create_url(self):
        url = reverse("blog:create")
        self.assertEqual(resolve(url).func.__name__, post_create.__name__)

    def test_post_create_template(self):
        response = self.client.get(reverse("blog:create"))
        self.assertTemplateUsed(response, "blog/post_create.html")

    def test_create_post(self):
        response = self.client.post(
            reverse("blog:create"),
            data={
                "title": "Test title",
                "content": "Test content",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.queryset.count(), 2)

    def test_post_detail_url(self):
        url = reverse("blog:detail", args=[1])
        self.assertEqual(resolve(url).func.__name__, post_detail.__name__)

    def test_post_detail_template(self):
        response = self.client.get(reverse("blog:detail", args=[1]))
        self.assertTemplateUsed(response, "blog/post_detail.html")

    def test_post_list_url(self):
        url = reverse("blog:list")
        self.assertEqual(resolve(url).func.__name__, post_list.__name__)

    def test_post_list_template(self):
        response = self.client.get(reverse("blog:list"))
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_post_update_url(self):
        url = reverse("blog:update", args=[1])
        self.assertEqual(resolve(url).func.__name__, post_update.__name__)

    def test_post_update_template(self):
        response = self.client.get(reverse("blog:update", args=[1]))
        self.assertTemplateUsed(response, "blog/post_update.html")

    def test_update_post(self):
        response = self.client.post(
            reverse("blog:update", args=[1]),
            data={
                "title": "Test",
                "content": "Content",
            },
        )
        self.assertEqual(response.status_code, 302)
        post = self.queryset.first()
        self.assertEqual(post.title, "Test")
        self.assertEqual(post.content, "Content")

    def test_post_delete_url(self):
        url = reverse("blog:delete", args=[1])
        self.assertEqual(resolve(url).func.__name__, post_delete.__name__)

    def test_delete_post(self):
        response = self.client.post(reverse("blog:delete", args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.queryset.count(), 0)


class BlogFormTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.queryset = Post.objects.all()

    def test_post_form(self):
        form = PostForm(
            data={
                "title": "Test title",
                "content": "Test content",
            }
        )
        self.assertTrue(form.is_valid())

    def test_post_form_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_post_form_save(self):
        form = PostForm(
            data={
                "title": "Test title",
                "content": "Test content",
            }
        )
        form.instance.author = self.user
        form.save()
        self.assertEqual(self.queryset.count(), 1)
        post = self.queryset.first()
        self.assertEqual(post.title, "Test title")
        self.assertEqual(post.content, "Test content")
        self.assertEqual(post.author, self.user)

    def test_post_form_update(self):
        post = Post.objects.create(
            title="Test title", content="Test content", author=self.user
        )
        form = PostForm(
            data={
                "title": "Test",
                "content": "Content",
            },
            instance=post,
        )
        form.instance.author = self.user
        form.save()
        post.refresh_from_db()
        self.assertEqual(post.title, "Test")
        self.assertEqual(post.content, "Content")
        self.assertEqual(post.author, self.user)


class BlogPostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.queryset = Post.objects.all()
        Post.objects.create(
            title="Test title", content="Test content", author=self.user
        )

    def test_post_str(self):
        post = self.queryset.first()
        self.assertEqual(str(post), "Test title")
