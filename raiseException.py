class ageCheck:
    def age1(self):
        try:
            a = int(input('enter the age of person:'))
            if a>18:
                print('you are illigible')
            else:
                raise ValueError
        except ValueError:
            print('you are not illigible')
        
ob= ageCheck()
ob.age1()
