import datetime
from django.utils import timezone
from django.contrib.auth.models import Permission

from catalog.models import BookInstance, Book, Genre, Language
from django.contrib.auth.models import User

class LoanedBookInstancesByUserListViewTest(TestCase):

    def setUp(self):

        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()


        test_author = Author.objects.create(first_name='John', last_name='Smith')
        test_genre = Genre.objects.create(name='Fantasy')
        test_language = Language.objects.create(name='English')
        test_book = Book.objects.create(title='Book Title', summary = 'My book summary', isbn='ABCDEFG', author=test_author, language=test_language)

        genre_objects_for_book = Genre.objects.all()
        test_book.genre.set(genre_objects_for_book) 
        test_book.save()


        number_of_book_copies = 30
        for book_copy in range(number_of_book_copies):
            return_date= timezone.now() + datetime.timedelta(days=book_copy%5)
            if book_copy % 2:
                the_borrower=test_user1
            else:
                the_borrower=test_user2
            status='m'
            BookInstance.objects.create(book=test_book,imprint='Unlikely Imprint, 2016', due_back=return_date, borrower=the_borrower, status=status)

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('my-borrowed'))
        self.assertRedirects(resp, '/accounts/login/?next=/catalog/mybooks/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('my-borrowed'))


        self.assertEqual(str(resp.context['user']), 'testuser1')

        self.assertEqual(resp.status_code, 200)


        self.assertTemplateUsed(resp, 'catalog/bookinstance_list_borrowed_user.html')

class RenewBookInstancesViewTest(TestCase):

    def setUp(self):

        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()

        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()
        permission = Permission.objects.get(name='Set book as returned')
        test_user2.user_permissions.add(permission)
        test_user2.save()


        test_author = Author.objects.create(first_name='John', last_name='Smith')
        test_genre = Genre.objects.create(name='Fantasy')
        test_language = Language.objects.create(name='English')
        test_book = Book.objects.create(title='Book Title', summary = 'My book summary', isbn='ABCDEFG', author=test_author, language=test_language,)

        genre_objects_for_book = Genre.objects.all()
        test_book.genre=genre_objects_for_book
        test_book.save()


        return_date= datetime.date.today() + datetime.timedelta(days=5)
        self.test_bookinstance1=BookInstance.objects.create(book=test_book,imprint='Unlikely Imprint, 2016', due_back=return_date, borrower=test_user1, status='o')


        return_date= datetime.date.today() + datetime.timedelta(days=5)
        self.test_bookinstance2=BookInstance.objects.create(book=test_book,imprint='Unlikely Imprint, 2016', due_back=return_date, borrower=test_user2, status='o')
