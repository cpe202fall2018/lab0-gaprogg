def weight_on_planets():
   raw_weight = input("What do you weigh on earth? ")
   e_weight = float(raw_weight)
   print("\nOn Mars you would weigh", 0.38*e_weight, "pounds.\nOn Jupiter you would weigh", 2.34*e_weight, "pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()
