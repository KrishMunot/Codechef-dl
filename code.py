import os
from bs4 import BeautifulSoup
import urllib2

def main():
	counter = 0
	Labels = []
	solutionUrls = []	
	username = "krishmunot"
  
	newpath = os.getcwd() + "/CodeChefCodes" 
	if not os.path.exists(newpath):
	    os.makedirs(newpath)

	url="http://www.codechef.com/users/" + username
  
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(), "html.parser")

	Links = soup.find('table', {'class' :None }).find_all('a')
  
	for Link in Links:
		solutionUrls.append(Link['href'])

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
        
	for link in solutionUrls:
		link = "http://codechef.com" + link
    
		page = urllib2.urlopen(link)
		soup = BeautifulSoup(page.read(), "html.parser")
		getCode = soup.find('td', {'class' : 'centered', 'width': '75'}).find_all('a')

		FileExtension = soup.find('td', {'class' : 'centered', 'width': '70'}).text

		tempString = getCode[0]['href'].replace("viewsolution", "viewplaintext")
    
		page = urllib2.urlopen(SourceCodeLink)
		soup = BeautifulSoup(page.read(), "html.parser")
		SourceCode = soup.find('pre', {'class' : None }).text
		filename = Labels[counter] + '.' + Extensions[FileExtension]

		with open(os.path.join(newpath, filename), 'wb') as temp_file:
		    temp_file.write(SourceCode)

if __name__ == '__main__':
	main()
