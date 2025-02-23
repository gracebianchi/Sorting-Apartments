# Sorting-Apartments

You will need to create three files:

Apartment.py - file containing a class definition for an Apartment object
lab06.py - file containing mergesort and other functions defined in the lab06.py section of this lab.
testFile.py - file containing pytest functions testing the overall correctness of your class definitions
There will be no starter code for this assignment, but rather the class descriptions and required methods are defined in the specification below.

You should organize your lab work in its own directory. This way all files for a lab are located in a single folder. Also, this will be easy to import various files into your code using the import / from technique shown in lecture.

Apartment.py class
The Apartment.py file will contain the definition of an Apartment. We will define the Apartment attributes as follows:

rent - integer that represents the rent of the Apartment
metersFromUCSB - integer that represents the Apartment’s distance, in meters, from UCSB
condition - string that represents the condition of the Apartment. This string will be one of three options: "bad", "average", or "excellent".
You should write a constructor that allows the user to construct an apartment object by passing in values for all of the fields. You may assume that all attributes of the Apartment object will be defined. Therefore, there should be no default values for rent, metersFromUCSB, or condition.

__init__(self, rent, metersFromUCSB, condition)
In addition to your constructor, your class definition should also support “getter” methods that can receive the state of the Apartment object:

getRent(self)
getMetersFromUCSB(self)
getCondition(self)
You will also implement the method

getApartmentDetails(self)
that returns a str with all of the Apartment attributes. The string should contain all attributes in the following EXACT format (Note: There is no \n character at the end of this string):

a0 = Apartment(1204, 200, "bad")
print(a0.getApartmentDetails())
Output

(Apartment) Rent: $1204, Distance From UCSB: 200m, Condition: bad
Lastly, your Apartment class should overload the >,<, and == operators. This will be used when finding the proper position of an Apartment in the list using the specifications in the Introduction section of this lab. In this context for example, the < operator will return True for Apartment1 < Apartment2 if Apartment1 is better than Apartment2. We reviewed operator overloading in class and the textbook does discuss overloading Python operators. You can also refer to this reference on overloading various operators as well:
https://www.geeksforgeeks.org/operator-overloading-in-python/

lab06.py
This file will contain functions that sort a list of Apartment objects, ensures that the list of Apartment objects are in asending order (best-to-worst), retrives information about the best/worst apartments, and gets the info of every affordable apartment in the list. These function defintions as well as their descriptions are provided below. Note that in order for the autograder to correctly check your implementation, function defintions must match exactly.

mergesort(apartmentList) - Performs a mergesort on the apartmentList passed as input. Sorts the Apartment objects based on the specifications in the Introduction section of this lab. Gradescope will test to ensure that your mergesort implementation’s Big-O is O(NlogN).
ensureSortedAscending(apartmentList) - method that returns a boolean value. True if the apartmentList is sorted correctly in asending order. False otherwise.
getBestApartment(apartmentList) - method that returns a string detailing the best Apartment’s rent, meters from UCSB, and condition. Make use of getApartmentDetails(self) and mergesort(apartmentList). You can assume that apartmentList has at least one apartment.
getWorstApartment(apartmentList) - method that returns a string detailing the worst Apartment’s rent, meters from UCSB, and condition. Make use of getApartmentDetails(self) and mergesort(apartmentList). You can assume that apartmentList has at least one apartment.
getAffordableApartments(apartmentList, budget) - method that returns a labeled, newline separated string detailing the rent, meters from UCSB, and condition of all the apartments whose rent is less than or equal to budget from the apartmentList in sorted order. Make use of getApartmentDetails(self) and mergesort(apartmentList). You can assume that apartmentList has at least one apartment and that there is no newline at the end of the string returned by this method. If there are no apartments that are affordable in the apartmentList, this method returns an empty string.
Sample Output 1
a0 = Apartment(1115, 215, "bad")
a1 = Apartment(950, 215, "average")
a2 = Apartment(950, 215, "excellent")
a3 = Apartment(950, 190, "excellent")
a4 = Apartment(900, 190, "excellent")
a5 = Apartment(500, 250, "bad")
apartmentList = [a0, a1, a2, a3, a4, a5]


print('apartmentList is NOT SORTED:')
for apartment in apartmentList: 
    print(apartment.getApartmentDetails())

assert ensureSortedAscending(apartmentList) == False
mergesort(apartmentList)
assert ensureSortedAscending(apartmentList) == True

print('apartmentList is SORTED:')
for apartment in apartmentList: 
    print(apartment.getApartmentDetails())
Output:

apartmentList is NOT SORTED:
(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad
(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average
(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: excellent
(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent
(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent
(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad
apartmentList is SORTED:
(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad
(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent
(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent
(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: excellent
(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average
(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad
Sample Output 2
a0 = Apartment(1200, 200, "average")
a1 = Apartment(1200, 200, "excellent")
a2 = Apartment(1000, 100, "average")
a3 = Apartment(1000, 215, "excellent")
a4 = Apartment(700, 315, "bad")
a5 = Apartment(800, 250, "excellent")
apartmentList = [a0, a1, a2, a3, a4, a5]

assert ensureSortedAscending(apartmentList) == False

print('Best Apartment in apartmentList:')
print(getBestApartment(apartmentList))

print('Worst Apartment in apartmentList:')
print(getWorstApartment(apartmentList))

Output:

Best Apartment in apartmentList: 
(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad
Worst Apartment in apartmentList:
(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average
Sample Output 3
a0 = Apartment(1115, 215, "bad")
a1 = Apartment(970, 215, "average")
a2 = Apartment(950, 215, "average")
a3 = Apartment(950, 190, "excellent")
a4 = Apartment(900, 190, "excellent")
a5 = Apartment(500, 250, "bad")
apartmentList = [a0, a1, a2, a3, a4, a5]

print('All apartments whose rent is <= in SORTED order:')
print(getAffordableApartments(apartmentList, 950))

Output:

All apartments whose rent is <= in SORTED order:
(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad
(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent
(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent
(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average
A Brief Note on Sorting Apartments
A common question that students have when working through this lab is

The directions say that a0 < a1 should return true if apartment a0 is a better apartment than a1. Intuitively though, why would the apartment that is lesser (<) be “better than” the other apartment?

Recall that you are sorting apartments in ascending order. For example, if you sorted runners in a race by the position they finished in you would do something like this:

1 4 3 2 5 —> 1 2 3 4 5

It is clear that 1<2, 2<3 etc. Notice that the 1st place runner finished in a “better” position even though they have a “lesser” position than the others. The same concept applies here to apartments.

How to Best Approach This Lab
There are a lot of parts to this lab that rely on one another. So if you’re failing a test and find yourself stuck it might be because of code that you’ve written elsewhere. To alleviate some of this stress, here are the suggested order in which you complete the functions required for this lab:

constructor and getters in Apartment.py
getApartmentDetails in Apartment.py
<, >, and == overloaded operators in Apartment.py
ensureSortedAscending in lab06.py
mergesort in lab06.py
getBestApartment and getWorstApartment in lab06.py
getAffordableApartments in lab06.py
testFile.py pytest
This file should import your Apartment.py class and your lab06.py function. You should write tests using pytest to test if the functionality is correct. Think of various scenarios and edge cases when testing your code. Write your tests first in order to check the correctness of the Apartment and then lab06.py methods. Gradescope requires testFile.py to be submitted before running any autograded tests. You should write at least one test for each method in each of these classes. This includes the overloaded operators but excludes the getters.
