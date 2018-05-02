
[Carlos Beas](https://github.com/cgbeas)

Software Developer

DXC.technology

carlos.beas@hpe.com

---------------------------------------------------------------------------------------------------------------------


# Introduction to Python

### Instructions:

* If you haven't done so already, install Python:
    - Available [here](https://www.python.org/downloads/)

    - Alternatively, I recommend dowloading Python along with the [Anaconda](https://www.anaconda.com/download) distribution
    
        > * [Anaconda](https://www.anaconda.com/download) is a free and open source Python distribution for large-scale data processing.

        > * It provides a number of premium data mining and analysis features.

        > * Helpful in simplifying [package management, version control](https://conda.io/docs/) and deployment.

Once you have python installed, perform the following steps to follow along with the examples:

* Go to Start -> Anaconda3 -> Jupyter Notebook
* Find supporting material [here]()


## What is Python?

* [Python](https://www.python.org/) is an interpreted high-level programming language for general-purpose programming.

* Features a dynamic type system and automatic memory management. 
    > It supports multiple programming paradigms, including object-oriented, imperative, functional/procedural, and has a large and comprehensive standard library.

* Interpreters are available for many operating systems, including:  UNIX, Linux, Windows, OSX

* Its design philosophy emphasizes code readability

* Provides a great interactive environment (i.e command line, this notebook!)


### Under The Hood:

* [CPython](https://en.wikipedia.org/wiki/CPython) is the reference implementation of the Python programming language. 
    > Written in C, CPython is the default and most widely used implementation of the language.
  
    > CPython compiles your Python code into bytecode and interprets that bytecode in a evaluation loop.

    > CPython is one of several "production-quality" Python implementations including: 
        >> * Jython, written in Java for the Java virtual machine (JVM)

        >> * PyPy, written in RPython and translated into C

        >> * IronPython, which is written in C# for the Common Language Infrastructure.

### Cython
* There is a separate project that does translate Python code to C, and that is called [Cython](http://cython.readthedocs.io/en/latest/index.html). 
* Cython adds a few extensions to the Python language, and lets you compile your code to C extensions, code that plugs into the CPython interpreter.

        


# Let's Start Coding!

### How to run interactive commands?

* Once you've openned and signed in to your UNIX/Linux environment:
* Run the following commands:
        $ python
        Python 2.6.4 (r264:75706, Mar 20 2017, 18:30:48) [C] on sunos5
        Type "help", "copyright", "credits" or "license" for more information.


        >>>print('Hello World')
        Hello World
        
        >>> 2 + 2
        4
        >>> a = 3
        >>> b = 5
        >>> c = a + b
        >>> print(c)
        8
        >>> 2 ** 8
        256


The same can be done inside this notebook!


```python
print('Hello World')
```

    Hello World
    

## Arithmetic Operations


```python
a = 3
b = 5

#Since it is interpreted language, Python is flexible about variable type casting
a = 3.1416
b = 'True'
print(a)
print(b)
```

    3.1416
    True
    


```python
b = 6
print("a is {} and b is {}".format(a,b))
print('Addition: ', a + b)
print('Subtraction: ', a - b)
print('Multiplication: ', a * b)
print('Division: ', a / b)
print('Power: ', a ** b)
```

    a is 3.1416 and b is 6
    Addition:  9.1416
    Subtraction:  -2.8584
    Multiplication:  18.8496
    Division:  0.5236
    Power:  961.4026825309764
    


```python
print('Division: ', a // b)
```

    Division:  0.0
    

### Bit-wise Operations


```python
a = 5
b = 3
#binary: 0101
print('Shift Right: ', a >> 1)  #0010  --> 2
print('SHift Left: ', a << 1)  #1010  --> 10
print('bit-wise OR: ', a | b)  #0101 | 0011  -->     0111 --> 7
print('bit-wise AND: ', a & b)  #0101 & 0011  -->    0001 --> 1
print('bit-wise XOR ', a ^ b)  #0101 ^ 0011  -->     0110 --> 6
```

    Shift Right:  2
    SHift Left:  10
    bit-wise OR:  7
    bit-wise AND:  1
    bit-wise XOR  6
    

### String operations


```python
my_string = 'I Like '
```

Strings are treated as arrays and can be indexed as follows:


```python
print(my_string[0])  # I
print(my_string[5]) # e
print(my_string[0:4]) #I Li
print(my_string[4:])
```

    I
    e
    I Li
    ke 
    

We can easily concatenate two strings using the '+' operator:


```python
my_new_string = my_string + 'coffee'
print(my_new_string)
```

    I Like coffee
    

We can also split a string easily with the 'split()' function:


```python
my_new_string.split()
```




    ['I', 'Like', 'coffee']




```python
this_string = "something,that,is,separated,by commas"
this_string.split(',')
```




    ['something', 'that', 'is', 'separated', 'by commas']



## Functions

In order to declare a function in Python:

    1.- You must use the special keyword 'def' before the name of your function
    2.- No need to specify return type since Python will interpret this at run time
    3.- Define the name of the variable your function will accept inside parenthesis that follow the function's name
    4.- A colon after closing the parenthesis where you define input argument indicates to python that what follows is the code that will be executed by your function
    5.- Remember to use indentation to indicate the lines of code that belong to your function!
    6.- Use the 'return' keyword to return any values/structures to the calling function.
    
Let's look at a simple, yet practical example:


```python
def removeIllegalCharacters(s):
    s = s.replace('\\','')
    s = s.replace('@','')
    return s
    
```


```python
NUM_PAT_ACCT = ['078356\\', 'HIL@LF\\', '36262\\', '\\275755', 'och\\']
CLEAN_NUM_PAT_ACCT = []

for val in NUM_PAT_ACCT:
    CLEAN_NUM_PAT_ACCT.append(removeIllegalCharacters(val))
    
CLEAN_NUM_PAT_ACCT
```




    ['078356', 'HILLF', '36262', '275755', 'och']




```python
def addPadding(v):
    s = str(v)
    s = s.replace('.','')
    for i in range(0,10-len(s)):
        s = '0' +  s
    return s
    
```


```python
values = [472270.16,
372165.1,
44071.66,
198.7,
311879.52,
11802.78,
382259.06,
286803.58,
38547.8,
158.96,
272338.22,
10133.7,
506088.9,
359567.52,
39501.56,
198.7,
342240.88,
14505.1,
1060263.2]

for val in values:
    print(addPadding(val))
```

    0047227016
    0003721651
    0004407166
    0000001987
    0031187952
    0001180278
    0038225906
    0028680358
    0000385478
    0000015896
    0027233822
    0000101337
    0005060889
    0035956752
    0003950156
    0000001987
    0034224088
    0000145051
    0010602632
    

## File I/O

Syntax:

> file_object  = open(“filename”, “mode”)

The modes are: 

> ‘r’ – Read mode which is used when the file is only being read 

> ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be   erased when this mode is activated) 

> ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end 

> ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file 

Here is an example of how to read a text file into a data structure:

The data structure we will be using is a 'Dictionary', which consist of a collection of tuples (key:value pairs):

{'key':value}

> Here, 'key' will usually be integer or string. Whatever type of key is chosen, there will only be one key:value pair for a particular key (in other words, there cannot be more than one key with the same value).
> Value can be any type of data:
    * Integer
    * String
    * Floating point number
    * Arrays
    * Array of arrays
    * Dictionary of dictionaries
    * etc...


```python
my_bag_of_words = {}
my_text_file = open('./alice.txt', 'r')
for line in my_text_file:
    words = line.split(' ')
    for word in words:
        if( word not in my_bag_of_words.keys()):
            my_bag_of_words[word] = 1
        else:
            my_bag_of_words[word] += 1
            
my_bag_of_words
```




    {'\n': 4,
     '"Oh': 1,
     '"and': 1,
     '"without': 1,
     '(as': 1,
     'Alice': 3,
     'Alice\n': 1,
     'Alice,': 1,
     'But': 1,
     'DOWN': 1,
     'I': 1,
     'In': 1,
     'Oh\n': 1,
     'Once': 1,
     'RABBIT-HOLE\n': 1,
     'Rabbit': 3,
     'So': 1,
     'THE': 1,
     'There': 1,
     'White': 1,
     'a': 8,
     'across': 2,
     'actually': 1,
     'after': 1,
     'after\n': 1,
     'and': 5,
     'and\n': 1,
     'and,': 1,
     'another': 1,
     'as': 1,
     'at': 1,
     'bank,': 1,
     'be': 2,
     'before': 1,
     'beginning': 1,
     'book': 1,
     'book,"': 1,
     'burning': 1,
     'but': 1,
     'by': 2,
     'close': 1,
     'considering': 1,
     'conversations': 1,
     'conversations?"\n': 1,
     'could,': 1,
     'curiosity,': 1,
     'daisies,': 1,
     'daisy-chain': 1,
     'day': 1,
     'dear!': 2,
     'did': 1,
     'do.': 1,
     'down': 2,
     'either': 1,
     'eyes': 1,
     'feel': 1,
     'feet,': 1,
     'field': 1,
     'flashed': 1,
     'for': 2,
     'get': 1,
     'getting': 1,
     'had': 3,
     'having': 1,
     'hear': 1,
     'hedge.': 1,
     'her': 6,
     'her.\n': 1,
     'hurried': 1,
     'in': 3,
     'in\n': 1,
     'into': 1,
     'is': 1,
     'it': 6,
     'it!': 1,
     'it,': 2,
     'its': 1,
     'itself,': 1,
     'just': 1,
     'large': 1,
     'late!"': 1,
     'looked': 1,
     'made': 1,
     'making': 1,
     'mind': 2,
     'moment,': 1,
     'much': 1,
     'never\n': 1,
     'no': 1,
     'nor': 1,
     'nothing': 2,
     'of': 7,
     'of\n': 1,
     'on': 1,
     'on,': 1,
     'or': 3,
     'or\n': 1,
     'out': 3,
     'own': 1,
     'peeped': 1,
     'picking': 1,
     'pictures': 2,
     'pink': 1,
     'pleasure': 1,
     'pop': 1,
     'rabbit': 1,
     'rabbit-hole,': 1,
     'ran': 1,
     'ran\n': 1,
     'reading,': 1,
     'remarkable': 1,
     'say': 1,
     'see': 1,
     'seen': 1,
     'shall': 1,
     'she': 5,
     'sister': 2,
     'sitting': 1,
     'sleepy': 1,
     'so': 1,
     'so\n': 1,
     'started': 1,
     'stupid),': 1,
     'suddenly': 1,
     'take\n': 1,
     'that': 1,
     'that,': 1,
     'the': 9,
     'the\n': 3,
     'then': 1,
     'think': 1,
     'thought': 1,
     'time': 1,
     'tired': 1,
     'to': 7,
     'too': 1,
     'took': 1,
     'trouble': 1,
     'twice': 1,
     'under\n': 1,
     'up': 1,
     'use': 1,
     'very': 4,
     'waistcoat-pocket': 1,
     'waistcoat-pocket,': 1,
     'was': 5,
     'watch': 1,
     'watch\n': 1,
     'way': 1,
     'well': 1,
     'went': 1,
     'what': 1,
     'when': 2,
     'whether': 1,
     'with': 3,
     'worth': 1,
     'would': 1}




```python
my_bag_of_words.keys()
```




    dict_keys(['DOWN', 'THE', 'RABBIT-HOLE\n', '\n', 'Alice', 'was', 'beginning', 'to', 'get', 'very', 'tired', 'of', 'sitting', 'by', 'her', 'sister', 'on', 'the\n', 'bank,', 'and', 'having', 'nothing', 'do.', 'Once', 'or', 'twice', 'she', 'had', 'peeped', 'into', 'book', 'reading,', 'but', 'it', 'no', 'pictures', 'conversations', 'in\n', 'it,', '"and', 'what', 'is', 'the', 'use', 'a', 'book,"', 'thought', 'Alice,', '"without', 'or\n', 'conversations?"\n', 'So', 'considering', 'in', 'own', 'mind', '(as', 'well', 'as', 'could,', 'for', 'day', 'made', 'feel', 'sleepy', 'stupid),', 'whether', 'pleasure', 'of\n', 'making', 'daisy-chain', 'would', 'be', 'worth', 'trouble', 'getting', 'up', 'and\n', 'picking', 'daisies,', 'when', 'suddenly', 'White', 'Rabbit', 'with', 'pink', 'eyes', 'ran\n', 'close', 'her.\n', 'There', 'so', 'remarkable', 'that,', 'nor', 'did', 'think', 'so\n', 'much', 'out', 'way', 'hear', 'say', 'itself,', '"Oh', 'dear!', 'Oh\n', 'I', 'shall', 'too', 'late!"', 'But', 'actually', 'took', 'watch\n', 'its', 'waistcoat-pocket', 'looked', 'at', 'then', 'hurried', 'on,', 'Alice\n', 'started', 'feet,', 'flashed', 'across', 'that', 'never\n', 'before', 'seen', 'rabbit', 'either', 'waistcoat-pocket,', 'watch', 'take\n', 'and,', 'burning', 'curiosity,', 'ran', 'field', 'after\n', 'just', 'time', 'see', 'pop', 'down', 'large', 'rabbit-hole,', 'under\n', 'hedge.', 'In', 'another', 'moment,', 'went', 'after', 'it!'])




```python
my_bag_of_words.values()
```




    dict_values([1, 1, 1, 4, 3, 5, 1, 7, 1, 4, 1, 7, 1, 2, 6, 2, 1, 3, 1, 5, 1, 2, 1, 1, 3, 1, 5, 3, 1, 1, 1, 1, 1, 6, 1, 2, 1, 1, 2, 1, 1, 1, 9, 1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])



And here is one where we use a data structure to write to a file:


```python
with open('./my_text_output.txt', 'w') as output_file:
    for key in my_bag_of_words.keys():
        output_file.write(key + ': ' + str(my_bag_of_words[key]) + '\n')

```

### Let's write our frist script

* Copy and paste the following code into a new file.

* Call it my_script.py


```python
##############################
# My First Python Script
#############################

def multiply(a,b):
    return a * b

result = multiply(2, 4)
print(result)

```

    8
    

In order to run your new script, you will call it from the command line by using the following command:

    $python my_script.py

## How To Write The Cython Version:


```python
##############################
# My Compiled Python Program
#############################

cpdef int multiply(int a, int b):
    return a * b

cdef int result
result = multiply(2, 4)
print(result)

```

Save the above lines of code in a new file, and call it 'multiply.pyx'

You will also need to create a setup.py file which is the equivalent of a 'makefile' for C.


```python
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("multiply.pyx")
)

```

In the command line, enter:

    $python setup.py multiply.pyx

## A Scritp for Text Manipulation


```python
##############################
# My Second Python Script
#############################

def parseArray(arr, char):
	my_dict = {}
	count = 0
	for el in arr:
		if(char in el):
			my_dict[el] = 'True'
			count += 1
		else:
			my_dict[el] = 'False'

	return count, my_dict
        

cities = ['Anchorage', 'Boston', 'Chicago', 'Denver',
         'El Paso', 'Fairfax', 'Georgia', 'Irvine']

count_result, dict_resut = parseArray(cities, 's')

print(count_result)
print(dict_resut)
```

    2
    {'Anchorage': 'False', 'Boston': 'True', 'Chicago': 'False', 'Denver': 'False', 'El Paso': 'True', 'Fairfax': 'False', 'Georgia': 'False', 'Irvine': 'False'}
    

## Modules

The Anaconda distribution comes with a lot of useful python modules which can be imported into our scripts with just a single line of code.

### CSV


```python
import csv
with open('./example.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], row['Favorite Coffee Brand'], row['Flavor'])
```

    Carlos Starbucks Pike's Place
    Jorge McDonalds Morning Joe
    Steve Dunkin Donuts Blueberry
    Rogelio Cafeteria Regular
    


```python
reader
```




    <csv.DictReader at 0xc0af908>



As we can see, csv.DictReader doesn't just return a dictionary.

What it returns is actually an object which has methods and variables available to it.

We can peek into this object by using the dir() function as follows:


```python
dir(reader)
```




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__next__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     '_fieldnames',
     'dialect',
     'fieldnames',
     'line_num',
     'reader',
     'restkey',
     'restval']



Let's take a closer look into one of these objects:


```python
print(reader.__dict__)
```

    {'_fieldnames': ['Name', 'Favorite Coffee Brand', 'Flavor'], 'restkey': None, 'restval': None, 'reader': <_csv.reader object at 0x000000000C04A8D0>, 'dialect': 'excel', 'line_num': 5}
    


```python
print(reader.fieldnames)
```

    ['Name', 'Favorite Coffee Brand', 'Flavor']
    


```python
print(reader.line_num)
```

    5
    

## Pandas

Pandas is shortname for "Python for Analytics and Data Science".

It has been developed over the years by the open source community to become one of the premiere Python modules that comes with the Anaconda distribution.

Among the many great features that Pandas has to offer, arguably the greatest one is the great support for the "Dataframe" data structure.  It allows a data scientist to quickly load up vast amounts of data into a data structure that makes it incredibly easy and convenient to perform very extensive data exploration and manipulation.

Let's look at an example of how to work with it!


```python
import pandas as pd
```


```python
my_dataframe = pd.read_csv('./example.csv')
my_dataframe
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Favorite Coffee Brand</th>
      <th>Flavor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Carlos</td>
      <td>Starbucks</td>
      <td>Pike's Place</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jorge</td>
      <td>McDonalds</td>
      <td>Morning Joe</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Steve</td>
      <td>Dunkin Donuts</td>
      <td>Blueberry</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Rogelio</td>
      <td>Cafeteria</td>
      <td>Regular</td>
    </tr>
  </tbody>
</table>
</div>




```python
for i, value in enumerate(my_dataframe['Name']):
    if(value == 'Carlos'):
        print(my_dataframe.loc[i,'Favorite Coffee Brand'])
```

    Starbucks
    

## Numpy

Another great module is numpy which is the default python library used for numeric computation and working with scientific data.

Let's take a look at how we may combine numpy and pandas!


```python
import numpy as np
```

With numpy, it is easy to create an array of floating point numbers that fall within a range.

Here's how:


```python
my_range_array = np.arange(0,4)
my_range_array
```




    array([0, 1, 2, 3])



Notice above that the left "limit" of the range provided is inclusive wheras the right "limit" is exclusive.

Be mindful of this fact when creating your own arays.

Now, let's create an array of numbers equidistant from each other and increasing linearly along a given range:


```python
my_linear_array = np.linspace(0,25,10)
my_linear_array
```




    array([  0.        ,   2.77777778,   5.55555556,   8.33333333,
            11.11111111,  13.88888889,  16.66666667,  19.44444444,
            22.22222222,  25.        ])



Lastly, let's look at how we could create an array of random numbers:


```python
my_random_array = [np.random.choice(my_linear_array, replace=False) for i in range(0,4)]
my_random_array
```




    [19.444444444444443,
     11.111111111111111,
     8.3333333333333321,
     16.666666666666664]



But how is this at all useful!!??


```python
my_dataframe['AVG_Visits_per_Month'] = my_random_array
my_dataframe
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Favorite Coffee Brand</th>
      <th>Flavor</th>
      <th>AVG_Visits_per_Month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Carlos</td>
      <td>Starbucks</td>
      <td>Pike's Place</td>
      <td>19.444444</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jorge</td>
      <td>McDonalds</td>
      <td>Morning Joe</td>
      <td>11.111111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Steve</td>
      <td>Dunkin Donuts</td>
      <td>Blueberry</td>
      <td>8.333333</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Rogelio</td>
      <td>Cafeteria</td>
      <td>Regular</td>
      <td>16.666667</td>
    </tr>
  </tbody>
</table>
</div>



## Why and When Should I Use Python?

Python is a very powerful tool when it comes to data wrangling, analysis and mining.

I recommend to start using Python in the following scenarios:

* When you need to modify the same fields in multiple rows of a text or csv file.
* When you have an idea that you want to quickly develop and test without having to use formal coding techniques.
* When you are thinking of creating a macro in Excel, I challenge you to create the same idea in a Python script.

# Resources

### [Carlos Beas Github Repo](https://github.com/cgbeas) 

### [Abel Gomez Github Repo](https://github.com/abgomez/intro-python)

### [Official Python Documentation](https://www.python.org/doc/)
