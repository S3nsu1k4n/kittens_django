from django.test import TestCase
from django.urls import reverse
from app.models import Kitten


class KittenListViewTest(TestCase):
    """Tests the list view"""
    @classmethod
    def setUpTestData(cls) -> None:
        for i in range(20):
            Kitten.objects.create(name=f'Kitten_{i+1}', age=i%10+1, cuteness=i, softness=i)

    def test_uses_correct_template(self):
        """Tests if the correct templates are used"""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'base_generic.html')
        self.assertTemplateUsed(response, 'app/kitten_list.html')

    def test_json_response_data(self) -> None:
        """Tests correct json data"""
        headers = {'HTTP_ACCEPT': 'application/json'}
        response = self.client.get(path=reverse('index'), **headers)
        self.assertEqual(response.status_code, 200)

        expected_json = {'kittens': []}
        for i in range(20):
            expected_json['kittens'].append({
                'name': f'Kitten_{i+1}',
                'age': i%10+1,
                'cuteness': i,
                'softness': i,
            })

        self.assertJSONEqual(str(response.content, encoding='utf-8'), expected_json)

class KittenDetailViewTest(TestCase):
    """Tests the detail view"""
    @classmethod
    def setUpTestData(cls) -> None:
        kitten = Kitten.objects.create(name='Apfel', age=9, cuteness=99, softness=88)
    
    def test_uses_correct_template(self):
        """Tests if the correct templates are used"""
        response = self.client.get(reverse('kitten-detail', args=(1, )))
        self.assertTemplateUsed(response, 'base_generic.html')
        self.assertTemplateUsed(response, 'app/kitten_detail.html')

    def test_json_response_data(self) -> None:
        """Tests correct json data"""
        headers = {'HTTP_ACCEPT': 'application/json'}
        response = self.client.get(path=reverse('kitten-detail', args=(1, )), **headers)
        self.assertEqual(response.status_code, 200)

        expected_json = {
            'name': 'Apfel',
            'age': 9,
            'cuteness': 99,
            'softness': 88,
        }

        self.assertJSONEqual(str(response.content, encoding='utf-8'), expected_json)

