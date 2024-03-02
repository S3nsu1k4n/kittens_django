from django.test import TestCase
from django.urls import reverse
from app.models import Kitten


class KittenCreateTest(TestCase):
    """Tests the create form"""
    def test_form_submission(self) -> None:
        """test correct creation of a kitten using the form"""
        form_data = {
            'name': 'Pfirsich',
            'age': 5,
            'cuteness': 91,
            'softness': 87,
        }

        response = self.client.post(reverse('kitten-create'), data=form_data)

        # check if redirects to the detail page of the created kitten
        self.assertRedirects(response, reverse('kitten-detail', args=[1]))

        # check if the created kitten is created correctly
        kitten = Kitten.objects.get(id=1)

        self.assertEqual(kitten.name, 'Pfirsich')
        self.assertEqual(kitten.age, 5)
        self.assertEqual(kitten.cuteness, 91)
        self.assertEqual(kitten.softness, 87)

class KittenUpdateTest(TestCase):
    """Tests the update form"""
    @classmethod
    def setUpTestData(cls) -> None:
        Kitten.objects.create(name='Apfel', age=9, cuteness=99, softness=88)
    
    def test_form_submission(self) -> None:
        """test correct update of a kitten using the form"""
        form_data = {
            'name': 'Pfirsich',
            'age': 9,
            'cuteness': 99,
            'softness': 87,
        }

        response = self.client.post(reverse('kitten-update', args=[1]), data=form_data)

        # check if redirects to the detail page of the created kitten
        self.assertRedirects(response, reverse('kitten-detail', args=[1]))

        # check if the created kitten is created correctly
        kitten = Kitten.objects.get(id=1)

        self.assertEqual(kitten.name, 'Pfirsich')
        self.assertEqual(kitten.age, 9)
        self.assertEqual(kitten.cuteness, 99)
        self.assertEqual(kitten.softness, 87)

class KittenDeleteTest(TestCase):
    """Tests the delete form"""
    @classmethod
    def setUpTestData(cls) -> None:
        Kitten.objects.create(name='Apfel', age=9, cuteness=99, softness=88)
    
    def test_form_submission(self) -> None:
        """test correct deletion of a kitten using the form"""
        response = self.client.post(reverse('kitten-delete', args=[1]))

        # check if redirects to the detail page of the created kitten
        self.assertRedirects(response, reverse('index'))

        number_kittens = len(Kitten.objects.all())
        self.assertEqual(number_kittens, 0)
