from selenium import webdriver
from budget.models import project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProjectListPage(StaticLiveServerTestCase):
	def setUp(self):
		self.browser=webdriver.Chrome('functional_tests/chromedriver')

	def tearDown(self):
		self.browser,close()

	def Object_Detection_in_Images_is_displayed_correctly(self):
		self.browser.get(live_server_url)
		alert=self.browser.find_element_by_class_name('write the class name')
		self.assertequals(
			alert.find_element_by_tag_name('h2').text,
			'Object Detection in Images'			
	
	
		)

	def test_run_button(self):
		self.browser.get(live_server_url)
		next_url=self.live_server_url+reverse('//write page here')
		self.browser.find_element_by_tag_name('a').click()
		self.assertEquals(
			self.browser.current_url,
			add_url
		)


