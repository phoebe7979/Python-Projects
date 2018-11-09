# -*- coding: utf-8 -*-
## __author__ == "jczetta (Jackie Cohen)"

## SI 506 - PS8
## Submit as usual per instructions.
## Do NOT change the name of this file when you save and submit.
## File must run to be graded.
## Accompanying test file provided.

###########################################
import json
import csv # Do not need to use this, but you may
###########################################

## [PROBLEM 1]
print("\n*** PROBLEM 1 ***\n")

## You should have downloaded a file called nested_data_ps8.json. Use Python file operations and the json.loads function to save the data from that file, in a Python dictionary, to a variable called file_diction.

## Write your code to do so here.

with open("nested_data_ps8.json") as md:
    str = md.read()
    file_diction = json.loads(str)

## [PROBLEM 2]
print("\n*** PROBLEM 2 ***\n")

## This problem occurs in several parts, dealing with nested data.

## We have provided a file called itunes_data.json, which contains data from iTunes that results from a search for the artist Solange.

## HINT: You may want to open up the data and save it all in a variable, in Python format, just once, up here...
## And maybe do some investigation on it! Understand, extract...
with open("itunes_data.json") as md:
    str = md.read()
    object = json.loads(str)

## [PART 1]: Write code to save a list of the song titles inside the data from the JSON file in a variable called song_titles.

song_titles = []
for x in object['results']:
    song_titles.append(x['trackName'])


## [PART 2]: Write code to save the first album title from the data in the JSON file in a variable called first_album.
first_album = object['results'][0]['collectionName']

## [PART 3]: Write code to save a list of the album titles inside the data from the JSON file in a variable called album_titles.

album_titles = []
for x in object['results']:
    album_titles.append(x['collectionName'])


## [PART 4]: Write code to save the dictionary representing the LONGEST song in milliseconds from the data in a variable called longest_song. HINT: Be careful about types... And examine the data!
## For credit on this part, you must write code to figure out which the longest song is, not just read the data and extract the specific dictionary with an index.

length = 0
longest_song = {}

for x in object['results']:
    if x['trackTimeMillis'] > length:
        length = x['trackTimeMillis']
        longest_song = x

## [PART 5]: Write code to generate a list of the strings representing each of the UNIQUE genres among the songs in the data from the JSON file. Save the unique genres into a variable called unique_genres.
# (This is a problem you could solve in a number of different ways. You must write code to determine them, not read the data and type them out.)
## HINT: What data structure do you know where things must be unique? How can you get a list of the unique things?
## Additional hint: using the in / not in operator can be very useful for making a list of things that are unique (only occur in the list once).

unique_genres = []
for x in object['results']:
    if x['primaryGenreName'] not in unique_genres:
        unique_genres.append(x['primaryGenreName'])
print(unique_genres)

## [PROBLEM 3]
print("\n*** PROBLEM 3 ***\n")
## This problem has one goal which you'll need to separate into a few parts to complete.

## We've provided a .json file called samplepost.json.
## The file contains a (edited) representation of a Facebook post from a few years ago. (The way of accessing data from Facebook has changed since the time this data was retrieved! But the data is still structured in a fine way, following JSON rules.)
## This data, in this JSON file, represents a Facebook post with a photo, and a number of likes and comments.

## Your goal is to take this .json file, open it, and use the data in it (specifically, the data about comments on the post) to create a CSV file.
## You'll be taking the data in the .json file and writing it to a .CSV file.
## The CSV file you create should be called post_data.csv.
## Its headers should be:
### CREATED_TIME,COMMENT_TEXT,NAME_OF_POSTER,NUM_LIKES,NUM_WORDS

post = open('samplepost.json', 'r')
postcontent = post.read()
python_obj = json.loads(postcontent)

commentitems = python_obj['comments']['data']
csvfile = open('post_data.csv', 'w')
csvfile.write('CREATED_TIME,COMMENT_TEXT,NAME_OF_POSTER,NUM_LIKES,NUM_WORDS' + '\n')
def cleaningtext(originaltext):
    textstr = "".join(originaltext.split('\n'))
    return textstr
def numwrd(textstr):
    return len(textstr.split())
for item in commentitems:
    commenttext = item['message']
    row = '{},{},{},{},{}'.format(item['created_time'], cleaningtext(commenttext), item['from']['name'], item['like_count'], numwrd(cleaningtext(commenttext))) + '\n'
    csvfile.write(row)
csvfile.close()
post.close()

## The column under CREATED_TIME in each row should contain a representation of the time at which a given comment was posted.
## The column under COMMENT_TEXT in each row should contain the text of the comment. (BE CAREFUL: You'll want to make sure there are no newlines in the text or that you handle new lines properly, so you don't mess up the formatting of the file!)
## The column under NAME_OF_POSTER should contain the name of the user who posted the comment (e.g. "P Resnick").
## The column under NUM_LIKES should contain an integer representing the number of likes htat have been given to the comment on Facebook. (Number of people who clicked "like" on this comment, which is represented in the data.)
## The column under NUM_WORDS should contain an integer representing the number of words (chunks of visible characters separated by spaces) that are in the text of the comment.

## There should be one row in the CSV file per each comment in the post.
## Remember, all the data about the post is inside samplepost.json.
## Ultimately, You just need to get data out of the dictionary of data, and decide how to write that data to a .CSV file!


## [PROBLEM 4] - OPTIONAL CHALLENGE: 100 points extra credit
print("\n*** PROBLEM 4 (OPTIONAL) ***\n")
## Given the CSV file called scores.csv, which we have provided, you should open the file, and use the data to:


# (1) Save the data in a Python dictionary called scores_diction,of the following format:
f1 = open('scores.csv', 'r')
f1lines = f1.readlines()
scores_diction = {}
for lin in f1lines[1:]:
    linlst = lin.strip().split(',')
    scorelst = []
    #for num in linlst[1:]:
    #    scorelst.append(int(num))
    scores_diction[linlst[0]] = linlst[1:]

## The keys should each correspond to one value in the NAME column of the CSV file, and each key's associated value should be a list that contains each of the values in the subsequent columns, in the same row.

# And (2), create a new valid .json file called scores_names.json with the data in that Python dictionary.
f2 = open('scores_names.json', 'w')
scorestr = json.dumps(scores_diction)
f2.write(scorestr)
f2.close()
f1.close()
## For example, one key-value pair in the data should be as follows (from the first line of the CSV file):
## "Student 3457":[78,89,92,81]

## Recap of your goal for this problem : The data from the scores.csv CSV file should be reorganized into a Python dictionary format and saved in scores_diction, and that dictionary should be saved as a .json file you create: scores_names.json
