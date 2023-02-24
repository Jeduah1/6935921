#Define a dictionary of cars and their prices 
cars = {"Tesla":25000,"Toyota":3000,"Jeep":27000,"Chevrolet":30000,"BMW":40000,"Cadillac":60000,"Lexus":35000,\
        "Buick":51000,"Hyundai":35000,"Ford":45000,"Lamborghini":27000,"Nissan":35000,"Mazda":45000,"Mini":35000,\
        "Honda":60000,"Audi":40000,"Kia":50000,"Porsche":30000,"Toyota-Tundra":26000,"Alf Romeo":45000,\
        "Toyota-Yaris":40005,"Vibe":53000,"Vibe-Pontiac":60000,"Sportage":34556,"Citron":13246,"Aston-Marton":90000}
# Ask the user for their car brand choices
car_brand = input("Enter the car brand you are looking for:")
# Check if the car is available in the dealership
if car_brand in cars:
    print("Yes, the car is available.")
    print("The sales price of the car is :",cars[car_brand])
else:
    print("Sorry the car is not available at the moment.")
#https://github.com/Jeduah1/6935921.git