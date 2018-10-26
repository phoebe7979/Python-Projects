# __author__ = "Jackie Cohen (jczetta@umich.edu)"
## TODO: Add encoding line here to ensure encoding works properly.

## Problem Set 7
## SI 506 - F18
## NOTE: DO NOT change the name of this file when you save and submit it (for grading purposes)! It will not get autograded if you change the name. No kidding.

## Import statements
## NOTE: Do not import additional modules that are not in the instructions
import json

## Each of the instructions for the problems in this problem set can be found in comments. Follow the instructions to edit this file and submit file(s) to the corresponding Canvas assignment, as directed on Canvas.

## Problem instructions are found beneath comments that designate the number, e.g. "[PROBLEM 1]"

#### HOW TO RUN PROBLEM SET TESTS:

## We have also provided a file called SI506F18ps7_tests.py. You should NOT EDIT THIS FILE AT ALL, and do not even need to look at it. If you save that file in the SAME DIRECTORY as this problem set program file, and run at the command line: python SI506F18ps7_tests.py

## Then, you will see all the print statements from this file (so comment them out if you don't want to see them) AND the results of the tests from this problem set. (We will look at this in class, too.)


## As always, passing these tests is necessary for a full score on this problem set, but not _always_ sufficient, as full credit also may depend upon whether or not you have followed the instructions correctly.
## The extent of these comment instructions may be less in future problem set files.
## Make sure you have set your text editor view settings to Soft Wrap to read these easily!

## We DO NOT grade code that does not run. Make sure that when you submit this file, you can successfully run the test file on it, even if that means commenting out some code. Your file MUST run in order to be graded. You should see output from tests when you run the test file. If you do not know how to check if your program runs, that is a first thing to make sure you understand and review.


## [PROBLEM 0]
## Make sure encoding utf-8 is properly set up in this file to ensure you do not encounter encoding problems. See the TODO line at the very top of this file.
## Also ensure -- as you continue working -- that character encoding works properly throughout the file.

## [PROBLEM 1]
print("\n*** PROBLEM 1 ***\n")

## We've provided some code below that creates a pretty complicated Python dictionary and saves it to a variable python_diction.

python_diction = {}
python_diction["items"] = []
python_diction["items"].append({"hello":1,"hi":2})
python_diction["items"].append({"hello":42,"hi":65})
python_diction["numbers"] = [1,2,3,5,7,8]

## Write Python code that uses the json.dumps function and Python file operations to write the data now in the python_diction variable to a file called python_diction_saved.json.
## Make sure to close your file after you write it!
## Follow the recipe in the comments to do so.

# Open a file for writing called python_diction_saved.json
f = open('python_diction_saved.json', 'w')
# Run json.dumps on python_diction and save the result in a variable
jdic = json.dumps(python_diction)
# Write the string saved in that variable you just created to the file you opened above, using the .write method on files
f.write(jdic)
# Close the file you opened
f.close()


## [PROBLEM 2]
print("\n*** PROBLEM 2 ***\n")
## Given the following list of tuples list_tups (each element in the list is 1 tuple), create (write) a CSV file called names_zips_ages.csv (it must be called EXACTLY this to pass the tests!) that has 4 rows:
# - 1 row of headers that looks like this: NAME,ZIP CODE,AGE
# - 3 additional rows wherein each row contains the data from each tuple in the list

list_tups = [("Brock","48103",62),("Wei","48109",19),("Aya","48108",36)]

# Write code to do so here.
f = open('names_zips_ages.csv', 'w')
f.write('NAME,ZIP CODE,AGE'+'\n')
for tup in list_tups:
    row = '{},{},{}'.format(tup[0], tup[1], tup[2]) + '\n'
    f.write(row)
f.close()



## [PROBLEM 3]
print("\n*** PROBLEM 3 ***\n")

## Given the included file sample_text.txt, use file methods and what you know about Python programming to find the most common WORD (group of characters with no spaces) in the file contents, and save that most common word to a variable called common_word.
## IMPORTANT HINT: This is VERY similar to many problems we have done before in this course, and examples you can read about in the textbook, although there is certainlly more than one way to complete it. What examples of code problems may be useful to consider in order to compare to them and solve this problem?

# Write code to do so here.
f = open('sample_text.txt', 'r')
d = {}
wds = f.read()
wdss = wds.split()
for w in wdss:
    if w not in d:
        d[w] = 1
    else:
        d[w] += 1
sd = sorted(d, key = lambda w:d[w], reverse = True)
common_word = sd[0]
f.close()
## [PROBLEM 4]
print("\n*** PROBLEM 4 ***\n")

## Define a function called common_file_word that accepts as input one string that represents a file name, and whose return value is the most common WORD inside that file.
## HINT: You should be able to re-use a lot of the code from Problem 3. You just need to generalize it into a function.

## Consider: what does your code from problem 3 do? Can all of that go inside the function -- yes? no? almost all? What will need to be different between the code inside your new common_file_word function (to be defined here) and the code you wrote in Problem 3?

## HINT: Draw or write out the outline of this problem before embarking on the code.
## HINT #2: After you're finished defining this function, the following code should work:
# print(common_file_word("sample_text.txt")) # Invoking your function on the name of the file that is included with this problem set
## HINT #3: It is possible to make only a few very small changes/additions (including indentation/function definition-related changes) to successful code from Problem 3 in order to completely solve this problem!
def common_file_word(fn):
    f = open(fn, 'r')
    d = {}
    wds = f.read()
    wdss = wds.split()
    for w in wdss:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    sd = sorted(d, key = lambda w:d[w], reverse = True)
    common_word = sd[0]
    f.close()
    return common_word
    ## [PROBLEM 4]
    print("\n*** PROBLEM 4 ***\n")
