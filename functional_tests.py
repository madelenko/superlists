from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Open the homepage		
		self.browser.get('http://localhost:8000')

		# Page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')
		

		# Enter to-do item right away

		# New to-do item "Buy peacock feathers"

		# Hit enter, page updates. List "1: Buy peacock feathers" 

		# There is still text box to add new item. Enter
		# "Use peacock feathers to make a fly"

		# The page updates again, and now shows both items.

		# Site remembers list: unique URL generated.

		# Visit URL and find the list.

		# Exit

if __name__ == '__main__':
	unittest.main()








