import os
clear = lambda: os.system('cls')
clear()
feet_inches=input("enter feet and inches: " )
height =1
def convert(feet_inches):
    parts= feet_inches.split(" ")
    feet = float(parts[0])
    inches=float(parts[1])

    meters= (feet*0.3848) +(inches *0.0254)
    return meters

result = convert (feet_inches)
if result < height:
    print ("kid is too small")
else:
    print ("go on kiddo")
           ~                
