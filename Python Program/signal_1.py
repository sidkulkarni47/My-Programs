print("This is a signal at a crossing")

print("""Press the button for walk sign to light up!
        1. Press
        2. Wait""")

option_choosen = input("Select: ").lower()
camera = input("Did camera see a suspicious activity(Type in yes or no): ").lower()

def walkOrNo():
    if option_choosen == "press":
        print("The walk sign is on, you can cross the street!")
    elif option_choosen == "wait":
        print("Wait till walk sign lights up automatically!") 

def fine():
    if camera == "yes":
        print("This a finable offence, please follow the instructions or you will be fine ")
    elif camera == "no":
        print("He is waiting for the lights to turn on automatically")

def speaker():
    
    camera2 = input("Instructions ignored and trying to cross the street?(Reply- Yes/No):").lower()
    if not camera2:
            print("Message from Camera - Data receiving in progress!")
            camera3 = input("Instructions ignored and trying to cross the street?(Reply- Yes/No): ").lower()
            camera3 == camera2
    else:
        if camera2 == "yes":
                    print("LOUD SPEAKER: Please wait do not cross, you are putting your life in danger")
        else:
                    print("Please follow the instruction, last warning!")       


if not option_choosen:
    print("Please enter response to the instructions!")
    if not camera:
        print("Message from Camera - Data receiving in progress!")
        camera1 = input("Re-enter--Did camera see a suspicious activity(Type in yes or no): ").lower()
        camera = camera1
        fine()
        speaker()

else:
    walkOrNo()





