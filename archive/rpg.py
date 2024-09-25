# This file was archived because I have no freaking idea on how the heck I can make an RPG.
def do_rpg(self, line):
        """Launch the GenRPG script - A generic text-based Role-Playing Game."""
        game_start = True
        while game_start == True:
            start_menu = int(input("Hello there! Would you like to: 1) Start a new game, 2) Load a previous save OR 3) Quit: "))
            if start_menu == 1:
                print('???: Hello, adventurer!')
                print('Genna: I am the Generic Narrator, but you can call be Genna.')
                print('Genna: Apparently this RPG hasn\'t been released to the public, I wonder how...')
                print('Genna: Anyways, what is your name?')
                name = input('Input your name: ')
                hero = {
                    'hero_name': name,
                    'max_health': 100
                }
                with open('hero.json', 'w') as outfile:
                    json.dump(hero, outfile)
                print(f'{name}: I am {name}.')
                print(f'Genna: Why hello there, {name}!')
                print('Genna: It looks like you managed to be a generic adventurer, although I myself, line, am just an NPC.')
                print('Genna: Anywho, let\'s get started!')
                print('You are at the local tavern, and you have gotten some starter equipment by the landlord.')
                print('It isn\'t much, but they wanted to help you out for your adventure.')
                print('Genna: You\'ll need to select option 2 in order to continue. I dunno why, but Leon hasn\'t made an option to start from here. Nobody knows why he didn\'t.')
            elif start_menu == 2:
                game_start = False
                with open('hero.json', 'r') as checkfile:
                    hero = json.load(checkfile)
                    print('Genna: Welcome back, ' + hero["hero_name"] + "!")
                    print('Genna: Let\'s go kick some butt like we always do.')
                    print("The landlord who gave you some equipment knocks on the door.")
                    print("Landlord?: Hello there, " + hero["hero_name"] + "!")
                print("You open the door and let the landlord in.")
                print("Sherry: I'm Sherry, and I see you've gotten well equipped.")
                print("Sherry: I'm sorry if it isn't much, but its hopefully the least I can do.")
                print("Sherry: Anyways, do you want to come down and meet the crew?")
                dialogueA = input('Select the following options (A: "Crew?", Other: *Go down*): ')
                if dialogueA == 'A':
                    print("Sherry: They're some people who want to tag along for the fight, if you're up.")
                else:
                    print("You go down the stairs and see a group of strangers who want to help you. You are slightly anxious but you fight it.")
            elif start_menu == 3:
                print('Farewell, traveller. See you again soon!')
                quit()
            else:
                print('Please select option 1, 2 or 3.')
