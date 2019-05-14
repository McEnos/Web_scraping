from urllib.request import urlopen, urljoin 
import webbrowser
import re 

def download_page(url):
	return urlopen(url).read().decode('utf8')

def extract_images_location(page):
	link_regex = re.compile(re.compile('<img[^>]+src=["\'](.*?)["\']',re.IGNORECASE))
	return link_regex.findall(page)


if __name__ == '__main__':
	target_url = 'http://www.apress.com/'
	apress = download_page(target_url)
	links = extract_images_location(apress)
	for link in links:
		full_url = urljoin(target_url,link)
		# webbrowser.open(full_url)
		print(full_url)