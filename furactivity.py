from datetime import date, timedelta
import time
import urllib
from bs4 import BeautifulSoup


def count_submissions():
	""" Counts the number of new submissions at FurAffinity. """

	already_done = []
	start = date.today()

	while True:
		try:
			new_posts = urllib.urlopen('http://furaffinity.net/browse', proxies=None, data=None)
			soup = BeautifulSoup(new_posts.read())

			# get the new submissions
			for link in soup.find_all('img'):
				new_result = link.get('src')

				if new_result not in already_done:
					already_done.append(new_result)
				else:
					pass
		except Exception, e:
			print str(e)

		# check to see if 30 days has passed
		if (date.today() == (start + timedelta(days=30))):
			start += timedelta(days=30)
			record_results(already_done)
			already_done = []
		else:
			pass

		time.sleep(10)

def record_results(already_done):
	""" Records the total number of submissions once every 30 days. """

	f = open('submissionlog.csv', 'a')
	f.write(len(already_done) + ',')
	f.close()

if __name__ == "__main__":
	count_submissions()
