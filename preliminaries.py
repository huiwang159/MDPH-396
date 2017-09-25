import numpy
import pandas
import nltk
pandas.set_option('display.max_columns', 50)
fake = pandas.read_csv('fake_data.csv', delimiter=',')
description = fake['incident_description']




'''
Parameters
----------
column: pandas dataframe

Returns
----------
average world count per entry: float
'''
def avg_wc(column):
    return numpy.mean([len(event.split()) for event in column])
# Ex. avg_wc(description)




'''
Parameters
----------
column: pandas dataframe

Returns
----------
Ex. [('ball', 'NN')]: list of tuples
'''
def tag_all(column):
    return nltk.pos_tag([word for sentence in column for word in sentence.split()])

# Ex. tag_all(description)[:10]




'''
Parameters
----------
column: pandas dataframe
tag_list: list of tags

Returns
----------
all words tagged with items in tag_list: list of strings
'''

def get_tag(column, tag_list):
    return [word for (word, tag) in tag_all(column) if tag in tag_list]

# Ex. get_tag(description, ['NN', 'NNS'])[:10]
# Ex. get_tag(description, ['VBS', 'VB'])




'''
Parameters
----------
column: pandas dataframe
tag_list: list of tags

Returns
----------
percentage of column composed of words specified in tag_list: float
'''

def composition(column, tag_list):
    return len(get_tag(column, tag_list))/len([word for sentence in column for word in sentence.split()])

# Ex. composition(description, ['NN', 'NNS'])
# Ex. composition(description, ['VBS', 'VB'])




'''
Parameters
----------
column: pandas dataframe
nm: string

Action
----------
Write a text file (with filename nm) of all the entries in the column in preparation for conversion into a nltk object
Note: the text file must then be place in nltk_data/corpora/gutenberg
'''
def txt(cl, nm):
    f = open(nm,'w') 
    for row in fake['incident_description']:
        f.write(row+' ')
    f.close()
txt(fake['incident_description'], 'f.txt')




'''
Parameters
----------
nm: filename

Action
----------
Converts text file into an nltk object so nltk methods can be used
'''
def nltk_ob(nm):
    return nltk.text.Text(nltk.corpus.gutenberg.words(nm))

# Ex. des = nltk_ob('f.txt')




'''
Parameters
----------
ob: nltk object

Returns
----------
Most common words from ob: list of strings
'''
def freq(ob):
    return nltk.FreqDist(ob).most_common()
