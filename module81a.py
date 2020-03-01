class calc():
    def add(self, input2):
        total_val = (self + input2)
        print(total_val)
    def subtract(self, input2):
        total_val = (self - input2)
        print(total_val)
    def multiply(self, input2):
        total_val = (self * input2)
        print(total_val)
    def divide(self, input2):
        if input2  == 0:
            print("DIV/0")
        else:
          total_val = (self / input2)
          print(total_val)


calc.divide(2,0)
calc.add(2,10)
calc.subtract(10,5)
calc.multiply(10,10)
