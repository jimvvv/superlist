#!/usr/bin/env 

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Jimmy has heard about a cool new online to-do app. He goes
		# to check out its homepage
		self.browser.get('http://localhost:8000')

		# He notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# He is invited to enter a to-do item straight away

		# He types "Buy peacock features" into a text box (Jimmy's hobby
		# is tying fly-fishing Lures)

		# When he hits enter, the page updates, and now the page lists
		# "1: Buy peacock features to make a fly" (Jimmy is very methodical)

		# The page updates again, and now shows both items on her list

		# Jimmy wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for him -- there is some
		# explanatory text to that effect.

		# He visits the URL - his to-do list is still there.

		# Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main()