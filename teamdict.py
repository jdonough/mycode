#! /usr/bin/env python3
cars = {"Ferrari": "fast", "Truck": "slow"}

cars2 = cars.copy()

cars2["Truck"] = "big"
print( cars.keys() )
print( cars.values() )
print( cars2.keys() )
print( cars2.values() )


print(cars2)
print(cars)
