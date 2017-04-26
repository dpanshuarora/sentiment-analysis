# sentiment-analysis

The program creates a dictionary from the pre-compiled list of words and their scores which were compiled manually.
It then caluclates the sentiment values of the tweets based on the sentiment scores of the words.
The tweets along with their scores are saved to a python list.

AFINN.txt is the list of words and their sentiments which is passed as argv[1]
output.txt is a json database of tweets and is passed as argv[2]
