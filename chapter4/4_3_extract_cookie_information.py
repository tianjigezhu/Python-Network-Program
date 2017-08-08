#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program is optimized for Python 2.7.
# It may run any other version with/without modifications.

import cookielib
import urllib
import urllib2

ID_USERNAME = 'id_username'
ID_PASSWORD = 'id_password'
USERNAME = 'tianjigezhuhn@aliyun.com'
PASSWORD = 'password'
LOGIN_URL = 'https://bitbucket.org/account/signin/?next=/'
NORMAL_URL = 'https://bitbucket.org/'

def extract_cookie_info():
	""" Fake login to a site with cookie """
	# Setup cookie jar
	cj = cookielib.CookieJar()
	login_data = urllib.urlencode({ID_USERNAME : USERNAME,
									ID_PASSWORD : PASSWORD})
	# Create url opener
	opener = urllib2.build_opener(urllib2.HTTPCookieProcesser(cj))
	resp = opener.open(LOGIN_URL, login_data)

	# Send login info
	for cookie in cj:
		print "---First time cookie: %s --> %s" % (cookie.name, cookie.value)

	print "Headers: %s" % resp.headers 

	# now access without any login info
	resp = opener.open(NORMAL_URL)
	for cookie in cj:
		print "++++Second time cookie: %s --> %s" % (cookie.name, cookie.value)

	print "Headers: %s" % resp.headers

if __name__ == '__main__':
	extract_cookie_info()