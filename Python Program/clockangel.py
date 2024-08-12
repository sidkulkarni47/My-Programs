print("This program is to calculate the angle on the clock by entering the minute hand and hour hand.")

hour_hand = int(input("Please enter the hour hand: "))
min_hand = int(input("Please enter the min hand: "))

actual_time = str(hour_hand) + ":" + str(min_hand)
print("The actual time is-", actual_time)



def all():
    hour = (360/12)*hour_hand + ((min_hand/60)*(360/12))
    min = (360/60)*min_hand
    angle = abs(hour - min)
    return angle
    
angle = all()
print("This is the angle: " , angle)