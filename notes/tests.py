from django.test import Client, TestCase
from django.urls import reverse

from notes.forms import AddPostForm, UpdateForm
from notes.models import Note, Category


class AddPageTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.add_page_url = reverse('add_page')
        self.category = Category.objects.create(title='TestCategory')
        self.data = {
            'title': 'TestTitle',
            'text': 'TestText',
            'reminder': '2023-03-01 13:00:00',
            'category': self.category.id
        }

    def test_add_page_url_resolves(self):
        """
        Test that the add_page URL resolves correctly.
        """
        response = self.client.get(self.add_page_url)
        self.assertEqual(response.status_code, 200)

    def test_add_page_view_uses_correct_template(self):
        """
        Test that the add_page view uses the correct template.
        """
        response = self.client.get(self.add_page_url)
        self.assertTemplateUsed(response, 'notes/addpage.html')

    def test_add_page_view_contains_form(self):
        """
        Test that the add_page view contains a form instance.
        """
        response = self.client.get(self.add_page_url)
        form = response.context.get('form')
        self.assertIsInstance(form, AddPostForm)

    def test_add_page_can_create_note_with_valid_data(self):
        """
        Test that a note can be created with valid data using the add_page view.
        """
        response = self.client.post(self.add_page_url, data=self.data)
        note = Note.objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(note.title, self.data['title'])
        self.assertEqual(note.text, self.data['text'])
        self.assertEqual(note.category, self.category)

    def test_add_page_cannot_create_note_with_invalid_data(self):
        """
        Test that a note cannot be created with invalid data using the add_page view.
        """
        self.data['title'] = 'a' * 201
        response = self.client.post(self.add_page_url, data=self.data)
        form = response.context.get('form')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(form.errors)
        self.assertContains(response, 'Переконайтеся, що це значення містить не більше ніж 150 символів (зараз 201).')


class EditNoteTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(title='Test Category')
        self.note = Note.objects.create(title='Test Note', text='Test Text',
                                        reminder='2023-03-01 14:00:00', category=self.category)
        self.url = reverse('edit', kwargs={'post_id': self.note.pk})

    def test_edit_note_view_success_status_code(self):
        """
        Test that the edit note view returns a success status code.
        """
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_edit_note_view_form_instance(self):
        """
        Test that the edit note view contains a form instance with the correct note object.
        """
        response = self.client.get(self.url)
        form = response.context.get('form')
        self.assertIsInstance(form, UpdateForm)
        self.assertEqual(form.instance, self.note)

    def test_edit_note_view_post_success(self):
        """
        Test that submitting a valid form to the edit note view updates the note object
        """
        data = {'title': 'Test Note Updated', 'text': 'Test Text Updated',
                'reminder': '2023-03-01 12:01:00', 'category': self.category.pk}
        response = self.client.post(self.url, data)
        self.note.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.note.title, 'Test Note Updated')
        self.assertEqual(self.note.text, 'Test Text Updated')
        self.assertEqual(self.note.category.pk, self.category.pk)

    def test_edit_note_view_post_invalid(self):
        """
        Test that submitting an invalid form to the edit note view does not update the note object
        """
        data = {'title': 'Test Note Updated 2', 'text': '',
                'reminder': '2023-03-01 12:02:00', 'category': self.category.pk}
        response = self.client.post(self.url, data)
        self.note.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.note.title == 'Test Note Updated')
        self.assertFalse(self.note.category.pk != self.category.pk)

    def test_edit_note_view_post_empty_fields(self):
        """
        Test that submitting a form with empty required fields to the edit note view does not update the note object
        """
        data = {'title': '', 'text': '',
                'reminder': '2023-03-01 12:00:00', 'category': self.category.pk}
        response = self.client.post(self.url, data)
        self.note.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.note.title == '')
