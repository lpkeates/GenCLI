# Modules (`cmd` is mandatory, `json` is required if you want to allow for configurations)
import cmd
import wikipedia
import random
import json
import time

# Loads the json file (if you want to change the prompt, make sure to do `prompt = <prompt prefix>`)
class myCLI(cmd.Cmd):
    with open("config.json", "r") as configcli:
        config = json.load(configcli)

    prompt = config['general']["prompt"]
    intro = r"""
   ______           ________    ____
  / ____/__  ____  / ____/ /   /  _/
 / / __/ _ \/ __ \/ /   / /    / /  
/ /_/ /  __/ / / / /___/ /____/ /   
\____/\___/_/ /_/\____/_____/___/

"A Generic Command Line Interface."
Version: Alpha-2.1 
Creator: Leon Peter Keates

Type `help` for more commands."""

    # Test command
    def do_ping(self, line):
        """Misc: Responds with 'Pong!'"""
        print('Pong!')

    # The "killswitch" in case of an update.
    def do_terminate(self, line):
        """System: Terminates the CLI"""
        return True
        
    # Another test command
    def do_hello(self, line):
        """Misc: Responds with 'Hello, world!'"""
        print('Hello, world!')

    # Shows the about info about GenCLI. You can edit this if you may.
    def do_about(self, line):
        """System: Shows basic information about GenCLI"""
        print("""Name: GenCLI (Generic Command Line Interface)
        Creator: Leon Peter Keates (leonpeterkeates@gmail.com)
        Website: N/A
        Current Version: Alpha-2.1 (updated 20/06/2024)
        Programmed In: Python
        Language: en-GB (British English)
        Status: Active (since 15/05/2024)""")

    # REQUIRES THE `wikipedia` MODULE.
    def do_wiki(self, line):
        """Tool: Searches for articles and/or get a summary of such on the English Wikipedia."""
        mode = int(input("Would you like to 1) Search for articles OR 2) Get a summary on an article: "))
        if mode == 1:
            query = input("What would you like to search?: ")
            search_result = wikipedia.search(query, results = 3)
            print(search_result)
        elif mode == 2:
            query = input("What article would you like to get a summary of?: ")
            summary_result = wikipedia.summary(query, sentences = 5, auto_suggest = False)
            print(summary_result)

    # REQUIRES THE 'random' MODULE.
    def do_rps(self, line):
        """Game: Initiates a game of Rock, Paper and Scissors."""
        user_action = input("Choose one of the following; Rock, Paper or Scissors: ")
        possible_actions = ["Rock", "Paper", "Scissors"]
        computer_action = random.choice(possible_actions)
        print(f'You chose {user_action}, while the computer chose {computer_action}')
        if user_action == computer_action:
            print('Darn, its a draw. You both chose the same option!')
        elif user_action == "Rock":
            if computer_action == "Scissors":
                print('Rock breaks scissors. You win!')
            elif computer_action == "Paper":
                print('Paper covers rock. You lose!')
        elif user_action == "Paper":
            if computer_action == "Rock":
                print('Paper covers rock. You win!')
            elif computer_action == "Scissors":
                print('Scissors cut paper. You lose!')
        elif user_action == "Scissors":
            if computer_action == "Paper":
                print("Scissors cut paper. You win!")
            elif computer_action == "Rock":
                print("Rock breaks scissors. You lose!")

    # A basic changelog command. You can do what the heck you like on this.
    def do_changelog(self, line):
        """System: See the latest update(s) as well as the current version."""
        version = input("What changelog would you like to search for (A1, A2, A2.1): ")
        if version == "A1":
            print("Changelog date: 15/05/2024 | Version Alpha-1 (creation)")
            print("Additions: Created the GenCLI with a lot of stuff.")
            print("Changes: N/A")
            print("Fixes: N/A")
            print("Removals: N/A")
        elif version == "A2":
            print("Changelog date: 19/06/2024 | Version Alpha-2")
            print('Additions: Added `wiki`, `config`, `rps` and `changelog` commands.')
            print("Changes: Changed the intro to avoid errors. The `about` command shows a summary of the project instead of a backstory.")
            print('Fixes: Fixed the intro giving an error upon launch with Python 3.12 or newer.')
            print('Removals: The RPG command will be removed until further notice. I don\'t have an ETA on when or if it will come back, but stay tuned!')
        elif version == "A2.1":
            print("Changelog date: 20/06/2024 | Version Alpha-2.1 (Tweak 1)")
            print('Additions: Added the `dice` command, which can roll a d4, d6, d8, d10, d12 or d20 from Dungeons and Dragons.')
            print('Changes: The help command can show a command\'s category (`rps` would be Game, `wiki` would be tool etc)')
            print('Fixes: Fixed the `about` command being a bit awkward with indentation. Its info was corrected as well.')
            print('Removals: N/A')

    # Allows for advanced configuration, which saves into the `config.json` file.
    def do_config(self, line):
        """System: Allows for configurating the CLI for the prompt (Default: >> ), Wikipedia (Default: Results = 3, Sentences = 5) or reset to default values."""
        change = int(input("What would you like to change? 1) Prompt, 2) Wikipedia Settings OR 3) Reset to default value(s): "))
        if change == 1:
            newPrompt = input("What would you like as your prompt: ")
            with open("config.json", "r") as prompt:
                data = json.load(prompt)

            data['general']['prompt'] = newPrompt
            with open("config.json", "w") as change:
                json.dump(data, change)
            
            return True
        elif change == 2:
            wikichange = int(input("What part would you like to change? 1) Results (for search), 2) Sentences (for summary) OR 3) Language (in general): "))
            if wikichange == 1:
                resultChange = int(input("How many result(s) do you want to see when searching: "))
                with open("config.json", "r") as prompt:
                    data = json.load(prompt)

                    data['wikipedia']['results'] = resultChange
                with open("config.json", "w") as change:
                    json.dump(data, change)
            elif wikichange == 2:
                sentenceChange = int(input("How many sentence(s) do you want to see in your summary: "))
                with open("config.json", "r") as prompt:
                    data = json.load(prompt)

                    data['wikipedia']['results'] = sentenceChange
                with open("config.json", "w") as change:
                    json.dump(data, change)
            elif wikichange == 3:    
                newlang = input("What language would you like to use instead (Example: `fr` for French, `ar` for Arabic or `hr` for Croatian): ")
                wikipedia.set_lang(newlang)
        elif change == 3:
            wikipedia.set_lang("en")
            with open("config.json", "r") as prompt:
                data = json.load(prompt)

            data['general']['prompt'] = ">> "
            data['wikipedia']['results'] = 3
            data['wikipedia']['sentences'] = 5
            with open("config.json", "w") as change:
                json.dump(data, change)

            return True

    # REQUIRES THE 'random' MODULE.
    def do_dice(self, line):
        """Tool: Rolls a dice of any one of the following choice(s): d4, d6, d8, d10, d12, d20"""
        choice = input("What dice would you like to roll? ")
        if choice == "d4":
            print('You rolled a d4, and it makes it...')
            time.sleep(3)
            print(random.randint(1,4))
        elif choice == "d6":
            print('You rolled a d6, and it makes it...')
            time.sleep(3)
            print(random.randint(1,6))
        elif choice == "d8":
            print('You rolled a d8, and it makes it...')
            time.sleep(3)
            print(random.randint(1,8))
        elif choice == "d10":
            print('You rolled a d10, and it makes it...')
            time.sleep(3)
            print(random.randint(1,10))
        elif choice == "d12":
            print('You rolled a d12, and it makes it...')
            time.sleep(3)
            print(random.randint(1,12))
        elif choice == "d20":            
            print('You rolled a d20, and it makes it...')
            time.sleep(3)
            print(random.randint(1,20))

# Keeps the CLI active until you terminate or update the config.
if __name__ == '__main__':
    myCLI().cmdloop()
