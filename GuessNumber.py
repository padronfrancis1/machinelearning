response = input("how many games would you like to play: ")

class MyClass():

    def game_loop(self, param1):
        self.param1 = int(param1)
        self.param2 = None

        i = 0
        while i <= self.param1 - 1:
            self.param2 = input("Please enter a number between 1 - 25: ")

            if self.param2.isdigit():
                if int(self.param2) <= 25:

                    val = int(self.param2)

                    if val == self.param1:
                        print("Youre guess is rght")
                        break
                    elif val < self.param1:
                        print("higher")
                    elif val > self.param1:
                        print("lower")
                    else:
                        pass
                elif int(self.param2) < 0:
                    print("number should be greater than 0")
                elif int(self.param2) > 25:
                    print("number should be less than 25")


            else:
                print("Please enter digits only")

            i += 1

if response.isdigit():
    a = MyClass()
    a.game_loop(int(response))
else:
    print("Please enter valid inputs")