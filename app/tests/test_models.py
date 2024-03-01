from django.test import TestCase
from app.models import Kitten


class KittenModelTest(TestCase):
    """Test the kitten model"""

    @classmethod
    def setUpTestData(cls) -> None:
        kitten = Kitten.objects.create(name='Apfel', age=9, cuteness=99, softness=88)


    def get_kitten_field(self, kitten_id: int, field_name: str):
        return Kitten.objects.get(id=kitten_id)._meta.get_field(field_name)
    
    def check_verbose_name(self, field_name: str, verbose_name: str) -> None:
        field_attr = self.get_kitten_field(kitten_id=1, field_name=field_name).verbose_name
        self.assertEqual(field_attr, verbose_name)

    def check_max_length(self, field_name: str, max_length: int) -> None:
        field_attr = self.get_kitten_field(kitten_id=1, field_name=field_name).max_length
        self.assertEqual(field_attr, max_length)

    def check_uniqueness(self, field_name: str, unique: bool) -> None:
        field_attr = self.get_kitten_field(kitten_id=1, field_name=field_name).max_length
        self.assertEqual(field_attr, unique)    

    def check_auto_now_add(self, field_name: str, auto_now_add: bool) -> None:
        field_attr = self.get_kitten_field(kitten_id=1, field_name=field_name).auto_now_add
        self.assertEqual(field_attr, auto_now_add)

    def check_auto_now(self, field_name: str, auto_now: bool) -> None:
        field_attr = self.get_kitten_field(kitten_id=1, field_name=field_name).auto_now
        self.assertEqual(field_attr, auto_now)

    def test_name_label(self):
        self.check_verbose_name('name', 'Name')
    
    def test_name_max_length(self):
        self.check_max_length('name', 32)

    def test_age_label(self):
        self.check_verbose_name('age', 'Age')

    def test_cuteness_label(self):
        self.check_verbose_name('cuteness', 'Cuteness')

    def test_softness_label(self):
        self.check_verbose_name('softness', 'Softness')
    
    def test_created_at(self):
        self.check_auto_now_add('created_at', True)

    def test_updated_at(self):
        self.check_auto_now('updated_at', True)