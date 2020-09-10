#Question 1
# You all are Pilots, you want to land a plane safely, so altitude required for landing a plane is
# 1000ft, it it is less than tell pilot to land the plane, or it is more than that but less than 5000ft ask
# the pilot to “come down to 1000ft”, else if it more than 5000ft ask the pilot to “go around and try
# later”
# Example : Input - 1000
# Output - Safe to Land
# Example : Input - 4500
# Output - Bring down to 1000
# Example : Input - 6500
# Output - Turn Around

height=int(input("Enter height in ft "))

if(height==1000):
    print("Safe to land")

elif(height>1000 and height<5000 ):
    print("Bring down to 1000 ft")
else:
    print("Turn Aronund")
