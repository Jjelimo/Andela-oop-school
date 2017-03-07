class Andela_School(object):
    def _init_(self,name,identification_card,year_joined,course,hostel,balance,room_no):
        self.name=name
        self.identificatin_card=identification_card
        self.year_joined=year_joined
        self.course=course
        self.hostel=hostel
        self.balance=balance
        self.room_no=room_no
class Department(Andela_School):
    def Department (self):
        print ("name: "),self.name,("identification_card"), self.identification_card,("course: "),self.course,("year_joined: "),self.year_joined
    def finance(self):
        if self.balance==0:
            print ("name: "),self.name, ("identification_card"),self.identification_card ("\nyou have cleared your fee balance")
        else:
            print ("name: "),self.name, ("balance"),self.balance, ("\nplease clear your balance")
    def accomodation(self,amount):
         if amount==o:
             print ("\sorry you have not paid for your accomodation")
         else:
             print ("name: "), self.name, ("hostel"), self.hostel, ("room_no"), self.room_no ("\n welcome to your new hostel")