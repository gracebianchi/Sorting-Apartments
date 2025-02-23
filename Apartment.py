# Apartment.py

class Apartment:

    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return f"(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.metersFromUCSB}m, Condition: {self.condition}"

    def __eq__(self, other):
        if self.rent == other.rent:
            if self.metersFromUCSB == other.metersFromUCSB:
                if self.condition == other.condition:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __lt__(self, other):
        if self.rent < other.rent:
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB < other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
                conditions = {"bad":0, "average":1, "excellent":2}
                return conditions[self.condition] > conditions[other.condition]
            else:
                return False
        else:
            return False
        
    def __gt__(self, other):
        if self.rent > other.rent:
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB > other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
                conditions = {"bad":0, "average":1, "excellent":2}
                return conditions[self.condition] < conditions[other.condition]
            else:
                return False
        else:
            return False


    
