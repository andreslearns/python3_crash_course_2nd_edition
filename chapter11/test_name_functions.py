import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Test for 'name_functions.py"""
    
    def test_first_last_name(self):
        """Do names likes 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual (formatted_name, 'Janis Joplin')
        
    def test_first_last_middle_name(self):
        """Do names like 'andrew ibarrientos soltes' work?"""
        formatted_name = get_formatted_name('andrew', 'soltes','ibarrientos')
        self.assertEqual(formatted_name, 'Andrew Ibarrientos Soltes')
        
if __name__ == '__main__':
    unittest.main()