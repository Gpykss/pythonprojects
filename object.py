

if __name__=='__main__' :
    class drug:#blueprint for creating the object

        comp = "Weekspharm" #this is a class variable which can be used by any instance of the object

        def __init__(self,work,year,type,name):
            self.work =work #instance variable they can only be used or be specific to a paticular instance of the object
            self.year =year
            self.type = type
            self.name = name

        def display_name(self):
            print(f"This drug caled {self.name} was produced by {self.comp}")




    drug1 = drug(0,0,0,"great")
    drug2 = drug(0,0,0,"joe")
    drug3 = drug(0,0,0,"meks")
    drug4 = drug.comp


    print(drug1.name)
    print(drug2.name)
    print(drug3.name)
    print(drug4)


    print()
    drug3.display_name()

    class family:
        total_family = 0
        def __init__(self, name, position):
            self.name = name
            self.position = position
            family.total_family +=1

        def cousins(self):
            print(f"{self.name} is my cousin ")


    class family3(family,drug):#this inherits from the family class
        pass

    class bfam (family3):
        pass

    family1 = family("john", "family")
    family2 = family("grace", "great-aunt")
    family4 = family3("grace" , "prince")

    print(family4.name)
    print(family4.position)
    family4.cousins()
    afg = bfam("great,", 0)
    afg.display_name()

    print(f" the total family is {family.total_family}")