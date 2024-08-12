print("This is me, Printer!")

printer_input = input("Enter the option you would like to proceed with(Photocopy, Scan, Fax)-").lower()

if printer_input == "photocopy":
    copy_input = input("Please place the paper in the machine and enter Yes! - ").lower()
    if copy_input == "":
        print("The machine cannot detect the paper!")
elif printer_input == "Scan":
    scan_input = input("Please place the paper in the machine to Scan and enter Yes! - ").lower()
    if scan_input == "":
        print("The machine cannot detect the paper!")
else:
    fax_input = input("Please place the paper in the machine to Scan and enter Yes! - ").lower()
    if fax_input == "":
        print("The machine cannot detect the paper!")
