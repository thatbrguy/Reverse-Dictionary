from bs4 import BeautifulSoup
import urllib
import time

INPUT_FILE_NAME = 'dictwords.txt'
OUTPUT_FILE_NAME = 'dataset.txt'

with open(INPUT_FILE_NAME, 'r') as file:

    file2 = open(OUTPUT_FILE_NAME, 'a')
    for i, word in enumerate(file, 1):
        
        begin = time.time()
        word = word.strip('\n')
        page = urllib.request.urlopen('https://en.oxforddictionaries.com/definition/' + word)
        soup = BeautifulSoup(page, "html5lib")
        print('Words Completed: %d Time/Word: %.3fs' % (i, time.time() - begin), end='\r')
        try:
            definition = soup.find("span", {"class":"ind"}).string
        except:
            print('------No definition for word: %s-----' % word)
            # If you want to save definition as NA for undefined words,
            # uncomment the below statement, and comment continue.
            
            #definition = 'NA'
            continue
            
        line = word + '\t' + definition + '\n'
        file2.write(line)

file2.close()
print('\nDone')