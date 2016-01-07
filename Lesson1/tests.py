from django.test import TestCase
from Lesson1.models import Person

class PersonTest(TestCase):
    def test_save_and_retrieve(self):
        # given
        person = Person.objects.create(first_name='Youngmo', last_name='Yoo')
        
        # when
        actual = Person.objects.get(id=person.id)
          
        # then
        self.assertEqual(person, actual)        
    
    def test_save_and_update(self):
        # given
        person = Person.objects.create(first_name='Youngmo', last_name='Yoo')
        
        # when
        person.first_name = 'Slack'
        person.last_name = 'Beck'
        
        person.save()
        
        # then
        actual = Person.objects.get(id=person.id)  
        self.assertEqual(person.first_name, actual.first_name)
        self.assertEqual(person.last_name, actual.last_name)
    
    def test_save_and_delete(self):
        # given
        person = Person.objects.create(first_name='Youngmo', last_name='Yoo')
        self.assertEqual(Person.objects.count(), 1)
        
        # when 
        person.delete()
        
        # then
        self.assertEqual(Person.objects.count(), 0)
    