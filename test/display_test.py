import unittest
from unittest.mock import patch, MagicMock
from PyQt5.QtWidgets import QApplication

app = QApplication([])  # Required for PyQt5 testing

class TestMainWindow(unittest.TestCase):

    def setUp(self):
        """Set up the MainWindow for testing."""
        self.window = MainWindow()

    def tearDown(self):
        """Clean up after each test."""
        self.window.close()

    def test_add_link_to_list(self):
        """Test adding a valid link to the list."""
        self.window.link_input.setText("https://www.youtube.com/watch?v=example")
        self.window.add_link_to_list()

        self.assertEqual(self.window.link_list.count(), 1)
        self.assertEqual(self.window.link_list.item(0).text(), "https://www.youtube.com/watch?v=example")

    def test_add_empty_link(self):
        """Test attempting to add an empty link."""
        self.window.link_input.setText("")
        self.window.add_link_to_list()

        self.assertEqual(self.window.link_list.count(), 0)

    @patch('helper.execute_command')
    def test_convert_links(self, mock_execute_command):
        """Test converting links."""
        # Add mock links to the list
        self.window.link_list.addItem("https://www.youtube.com/watch?v=example1")
        self.window.link_list.addItem("https://www.youtube.com/watch?v=example2")

        # Call convert
        self.window.convert()

        # Verify execute_command was called twice with the correct arguments
        mock_execute_command.assert_any_call("youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=example1")
        mock_execute_command.assert_any_call("youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=example2")

        # Verify the list is cleared
        self.assertEqual(self.window.link_list.count(), 0)

    def test_message_display(self):
        """Test that the message label is updated correctly after adding a link."""
        self.window.link_input.setText("https://www.youtube.com/watch?v=example")
        self.window.add_link_to_list()

        # Ensure the input is cleared
        self.assertEqual(self.window.link_input.text(), "")

if __name__ == "__main__":
    unittest.main()
