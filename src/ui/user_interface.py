from services.tool import Tool

COMMANDS = {
    "Q": "Type 'Q' to quit",
    "D": "Type 'D' to double",
    "F": "Type 'F' to surrender",
    "H": "Type 'H' to hit",
    "S": "Type 'S' to stand",
    "Y": "Type 'Y' to split",
}

class User_interface:
    def __init__(self):
        self.tool = Tool()
    def _start(self):
        self._instructions()

        while True:
            self.tool._new_hand()
            self.tool._show_hands()
            command = input("command: ")

            if command.lower() == "q":
                break
            elif command.lower() == "d":
                pass
                #self.tool._double()
            elif command.lower() == "f":
                #self._surrender()
                pass
            elif command.lower() == "h":
                #self._hit()
                pass
            elif command.lower() == "s":
                #self._stand()
                pass
            elif command.lower() == "y":
                #self._split()
                pass
            else:
                print("invalid command, see commands below:")
                self._instructions()
    
    def _instructions(self):
        for instruction in COMMANDS:
            print(COMMANDS[instruction])
        print("\n")