class Calculator():
    
  def add(self, a, b):
      return a + b
  
  def sub(self, a, b):
     pass

if __name__ == "__main__":
    mycal = Calculator()
    print(mycal.add(5, 10))  # Expected output: 15
