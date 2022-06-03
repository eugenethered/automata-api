import unittest

from apiautomata.holder.Items import Items


class ItemsCase(unittest.TestCase):

    def test_should_store_string_value_for_name_reference(self):
        items = Items()
        items.add('Automata!', 'name')
        self.assertEqual(items.get('name'), 'Automata!')

    def test_should_store_entity_by_type(self):
        class TestEntity:
            def __init__(self):
                self.value = 'testing'
        test_entity = TestEntity()
        items = Items()
        items.add_entity(test_entity)
        test_entity = items.get_entity(TestEntity)
        self.assertEqual(type(test_entity), TestEntity)
        self.assertEqual(test_entity.value, 'testing')


if __name__ == '__main__':
    unittest.main()
