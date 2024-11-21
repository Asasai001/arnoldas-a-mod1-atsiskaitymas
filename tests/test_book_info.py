import unittest
from unittest.mock import patch, MagicMock
from arnoldas_a_mod1_atsiskaitymas.book_info import book_info

class TestBookInfo(unittest.TestCase):
    @patch('arnoldas_a_mod1_atsiskaitymas.book_info.webdriver.Chrome')
    def test_book_info(self, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver

        mock_element1 = MagicMock()
        mock_element1.find_element.side_effect = [
            MagicMock(text="A Light in the Attic"),
            MagicMock(text="£51.77"),
            #Testuojant rodoma klaida dėl reitingo, book_rating grazina MagicMoc objeką
            #vietoje tikrosios reiksmes
            MagicMock(get_attribute=lambda name: "star-rating Three"),
        ]
        mock_element2 = MagicMock()
        mock_element2.find_element.side_effect = [
            MagicMock(text="Tipping the Velvet"),
            MagicMock(text="£53.74"),
            MagicMock(get_attribute=lambda name: "star-rating One"),
        ]
        mock_element3 = MagicMock()
        mock_element3.find_element.side_effect = [
            MagicMock(text="Soumission"),
            MagicMock(text="£50.10"),
            MagicMock(get_attribute=lambda name: "star-rating One"),
        ]
        mock_element4 = MagicMock()
        mock_element4.find_element.side_effect = [
            MagicMock(text="Sharp Objects"),
            MagicMock(text="£47.82"),
            MagicMock(get_attribute=lambda name: "star-rating Four"),
        ]
        mock_element5 = MagicMock()
        mock_element5.find_element.side_effect = [
            MagicMock(text="Sapiens: A Brief History of Humankind"),
            MagicMock(text="£54.23"),
            MagicMock(get_attribute=lambda name: "star-rating Five"),
        ]

        mock_driver.find_elements.return_value = [mock_element1, mock_element2, mock_element3, mock_element4, mock_element5]


        expected = [
            {"book_title": "A Light in the Attic", "book_price": "£51.77", "book_rating": "Three"},
            {"book_title": "Tipping the Velvet", "book_price": "£53.74", "book_rating": "One"},
            {"book_title": "Soumission", "book_price": "£50.10", "book_rating": "One"},
            {"book_title": "Sharp Objects", "book_price": "£47.82", "book_rating": "Four"},
            {"book_title": "Sapiens: A Brief History of Humankind", "book_price": "£54.23", "book_rating": "Five"},
        ]

        result = book_info()
        self.assertEqual(result, expected)


    @patch('arnoldas_a_mod1_atsiskaitymas.book_info.webdriver.Chrome')
    @patch('arnoldas_a_mod1_atsiskaitymas.book_info.WebDriverWait')
    def test_no_books(self, mock_wait, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver

        mock_wait.return_value.until.return_value = True

        mock_driver.find_elements.return_value = []

        result = book_info()
        self.assertEqual(result, [])

if __name__ == '__main__':
        unittest.main()
