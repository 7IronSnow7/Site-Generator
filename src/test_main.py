import unittest
from main import extract_title

class TestMain(unittest.TestCase):
    def test_extract_title(self):
        # Test proper h1 heading
        markdown_text = "# This is a heading"
        heading = extract_title(markdown_text)
        self.assertEqual(heading, "This is a heading")
        
        # Test with extra spaces
        markdown_text = "#     Heading with spaces"
        heading = extract_title(markdown_text)
        self.assertEqual(heading, "Heading with spaces")
        
        # Test exception is raised
        with self.assertRaises(Exception):
            extract_title("No heading here")