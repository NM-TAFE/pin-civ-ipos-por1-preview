from utilities import all_items_in_collection_equal
import unittest


class TestAllItemsInCollectionEqual(unittest.TestCase):
    def test_list_with_identical_elements_is_true(self):
        test_list = [1] * 3
        result = all_items_in_collection_equal(test_list)
        self.assertTrue(result)

    def test_empty_list_is_false(self):
        test_list = []
        result = all_items_in_collection_equal(test_list)
        self.assertFalse(result)

    def test_list_with_mixed_elements_is_false(self):
        test_list = [1, 2, 1]
        result = all_items_in_collection_equal(test_list)
        self.assertFalse(result)
