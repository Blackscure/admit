class Menu(object):
    def admit(self):
        status = ""
        while status != "q":
            status = input("If you are under 18years enter Yes and Abv if you are above 18years abd q to quit: ")
            if status == "yes":
                print("required age")
            elif status == "Abv":
                print("over age")
            elif status == "q":
                print("quit the program")
                status = "q"
            else:
                print(" sorry status not found")


 