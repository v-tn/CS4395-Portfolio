# Portfolio Chapter 12: Web Crawl
# Name:         Vincent Nguyen
# NetID:        VTN180000
# Course:       CS 4395.001
# Description:  This program utilizes web crawl to find other urls from the starting url. Then this program
#               uses web scrape to get the contents of the web page into a file. The program will clean up
#               the file to make it readable to find the most term frequency of the files.

from urllib import request
from bs4 import BeautifulSoup
import requests
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Function to web crawl
def web_crawl():
    file_url = []
    queue_url = []

    # Starting url
    url_start = "https://en.wikipedia.org/wiki/Ice_hockey"

    # Request the url
    request_url = requests.get(url_start)

    # Get text from url
    content = request_url.text
    beauty_soup = BeautifulSoup(content, "html.parser")

    # Write the links to url_ice_hockey_.txt
    with open('url_ice_hockey.txt', 'w', encoding='UTF-8') as file:

        # Find all urls in webpage
        for urls in beauty_soup.find_all('a'):

           # Get hypertext reference from the urls
            urls_string = str(urls.get('href'))

            # Find links that contain 'ice', 'hockey', 'history', or 'ring'
            if 'Ice' in urls_string or 'hockey' in urls_string or 'history' in urls_string or 'ring' in urls_string:

                # Find links that does not contain web.archive, google, or archive.org
                if urls_string.startswith('http') and 'web.archive' not in urls_string and '.pdf' not in urls_string\
                        and 'google' not in urls_string and 'archive.org' not in urls_string:

                    # Append url links to queue
                    file_url.append(urls_string + '\n')
                    queue_url.append(urls_string)

        # For loop to write each url in queue to file
        for url in file_url:
            file.write(url)

        # Close file
        file.close()

    # Return queue of urls
    return queue_url


# Function to web scrape
def scrape(queue_urls):
    num = 0
    num_queue = []

    # For loops to web scrape each url from queue
    for url in queue_urls:
        num += 1

        # If statement to select relatable links to ice hockey
        if (num > 22 and num < 25) or (num > 25 and num < 29) or (num == 32) or (num == 34) or (num == 42) or \
                (num == 46) or (num > 47 and num < 51) or (num == 58) or (num > 62 and num < 64) or (num == 62):

            # Append the link number to queue to use for later
            num_queue.append(num)

            # Open new file to write contents of web page to file
            with open('file' + str(num) + '.txt', 'w') as file:
                try:
                    # Decode contents from url
                    link = url
                    link_website = request.urlopen(link).read().decode('UTF-8')
                    soup_beauty = BeautifulSoup(link_website, "html.parser")

                    for style_script in soup_beauty(["style", "script"]):
                        # Get other contents inside of url and ignore style and script
                        style_script.extract()

                    # Get contents of url through BeautifulSoup
                    contents = soup_beauty.get_text()

                    # Clean up the contents in file
                    text_url = [texts for texts in contents.splitlines() if not re.match(r'^\s*$', texts)]
                    for counter, texts in enumerate(text_url):
                        tokens = sent_tokenize(texts)
                        for content in tokens:
                            # Write contents to file after cleaning up the contents
                            file.write(content + " ")

                    # Print url that we are using to screen
                    print(url + "\n")

                # Catch exception
                except Exception:
                    print(url + " has error\n")

                # Close file
                file.close()

    # Return queue that has number
    return num_queue


# Function to clean up files
def clean_up(nums_queue):
    dict_term_frequency = {}

    # For loop to open file and lower case the files
    for num in nums_queue:
        # Open file and read it
        with open('file' + str(num) + '.txt', 'r') as file:
            for content in file:
                contents = content.lower()

        # Close file
        file.close()

        # Open file to write to file
        with open('file' + str(num) + '.txt', 'w') as file:
            # Writes contents of file in lower case
            file.write(contents)

        # Close file
        file.close()

    # For loop to find term frequency and put it into dictionary
    for num in nums_queue:
        # Open file to read it
        with open('file' + str(num) + '.txt', 'r') as file:
            # Go through contents in the file
            for content in file:
                # Tokenize the contents in file and remove any stopwords
                tokens = word_tokenize(content)
                tokens = [tokens_file for tokens_file in tokens if tokens_file.isalpha() and tokens_file not in
                          stopwords.words('english')]

                # Loop to go through the tokens
                for tokens_file in tokens:
                    # Find recurrence of the tokens and add it to the frequency in dictionary
                    if tokens_file in dict_term_frequency:
                        dict_term_frequency[tokens_file] = dict_term_frequency[tokens_file] + 1
                    else:
                        dict_term_frequency[tokens_file] = 1
        # Close file
        file.close()

    # Print out dict
    print(dict_term_frequency)


# Main function
if __name__ == '__main__':
    queues = []
    queue_num = []

    # Call functions to web crawl, web scrape, and then to clean up the files
    queues = web_crawl()
    queue_num = scrape(queues)
    clean_up(queue_num)



