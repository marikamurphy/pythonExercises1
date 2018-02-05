"""
Filter Words
------------

Print out only words that start with "o", ignoring case::

    lyrics = '''My Bonnie lies over the ocean.
                My Bonnie lies over the sea.
                My Bonnie lies over the ocean.
                Oh bring back my Bonnie to me.
                '''

Bonus points: print out words only once.

See :ref:`filter-words-solution`.
"""
import re
lyrics = '''My Bonnie lies over the ocean.
            My Bonnie lies over the sea.
            My Bonnie lies over the ocean.
            Oh bring back my Bonnie to me.
         '''
lyrics=lyrics.lower()
lyrics=re.sub(r'[\.,]?','',lyrics)
lyricList=lyrics.split()
owords=[]
for word in lyricList:
        if(word[:1]=='o'):
            try:
                x=owords.index(word)
            except:

                owords.append(word)


print("'O'-words\n"+str(owords))
            

