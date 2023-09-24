'''
ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す

tom.full_name()  # "Tom Ford" という値を返す
'''
class Customer:
    def __init__(self,first_name,family_name):
        self.first_name=first_name.capitalize()
        self.family_name=family_name.capitalize()
        print(self.first_name,self.family_name)

ken = Customer(first_name="ken",family_name="tanaka")
tom = Customer(first_name="tom",family_name="ford")
