class Andela_School(object):

    def _init_(self,name,identification_card):
        self.name=name
        self.identification_card=identification_card
        self.year_joined=year_joined
        self.course=course
        self.hostel=hostel
        self.balance=0
        self.room_no=room_no
        

class Department(Andela_School):

    def Department (self):

        self.name=name

        self.identification_card=identification_card

        self.course=course

        self.balance=balance

    def finance(self,amount):

        self.name=name

        self.identification_card=identification_card

        if amount > self.balance:

            print "You have not cleared your fee balance"

        else:
            self.balance=amount

            return self.balance



    def accomodation(self,amount):

         if amount==o:

             print ("\sorry you have not paid for your accomodation")

         else:

             print ("name: "), self.name, ("hostel"), self.hostel, ("room_no"), self.room_no ("\n welcome to your new hostel")