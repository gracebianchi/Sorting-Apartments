# testFile.py

from Apartment import Apartment
from lab06 import *

def test_Apartment():
    a1 = Apartment(1250, 300, "bad")
    a2 = Apartment(900, 200, "average")
    a3 = Apartment(1500, 400, "excellent")
    a4 = Apartment(800, 190, "excellent")
    a5 = Apartment(500, 250, "average")
    apartmentList = [a1, a2, a3, a4, a5]

    assert a1.getRent() == 1250
    assert a2.getMetersFromUCSB() == 200
    assert a3.getCondition() == "excellent"
    assert a4.getApartmentDetails() == "(Apartment) Rent: $800, Distance From UCSB: 190m, Condition: excellent"
    assert a1 == a1
    assert a4 > a5
    assert a5 < a4

def test_lab06():
    a1 = Apartment(1250, 300, "bad")
    a2 = Apartment(900, 200, "average")
    a3 = Apartment(1500, 400, "excellent")
    a4 = Apartment(800, 190, "excellent")
    a5 = Apartment(500, 250, "average")
    apartmentList = [a1, a2, a3, a4, a5]

    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    assert getBestApartment(apartmentList) == "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: average"
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1500, Distance From UCSB: 400m, Condition: excellent"
    assert getAffordableApartments(apartmentList, 800) == "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: average\n(Apartment) Rent: $800, Distance From UCSB: 190m, Condition: excellent"
    
