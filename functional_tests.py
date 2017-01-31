from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrueve_it_later(self):
        # url of web app
        self.browser.get('http://localhost:8000')

        # check that web page has the correct title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finished the test!')

        # user invited to enter a to-do item straight away

        # user types "Buy peacock feathers into text box"

        # When user hits enter, the page updates, and now the page
        # lists "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"

        # Site generates a unique URL for this list and has text telling
        # the user that her list is saved

        # User visits the URL and the to-do list is still there.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    