from django.test import TestCase
from django.urls import reverse
from app.models import Kitten


class KittenListViewTest(TestCase):
    
    def test_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'base_generic.html')
        self.assertTemplateUsed(response, 'app/kitten_list.html')


class KittenDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        kitten = Kitten.objects.create(name='Apfel', age=9, cuteness=99, softness=88)
    
    def test_uses_correct_template(self):
        response = self.client.get(reverse('kitten-detail', args=([1])))
        self.assertTemplateUsed(response, 'base_generic.html')
        self.assertTemplateUsed(response, 'app/kitten_detail.html')
