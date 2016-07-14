'''
Created on 13-Jul-2016

@author: zeeshan
'''
from collections import Counter

text = "Tuples are immutable, and usually contain an heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list."

words = text.split()

print(words)

counter = Counter(words)
topThree = counter.most_common(3)
print(topThree)