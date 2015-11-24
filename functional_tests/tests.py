#!/usr/bin/env 
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Jimmy has heard about a cool new online to-do app. He goes
		# to check out its homepage
		self.browser.get(self.live_server_url)

		# He notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		# He is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-to item'
		)

		# He types "Buy peacock feathers" into a text box (Jimmy's hobby
		# is tying fly-fishing Lures)
		inputbox.send_keys('Buy peacock feathers')

		# When he hits enter, he is taken to a new URL,
		# and now the page lists "1. Buy peacock feathers" as an item in a
		# to-do list table
		inputbox.send_keys(Keys.ENTER)
		jimmy_list_url = self.browser.current_url
		self.assertRegexpMatches(jimmy_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Jimmy is very
		# methodical)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		
		# The page updates again, and now shows both items on her list
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		# Now a new user, Francis, comes along to the site.

		## We use a new browser session to make sure that no information
		## of Jimmy's is coming through from cookies etc #
		self.browser.quit()
		self.browser = webdriver.Chrome()

		# Francis visits the home page. There is no sign of Jimmy's 
		# list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		# Francis starts a new list by entering a new item. He
		# is less interesting than Jimmy...
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		# Francis gets his own unique URL
		francis_list_url = self.browser.current_url
		self.assertRegexpMatches(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, jimmy_list_url)

		# Again, there is no trace of Jimmy's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)

		# Satisfied, they both go back to sleep


		# Jimmy wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for him -- there is some
		# explanatory text to that effect.
		self.fail('Finish the test!')
		# He visits the URL - his to-do list is still there.

		# Satisfied, she goes back to sleep
