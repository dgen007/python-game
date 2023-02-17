class Employee():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.fullname = fname +" "+ lname

    def favourite_quote(self,quote="Hello World!!"):
        return f"{self.fname}'s favourite quote is {quote}"

# class Student():
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#         self.email = f"{fname.lower()}.{lname.lower()}@genuni.co.uk"




#Create a class for students of GenUni
#should have attributes for first and last name of student
#the third attrbute should be for email which is concatenating
#first_name(.)last_name@genuni.co.uk
#Print the students first name(.)last name and email

#Create a method that generates ths student id by concatenating the 
#students first and last names with their birth month as a parameter
#when you call the method DAVIDAKUMA06