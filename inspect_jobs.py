from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_postings():
	driver = webdriver.Chrome()
	engineering_manager_url = 'https://careers.google.com/jobs#t=sq&q=j&li=20&l=false&jlo=en-US&jc=SOFTWARE_ENGINEERING&j=engineering+manager&jl=United+States&st='
	posting_urls = []
	for i in range(0, 60, 20):
		url = engineering_manager_url + str(i)
		driver.get(url)
		raw_postings = driver.find_elements_by_class_name('GXRRIBB-ub-e') # Todo - this changes day by day
		posting_urls += [raw_posting.get_attribute('href') for raw_posting in raw_postings]

	qualifications = []
	for posting_url in posting_urls:
		driver.get(posting_url)
		q = driver.find_elements_by_class_name('GXRRIBB-V-c'). # todo - this may change day by day
		qualifications.append({'minimum': q[0].text, 'preferred': q[1].text})

	driver.close()

get_postings()