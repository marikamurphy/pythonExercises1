
"""
Sort Words
----------

Given a (partial) sentence from a speech, print out
a list of the words in the sentence in alphabetical order.
Also print out just the first two words and the last
two words in the sorted list.

::

    speech = '''Four score and seven years ago our fathers brought forth 
             on this continent a new nation, conceived in Liberty, and 
             dedicated to the proposition that all men are created equal.
             '''


Ignore case and punctuation.

See :ref:`sort-words-solution`.
"""
import re

speech = '''Four score and seven years ago our fathers brought forth 
         on this continent a new nation, conceived in Liberty, and 
         dedicated to the proposition that all men are created equal.
         '''
speech=speech.lower() 
speech=re.sub(r'([,\.]?)','',speech)                
wordList=speech.split()
wordList.sort()

print("Words in alphabetical order:\n"+str(wordList))
print("First two words:\n"+str(wordList[:2]))
print("Last two words:\n"+str(wordList[-2:]))
