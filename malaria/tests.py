from django.contrib.auth.models import User
from django.test import TestCase
from malaria.models import Post, RevPost
from malaria.services import (create_revpost,
                              delete_post_by_id,
                              get_post_by_id,
                              get_revposts_of_owner)
from webhub.models import Pcuser


class MalariaTests(TestCase):

    def setUp(self):
        """Setup the test database"""

        self.u1 = User.objects.create_superuser(username='admin',
                                                password='password',
                                                email='')

        self.u2 = User.objects.create_superuser(username='admin2',
                                                password='password2',
                                                email='')

        self.u1.save()
        self.u2.save()

        self.o1 = Pcuser(user=self.u1)
        self.o2 = Pcuser(user=self.u2)

        self.o1.save()
        self.o2.save()

        self.p1 = Post(owner=self.o1,
                       title_post="Title 1",
                       description_post="Description 1")

        self.p2 = Post(owner=self.o2,
                       title_post="Title 2",
                       description_post="Description 2")

        self.p3 = Post(owner=self.o1,
                       title_post="Title 3",
                       description_post="Description 3")

        self.p4 = Post(owner=self.o2,
                       title_post="Title 4",
                       description_post="Description 4")

        self.p5 = Post(owner=self.o1,
                       title_post="Title 5",
                       description_post="Description 5")

        self.p1.save()
        self.p2.save()
        self.p3.save()
        self.p4.save()
        self.p5.save()

    def test_create_revpost(self):

        revpost = create_revpost(self.o1,
                                 self.p1,
                                 self.p1.title_post,
                                 self.p1.description_post)

        self.assertIsNotNone(revpost)
        self.assertEqual(RevPost.objects.get(pk=revpost.id), revpost)
        self.assertEqual(revpost.owner_rev, self.o1)
        self.assertEqual(revpost.owner_rev_post, self.p1)
        self.assertEqual(revpost.title_post_rev, self.p1.title_post)
        self.assertEqual(revpost.description_post_rev,
                         self.p1.description_post)

        revpost = create_revpost(self.o1,
                                 self.p2,
                                 self.p2.title_post,
                                 self.p2.description_post)

        self.assertIsNotNone(revpost)
        self.assertEqual(RevPost.objects.get(pk=revpost.id), revpost)
        self.assertEqual(revpost.owner_rev, self.o1)
        self.assertEqual(revpost.owner_rev_post, self.p2)
        self.assertEqual(revpost.title_post_rev, self.p2.title_post)
        self.assertEqual(revpost.description_post_rev,
                         self.p2.description_post)

        revpost = create_revpost(self.o1,
                                 self.p3,
                                 self.p3.title_post,
                                 self.p3.description_post)

        self.assertIsNotNone(revpost)
        self.assertEqual(RevPost.objects.get(pk=revpost.id), revpost)
        self.assertEqual(revpost.owner_rev, self.o1)
        self.assertEqual(revpost.owner_rev_post, self.p3)
        self.assertEqual(revpost.title_post_rev, self.p3.title_post)
        self.assertEqual(revpost.description_post_rev,
                         self.p3.description_post)


        revpost = create_revpost(self.o2,
                                 self.p1,
                                 self.p1.title_post,
                                 self.p1.description_post)

        self.assertIsNotNone(revpost)
        self.assertEqual(RevPost.objects.get(pk=revpost.id), revpost)
        self.assertEqual(revpost.owner_rev, self.o2)
        self.assertEqual(revpost.owner_rev_post, self.p1)
        self.assertEqual(revpost.title_post_rev, self.p1.title_post)
        self.assertEqual(revpost.description_post_rev,
                         self.p1.description_post)

        revpost = create_revpost(self.o2,
                                 self.p4,
                                 self.p4.title_post,
                                 self.p4.description_post)

        self.assertIsNotNone(revpost)
        self.assertEqual(RevPost.objects.get(pk=revpost.id), revpost)
        self.assertEqual(revpost.owner_rev, self.o2)
        self.assertEqual(revpost.owner_rev_post, self.p4)
        self.assertEqual(revpost.title_post_rev, self.p4.title_post)
        self.assertEqual(revpost.description_post_rev,
                         self.p4.description_post)

        revpost = create_revpost(self.o2,
                                 self.p5,
                                 self.p5.title_post,
                                 self.p5.description_post)

        self.assertIsNotNone(revpost)
        self.assertEqual(RevPost.objects.get(pk=revpost.id), revpost)
        self.assertEqual(revpost.owner_rev, self.o2)
        self.assertEqual(revpost.owner_rev_post, self.p5)
        self.assertEqual(revpost.title_post_rev, self.p5.title_post)
        self.assertEqual(revpost.description_post_rev,
                         self.p5.description_post)

        revpost_list = RevPost.objects.filter(owner_rev_id=self.o1.id)
        self.assertIsNotNone(revpost_list)
        self.assertEqual(len(revpost_list), 3)
        self.assertIsNotNone(RevPost.objects.filter(owner_rev=self.o1,
                                                    owner_rev_post=self.p1))
        self.assertIsNotNone(RevPost.objects.filter(owner_rev=self.o1,
                                                    owner_rev_post=self.p2))
        self.assertIsNotNone(RevPost.objects.filter(owner_rev=self.o1,
                                                    owner_rev_post=self.p3))
        self.assertFalse(RevPost.objects.filter(owner_rev=self.o1,
                                                owner_rev_post=self.p4))
        self.assertFalse(RevPost.objects.filter(owner_rev=self.o1,
                                                owner_rev_post=self.p5))

        revpost_list = RevPost.objects.filter(owner_rev_id=self.o2.id)
        self.assertIsNotNone(revpost_list)
        self.assertEqual(len(revpost_list), 3)
        self.assertIsNotNone(RevPost.objects.filter(owner_rev=self.o2,
                                                    owner_rev_post=self.p1))
        self.assertIsNotNone(RevPost.objects.filter(owner_rev=self.o2,
                                                    owner_rev_post=self.p4))
        self.assertIsNotNone(RevPost.objects.filter(owner_rev=self.o2,
                                                    owner_rev_post=self.p5))
        self.assertFalse(RevPost.objects.filter(owner_rev=self.o2,
                                                owner_rev_post=self.p2))
        self.assertFalse(RevPost.objects.filter(owner_rev=self.o2,
                                                owner_rev_post=self.p3))

        revpost = create_revpost(None,
                                 self.p1,
                                 self.p1.title_post,
                                 self.p1.description_post)

        self.assertIsNone(revpost)

        revpost = create_revpost(self.o1,
                                 None,
                                 self.p1.title_post,
                                 self.p1.description_post)

        self.assertIsNone(revpost)

        revpost = create_revpost(self.o1,
                                 self.p1,
                                 None,
                                 self.p1.description_post)

        self.assertIsNone(revpost)

        revpost = create_revpost(self.o1,
                                 self.p1,
                                 self.p1.title_post,
                                 None)

        self.assertIsNone(revpost)

        revpost = create_revpost(None,
                                 self.p1,
                                 self.p1.title_post,
                                 None)

        self.assertIsNone(revpost)

        revpost = create_revpost(self.o1,
                                 None,
                                 self.p1.title_post,
                                 None)

        self.assertIsNone(revpost)

        revpost = create_revpost(self.o1,
                                 None,
                                 None,
                                 None)

        self.assertIsNone(revpost)

        revpost = create_revpost(None,
                                 None,
                                 None,
                                 self.p1.description_post)

        self.assertIsNone(revpost)

        revpost = create_revpost(None,
                                 None,
                                 None,
                                 None)

        self.assertIsNone(revpost)

    def test_delete_post_by_id(self):

        self.assertTrue(delete_post_by_id(self.p1.id))
        self.assertTrue(delete_post_by_id(self.p2.id))
        self.assertTrue(delete_post_by_id(self.p3.id))

        self.assertFalse(delete_post_by_id(-999999))
        self.assertFalse(delete_post_by_id(-1))
        self.assertFalse(delete_post_by_id(100))
        self.assertFalse(delete_post_by_id(200))
        self.assertFalse(delete_post_by_id(300))
        self.assertFalse(delete_post_by_id(400))
        self.assertFalse(delete_post_by_id(500))
        self.assertFalse(delete_post_by_id(600))
        self.assertFalse(delete_post_by_id(999))
        self.assertFalse(delete_post_by_id(999999))

    def test_get_post_by_id(self):

        post = get_post_by_id(self.p1.id)
        self.assertIsNotNone(post)
        self.assertEqual(post, self.p1)
        self.assertEqual(post.id, self.p1.id)
        self.assertEqual(post.owner, self.p1.owner)
        self.assertEqual(post.title_post, self.p1.title_post)
        self.assertEqual(post.description_post, self.p1.description_post)

        post = get_post_by_id(self.p2.id)
        self.assertIsNotNone(post)
        self.assertEqual(post, self.p2)
        self.assertEqual(post.id, self.p2.id)
        self.assertEqual(post.owner, self.p2.owner)
        self.assertEqual(post.title_post, self.p2.title_post)
        self.assertEqual(post.description_post, self.p2.description_post)

        post = get_post_by_id(self.p3.id)
        self.assertIsNotNone(post)
        self.assertEqual(post, self.p3)
        self.assertEqual(post.id, self.p3.id)
        self.assertEqual(post.owner, self.p3.owner)
        self.assertEqual(post.title_post, self.p3.title_post)
        self.assertEqual(post.description_post, self.p3.description_post)

        self.assertIsNone(get_post_by_id(-999999))
        self.assertIsNone(get_post_by_id(-1))
        self.assertIsNone(get_post_by_id(100))
        self.assertIsNone(get_post_by_id(200))
        self.assertIsNone(get_post_by_id(300))
        self.assertIsNone(get_post_by_id(999))
        self.assertIsNone(get_post_by_id(999999))

        self.assertNotEqual(get_post_by_id(-999999), self.p1)
        self.assertNotEqual(get_post_by_id(-1), self.p1)
        self.assertNotEqual(get_post_by_id(100), self.p1)
        self.assertNotEqual(get_post_by_id(200), self.p1)
        self.assertNotEqual(get_post_by_id(300), self.p1)
        self.assertNotEqual(get_post_by_id(999), self.p1)
        self.assertNotEqual(get_post_by_id(999999), self.p1)

        self.assertNotEqual(get_post_by_id(-999999), self.p2)
        self.assertNotEqual(get_post_by_id(-1), self.p2)
        self.assertNotEqual(get_post_by_id(100), self.p2)
        self.assertNotEqual(get_post_by_id(200), self.p2)
        self.assertNotEqual(get_post_by_id(300), self.p2)
        self.assertNotEqual(get_post_by_id(999), self.p2)
        self.assertNotEqual(get_post_by_id(999999), self.p2)

        self.assertNotEqual(get_post_by_id(-999999), self.p3)
        self.assertNotEqual(get_post_by_id(-1), self.p3)
        self.assertNotEqual(get_post_by_id(100), self.p3)
        self.assertNotEqual(get_post_by_id(200), self.p3)
        self.assertNotEqual(get_post_by_id(300), self.p3)
        self.assertNotEqual(get_post_by_id(999), self.p3)
        self.assertNotEqual(get_post_by_id(999999), self.p3)

        self.assertNotEqual(get_post_by_id(self.p1.id), self.p2)
        self.assertNotEqual(get_post_by_id(self.p1.id), self.p3)

        self.assertNotEqual(get_post_by_id(self.p2.id), self.p1)
        self.assertNotEqual(get_post_by_id(self.p2.id), self.p3)

        self.assertNotEqual(get_post_by_id(self.p3.id), self.p1)
        self.assertNotEqual(get_post_by_id(self.p3.id), self.p2)

    def test_get_revposts_of_owner(self):

        revpost_list = get_revposts_of_owner(self.p1.id)
        self.assertEqual(len(revpost_list), 0)

        revpost_1 = create_revpost(self.o1,
                                   self.p1,
                                   "Test title 1",
                                   "Test description 1")
        revpost_list = get_revposts_of_owner(self.p1.id)
        self.assertEqual(len(revpost_list), 1)
        self.assertIn(revpost_1, revpost_list)
        revpost_compare = RevPost.objects.get(pk=revpost_1.id)
        self.assertEqual(revpost_compare.owner_rev, self.o1)
        self.assertEqual(revpost_compare.owner_rev_post, self.p1)
        self.assertEqual(revpost_compare.title_post_rev, "Test title 1")
        self.assertEqual(revpost_compare.description_post_rev,
                         "Test description 1")

        revpost_2 = create_revpost(self.o1,
                                   self.p1,
                                   "Test title 2",
                                   "Test description 2")
        revpost_list = get_revposts_of_owner(self.p1.id)
        self.assertEqual(len(revpost_list), 2)
        self.assertIn(revpost_1, revpost_list)
        self.assertIn(revpost_2, revpost_list)
        revpost_compare = RevPost.objects.get(pk=revpost_2.id)
        self.assertEqual(revpost_compare.owner_rev, self.o1)
        self.assertEqual(revpost_compare.owner_rev_post, self.p1)
        self.assertEqual(revpost_compare.title_post_rev, "Test title 2")
        self.assertEqual(revpost_compare.description_post_rev,
                         "Test description 2")

        revpost_3 = create_revpost(self.o1,
                                   self.p1,
                                   "Test title 3",
                                   "Test description 3")
        revpost_list = get_revposts_of_owner(self.p1.id)
        self.assertEqual(len(revpost_list), 3)
        self.assertIn(revpost_1, revpost_list)
        self.assertIn(revpost_2, revpost_list)
        self.assertIn(revpost_3, revpost_list)
        revpost_compare = RevPost.objects.get(pk=revpost_3.id)
        self.assertEqual(revpost_compare.owner_rev, self.o1)
        self.assertEqual(revpost_compare.owner_rev_post, self.p1)
        self.assertEqual(revpost_compare.title_post_rev, "Test title 3")
        self.assertEqual(revpost_compare.description_post_rev,
                         "Test description 3")

        revpost_list = get_revposts_of_owner(self.p2.id)
        self.assertEqual(len(revpost_list), 0)

        revpost_1 = create_revpost(self.o1,
                                   self.p2,
                                   "Test title 1",
                                   "Test description 1")
        revpost_list = get_revposts_of_owner(self.p2.id)
        self.assertEqual(len(revpost_list), 1)
        self.assertIn(revpost_1, revpost_list)
        revpost_compare = RevPost.objects.get(pk=revpost_1.id)
        self.assertEqual(revpost_compare.owner_rev, self.o1)
        self.assertEqual(revpost_compare.owner_rev_post, self.p2)
        self.assertEqual(revpost_compare.title_post_rev, "Test title 1")
        self.assertEqual(revpost_compare.description_post_rev,
                         "Test description 1")
        revpost_2 = create_revpost(self.o1,
                                   self.p2,
                                   "Test title 2",
                                   "Test description 2")
        revpost_list = get_revposts_of_owner(self.p2.id)
        self.assertEqual(len(revpost_list), 2)
        self.assertIn(revpost_1, revpost_list)
        self.assertIn(revpost_2, revpost_list)
        revpost_compare = RevPost.objects.get(pk=revpost_2.id)
        self.assertEqual(revpost_compare.owner_rev, self.o1)
        self.assertEqual(revpost_compare.owner_rev_post, self.p2)
        self.assertEqual(revpost_compare.title_post_rev, "Test title 2")
        self.assertEqual(revpost_compare.description_post_rev,
                         "Test description 2")

        revpost_3 = create_revpost(self.o1,
                                   self.p2,
                                   "Test title 3",
                                   "Test description 3")
        revpost_list = get_revposts_of_owner(self.p2.id)
        self.assertEqual(len(revpost_list), 3)
        self.assertIn(revpost_1, revpost_list)
        self.assertIn(revpost_2, revpost_list)
        self.assertIn(revpost_3, revpost_list)
        revpost_compare = RevPost.objects.get(pk=revpost_3.id)
        self.assertEqual(revpost_compare.owner_rev, self.o1)
        self.assertEqual(revpost_compare.owner_rev_post, self.p2)
        self.assertEqual(revpost_compare.title_post_rev, "Test title 3")
        self.assertEqual(revpost_compare.description_post_rev,
                         "Test description 3")

        revpost_list = get_revposts_of_owner(self.p4.id)
        self.assertEqual(len(revpost_list), 0)

        revpost_1 = create_revpost(self.o2,
                                   self.p4,
                                   "Test title 1",
                                   "Test description 1")
        revpost_list = get_revposts_of_owner(self.p4.id)
        self.assertEqual(len(revpost_list), 1)
        self.assertIn(revpost_1, revpost_list)
        revpost_compare = RevPost.objects.get(pk=revpost_1.id)
        self.assertEqual(revpost_compare.owner_rev, self.o2)
        self.assertEqual(revpost_compare.owner_rev_post, self.p4)
        self.assertEqual(revpost_compare.title_post_rev, "Test title 1")
        self.assertEqual(revpost_compare.description_post_rev,
                         "Test description 1")

        revpost_2 = create_revpost(self.o2,
                                   self.p4,
                                   "Test title 2",
                                   "Test description 2")
        revpost_list = get_revposts_of_owner(self.p4.id)
        self.assertEqual(len(revpost_list), 2)
        self.assertIn(revpost_1, revpost_list)
        self.assertIn(revpost_2, revpost_list)
        revpost_compare = RevPost.objects.get(pk=revpost_2.id)
        self.assertEqual(revpost_compare.owner_rev, self.o2)
        self.assertEqual(revpost_compare.owner_rev_post, self.p4)
        self.assertEqual(revpost_compare.title_post_rev, "Test title 2")
        self.assertEqual(revpost_compare.description_post_rev,
                         "Test description 2")
        revpost_1 = create_revpost(self.o2,
                                   self.p5,
                                   "Test title 1",
                                   "Test description 1")
        revpost_list = get_revposts_of_owner(self.p5.id)
        self.assertEqual(len(revpost_list), 1)
        self.assertIn(revpost_1, revpost_list)
        revpost_compare = RevPost.objects.get(pk=revpost_1.id)
        self.assertEqual(revpost_compare.owner_rev, self.o2)
        self.assertEqual(revpost_compare.owner_rev_post, self.p5)
        self.assertEqual(revpost_compare.title_post_rev, "Test title 1")
        self.assertEqual(revpost_compare.description_post_rev,
                         "Test description 1")

        revpost_2 = create_revpost(self.o2,
                                   self.p5,
                                   "Test title 2",
                                   "Test description 2")
        revpost_list = get_revposts_of_owner(self.p5.id)
        self.assertEqual(len(revpost_list), 2)
        self.assertIn(revpost_1, revpost_list)
        self.assertIn(revpost_2, revpost_list)
        revpost_compare = RevPost.objects.get(pk=revpost_2.id)
        self.assertEqual(revpost_compare.owner_rev, self.o2)
        self.assertEqual(revpost_compare.owner_rev_post, self.p5)
        self.assertEqual(revpost_compare.title_post_rev, "Test title 2")
        self.assertEqual(revpost_compare.description_post_rev,
                         "Test description 2")

        revpost_list = get_revposts_of_owner(-999999)
        self.assertEqual(len(revpost_list), 0)

        revpost_list = get_revposts_of_owner(-1)
        self.assertEqual(len(revpost_list), 0)

        revpost_list = get_revposts_of_owner(100)
        self.assertEqual(len(revpost_list), 0)

        revpost_list = get_revposts_of_owner(200)
        self.assertEqual(len(revpost_list), 0)

        revpost_list = get_revposts_of_owner(300)
        self.assertEqual(len(revpost_list), 0)

        revpost_list = get_revposts_of_owner(999)
        self.assertEqual(len(revpost_list), 0)

        revpost_list = get_revposts_of_owner(999999)
        self.assertEqual(len(revpost_list), 0)
