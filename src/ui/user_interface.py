from services.tool import Tool

GAMECOMMANDS = {
    "Q": "Type 'Q' to quit to menu",
    "D": "Type 'D' to double",
    "F": "Type 'F' to surrender",
    "H": "Type 'H' to hit",
    "S": "Type 'S' to stand",
    "Y": "Type 'Y' to split",
}
MENUCOMMANDS = {
    "Q": "Type 'Q' to quit",
    "O": "Type 'O' for Options",
    "P": "Type 'P' to play",
    "S": "Type 'S' for statistics"
}
STATCOMMANDS = {
    "Q": "Type 'Q' to quit to menu",
    "R": "Type 'R' to reset statistics"
}
OPTIONCOMMANDS = {
    "1: Surrender": "ON",
    "2: Double after split allowed": "ON"
}


class User_interface:
    def __init__(self):
        self.tool = Tool()
        self.separator = "-"*60

    def start(self):
        while True:
            self._menu_screen()
            self._menu_commands()
            menucommand = input(f"\n{self.separator}\ninput: ").upper()
            print(f"{self.separator}")
            if menucommand == "Q":
                break
            elif menucommand == "S":
                self._statistics()
            elif menucommand == "P":
                self._game()
            elif menucommand == "O":
                self._options()

    def _menu_screen(self):
        print(f"{self.separator}\n    ____  _        _    ____ _  __   _   _    ____ _  __\n\
   | __ )| |      / \  / ___| |/ /  | | / \  / ___| |/ /\n\
   |  _ \| |     / _ \| |   | ' /_  | |/ _ \| |   | ' / \n\
   | |_) | |___ / ___ | |___| . | |_| / ___ | |___| . \ \n\
   |____/|_____/_/   \_\____|_|\_\___/_/   \_\____|_|\_\ \n\
       ____ _____ ____     _  _____ _____ ______   __     \n\
      / ___|_   _|  _ \   / \|_   _| ____/ ___\ \ / /     \n\
      \___ \ | | | |_) | / _ \ | | |  _|| |  _ \ V /      \n\
       ___) || | |  _ < / ___ \| | | |__| |_| | | |       \n\
      |____/ |_| |_| \_/_/   \_|_| |_____\____| |_|       \n\
                  _____ ___   ___  _                    \n\
                 |_   _/ _ \ / _ \| |                   \n\
                   | || | | | | | | |                   \n\
                   | || |_| | |_| | |___                \n\
                   |_| \___/ \___/|_____|               \n\n")

    def _statistics(self):
        while True:
            Wins = self.tool.return_stats()["W"]
            Losses = self.tool.return_stats()["L"]
            if Wins+Losses == 0:
                print(
                    f"\n\n\n\n\n\n\n\nThere are zero recorded games. Go play some games.\n\n\n\n\n\n\n\n")
            else:
                prctage = Wins/(Wins+Losses)
                if Losses == 0:
                    if Wins > 1:
                        print(
                            f"\n\n\n\n\n\n\n\nYou are an absolute machine, a specimen to be envied.\nYou picked the optimal strategy every time out of {Wins} games.\n\n\n\n\n\n\n\n")
                    else:
                        print(
                            f"\n\n\n\n\n\n\n\nYou picked the optimal strategy in the one game you played.\nGo play some games.\n\n\n\n\n\n\n\n")
                elif Wins == 0:
                    print(
                        f"\n\n\n\n\n\n\n\nSo you lost all the games you played, big deal.\nHit the reset button and get back to work!\n\n\n\n\n\n\n\n")
                else:
                    print(
                        f"\n\n\n\n\n\n\nYou picked the correct strategy {Wins} times, and the wrong\nstrategy {Losses} times.\n")
                    print("Your percentage of success was %.2f\n\n\n\n\n\n" % prctage)
            self._stat_commands()
            statcommand = input(f"\n{self.separator}\ninput: ").upper()
            if statcommand == "Q":
                break
            elif statcommand == "R":
                self.tool.reset_stats()

    def _game(self):
        self._instructions()
        while True:
            self.tool.tool_new_hand()
            print(self.tool.show_hands())

            if self.tool.check_for_blackjack():
                print(
                    f"Blackjack! Players with luck don't need strategy\n{self.separator}")
                continue

            wsbd = self.tool.strategy()
            gamecommand = input("command: ").upper()

            if gamecommand == "Q":
                break
            elif gamecommand in {"D", "F", "H", "S", "Y"}:
                if gamecommand == wsbd:
                    print(
                        f"\nYou chose the correct strategy, which was: {wsbd}")
                else:
                    print(
                        f"\nYou chose... poorly. The correct strategy was {wsbd}, you chose {gamecommand}")
                print(f"\n{self.separator}")
                self.tool.tracking(gamecommand, wsbd)
            else:
                print(
                    f"\nInvalid command, see commands below:\n{self.separator}")
                self._instructions()

    def _options(self):
        while True:
            self._options_listed()
            print(f"Type the number of setting you want to change")
            print(f"\nType 'Q' to quit to menu\n")
            option_command = input(f"\n{self.separator}\ninput: ").upper()
            print(f"{self.separator}")
            if option_command == "Q":
                break
            if option_command == "1":
                if OPTIONCOMMANDS.get("1: Surrender") == "ON":
                    OPTIONCOMMANDS["1: Surrender"] = "OFF"
                else:
                    OPTIONCOMMANDS["1: Surrender"] = "ON"
                self.tool.change_surrender_status()
            if option_command == "2":
                if OPTIONCOMMANDS.get("2: Double after split allowed") == "ON":
                    OPTIONCOMMANDS["2: Double after split allowed"] = "OFF"
                else:
                    OPTIONCOMMANDS["2: Double after split allowed"] = "ON"
                self.tool.change_das_status()

    def _options_listed(self):
        for instruction in OPTIONCOMMANDS:
            buffer = " " * \
                (60-(len(instruction)+len(OPTIONCOMMANDS[instruction])))
            print(f"{instruction}{buffer}{OPTIONCOMMANDS[instruction]}")
            print("\n")

    def _instructions(self):
        for instruction in GAMECOMMANDS:
            print(GAMECOMMANDS[instruction])
        print("\n")

    def _menu_commands(self):
        for command in MENUCOMMANDS:
            if command == "P":
                print("\n")
            if command == "O":
                print("", end="   ")
            print(f"{MENUCOMMANDS[command]}", end="                     ")

    def _stat_commands(self):
        for command in STATCOMMANDS:
            print(f"{STATCOMMANDS[command]}", end="       ")
