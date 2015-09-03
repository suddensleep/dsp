# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both types that store multiple different ordered values at the same time. Each of these constructions can enumerate elements of any type (including different types in the same list or tuple!), and you can access the specific elements of each by using bracket notation (i.e. `myTuple[i]` or `myList[j]`). 

>> The main difference between lists and tuples is that lists are mutable and tuples are immutable. This means, for example, that you can explicitly change any element of a list (i.e. `myList[j] = 15.6`); trying this with a tuple throws a `TypeError` and a message that tuples do not support item assignment.

>> Only "hashable" types (i.e. types that can be stored in a hashtable) can be used as dictionary keys, and mutable objects are in general not hashable; therefore, tuples can be used as dictionary keys and lists cannot. This fits with my intuition about how dictionaries work: if a different part of the code were able to alter a dictionary key, it would (perhaps unwittingly) change the very mapping that the dictionary represents.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are a type that also store a collection of different values, much like lists and tuples. There are two main differences. The first difference is that sets will only store unique elements so `s = {'a', 'b', 'c', 'c'}` produces the set creates a set that looks like `set(['a', 'c', 'b'])` when printed. The other big difference, also seen above, is that sets are unordered. 
 
>> You would use a list if you wanted to maintain your elements in a specific order and allow for multiple copies of the same value. An example of this would be using a list of strings to store customer complaints in the order in which they arrived.
>> A similar situation in which you might use a set instead would be if the customer complaints were filed through a multiple choice or questionnaire style interface. You might use a set to examine which ones out of ten possible responses were actually given by the customers taking the questionnaire; this way, you could figure out which response options to delete from the survey.

>> `element in mySet` is generally faster than `element in myList`, because sets use hashtables to store the values inside of them and lists use standard numerical indexing.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's `lambda` function is used to create short simple functions that are to be used once and discarded. For example, you might want to quickly figure out whether the integers in a list are even or odd. You could create an `if: ... elif:` statement that checks each element modulo 2, but this would take up a few lines of code.
>> 
>> Instead, you can write the snippet:

```
myList = [3, 4, 7, 2, 9, 190]
myEvens = filter(lambda x: x%2 == 0, myList)
myOdds = filter(lambda x: x%2, myList)
```
>> This provides a quick way to check whether the element is even or odd without writing if statements.
>> 
>> `lambda` can be useful for sorting lists as well. The following code sorts a list of integers in terms of their lowest residues modulo 10:

```
myList = range(100)
mySortedList = sorted(myList, key = lambda x: x%10)
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension is a shorthand for referring to and manipulating elements of a list. The Python documentation states:
>>> "A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses."

>> So, if you are working with a list called `myLowerList` containing any number of lowercase strings, you can easily construct a corresponding list of the same strings in uppercase by typing:

```
myUpperList = [s.upper() for s in myLowerList]
```
>> A corresponding way to do this using `map` is as follows:

```
import string
myUpperList = map(string.upper, myLowerList)
```
>> One drawback of this method is the need to import the string module, rather than just use the built-in method as above. I wonder if there is a way to get around this ...
>> 
>> We can also make more complicated list comprehensions. Say we have a function `hasVowel(s)` that reads in a string argument and returns True if the string contains a vowel. We can now take a list of lowercase strings, and create a new capitalized list of only those strings that have vowels:

```
myNewList = [s.upper() for s in MyLowerList if hasVowel(s)]
```
>> To do this with `map` and `filter`, you might write:

```
import string
myNewList = map(string.upper, filter(hasVowel, myLowerList))
```
>> Reading through the comments on [this](http://stackoverflow.com/questions/1247486/python-list-comprehension-vs-map) Stack Overflow question highlighted an interesting debate in my mind. List comprehensions seem to be more readable "for novice programmers" in that they use the simple language of logic to get their point across. However, `map` and `filter` seem to be easier to type when you have a good sense for what they do (i.e. no reference to "dummy variables"). The quoted speeds seem to be comparable in my mind, although perhaps this changes when examined at larger scales.
>> 
>> Finally, set comprehensions and dictionary comprehensions are also possible:

```
mySet = {x%5 for x in range(100)}
myDict = {x:x%5 for x in range(100)}
```
>> The set above evaluates to `set([0,1,2,3,4])` (in some order) and the dictionary consists of keys for the numbers 0 through 99 along with values equal to their residues modulo 5.

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> The number of days between 01-02-2013 and 07-28-2015 is 937.

b.  

```
date_start = '12312013'  
date_stop = '05282015'  
```

>> The number of days between 12312013 and 05282015 is 513.

c.  

```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> The number of days between 15-Jan-1994 and 14-Jul-2015 is 7850.

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





