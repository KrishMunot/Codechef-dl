import os
from bs4 import BeautifulSoup
import urllib2

def main():
	counter = 0
	Labels = []
	solutionUrls = []
# Enter your username below within quotes	
	username = "krishmunot"

# Creating new directory for saving code files
	newpath = os.getcwd() + "/codechef" 
	if not os.path.exists(newpath):
	    os.makedirs(newpath)
	url="http://www.codechef.com/users/" + username

# Opening page && parsing html content. 
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(), "html.parser")

# getting all links of the code submission 
	Links = soup.find('table', {'class' :None }).find_all('a')

# removing first two links as they are irrelevant
# such as personal and team links
	Links = Links[2:]

# Labels(names) of every question you solved
	for Link in Links:
		Labels.append(Link.text)

# All urls of questions you solved
	for Link in Links:
		solutionUrls.append(Link['href'])

# Language Extension Dictionary
# you can add more language extension if you need
	Extensions = {	'C' : 'c',
			'C++ 4.3.2' : 'cpp',
			'PYTH' : 'py',
			'C++ 4.9.2' : 'cpp',
			'PYTH 3.4' : 'py',
			'JAVA' : 'java',
			"C++ 4.8.1", "cpp",
			"C++14", "cpp",
			"C++11", "cpp",
			"C99 strict", "c",
			"C#", "cs",
			"F#", "fs",
			"PYTH 3.1.2", "py",
			"ASM", "asm",
			"PHP", "php",
			"TEXT", "txt",
			"PERL", "pl",
			"JS", "js"
			}

# Navigating to Every url of the solution & get the solution code
	for link in solutionUrls:
	# generating link  of every code submissions
		link = "http://codechef.com" + link

	# get page content to get unique code of every submission
		page = urllib2.urlopen(link)
		soup = BeautifulSoup(page.read(), "html.parser")

	# getting code from this html page
		getCode = soup.find('td', {'class' : 'centered', 'width': '75'}).find_all('a')

	# we need this while saving file
		FileExtension = soup.find('td', {'class' : 'centered', 'width': '70'}).text

	# Genrating link for the raw code
		tempString = getCode[0]['href'].replace("viewsolution", "viewplaintext")

	# modifying link for to get raw code easily
		SourceCodeLink = "http://codechef.com" + tempString

	# Opening page and getting html content
		page = urllib2.urlopen(SourceCodeLink)
		soup = BeautifulSoup(page.read(), "html.parser")

	# saving raw code in 'SourceCode' variable.
		SourceCode = soup.find('pre', {'class' : None }).text

	# Getting subbmission code name for saved labels && extension from dictionary
		filename = Labels[counter] + '.' + Extensions[FileExtension]

	# Opening that file and saving code in it.
		with open(os.path.join(newpath, filename), 'wb') as temp_file:
		    temp_file.write(SourceCode)
		
	# Yeah, counter is for the labels list.
		counter += 1
		
if __name__ == '__main__':
	main()
