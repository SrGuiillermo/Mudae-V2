harem = []
harem_characters = []
harem_series = []


while len(harem) < 1:
    try:
        with open("harem.txt", "r") as f:
            data = f.read().split("\n")
        for i, x in enumerate(data):
            if i%2 == 0:
                harem_characters.append(x)
            elif i%2 != 0:
                harem_series.append(x)
        harem = list(zip(harem_characters, harem_series))
    except FileNotFoundError:
        print("[harem.txt] file not found or is empty")
        print("You need to add at least one character to continue")
        response = input("Do you want to continue? [Y/N]").lower()
        if response == "n": exit()
        elif response == "y":
            new_character = input("Write new character to add: \n")
            new_series = input("Write serie of that character: \n")
            temp_harem = [new_character, new_series]
            with open("harem.txt", "w") as f:
                f.write("\n".join(temp_harem))


def check_in_harem(character):
    check = False
    for c, s in harem:
        if c.lower() == character : check = True
    return check


def show_harem():
    print()
    for c, s in harem:
        print(c)
    print()


def show_full_harem():
    print()
    for c, s in harem:
        print(c)
        print(s)
    print()


def help_command():
    print()
    print("help -- print this command")
    print("harem -- print your harem")
    print("series -- print series you have characters of")
    print("fullharem -- print your whole harem, including series")
    print("sort -- sort your harem")
    print("add -- add a new character to your harem")
    print("sm -- generate $sm command based on your harem")
    print()


def sort_harem():
    show_harem()
    while True:
        input_character = input("Write character to sort ([ESC] to exit): \n")
        if input_character.lower() == "esc" : break
        while check_in_harem(input_character.lower()) == False and input_character.lower() != "esc":
            input_character = input("Character not in harem, write another character ([ESC] to exit): \n")
        if input_character.lower() == "esc" : break

        input_action = input("What do you want to do with that character: \n"
                            "[C] to change position in command $sm of that character \n"
                            "[R] to remove that character \n"
                            "[S] to change that character's series \n"
                            "[ESC] to exit \n").lower()
        
        if input_action == "esc" : pass

        elif input_action == "c":

            input_ch = input(f"Write character from your harem, {input_character} will be put above in $sm command \n:" 
                              "[LAST] for last position, [ESC] to exit \n")
            while check_in_harem(input_ch.lower()) == False and input_character.lower() != "last" and input_character.lower() != "esc":
                input_ch = input(f"Character not in harem, write another character, {input_character} will be put above in $sm command \n:" 
                                  "[LAST] for last position, [ESC] to exit \n")
            
            if input_ch.lower() == "esc" : break
            
            elif input_ch.lower() == "last":
                for i, h in enumerate(harem):
                    if h[0].lower() == input_character.lower():
                        temp_inp = h
                        del harem[i]
                        break
                harem.append(temp_inp)
            
            else:
                for i, h in enumerate(harem):
                    if h[0].lower() == input_character.lower():
                        temp_inp = h
                        del harem[i]
                        break
                
                for i, h in enumerate(harem):
                    if h[0].lower() == input_ch.lower():
                        harem.insert(i, temp_inp)
                        break

        elif input_action == "r":
            response = input(f"Are you sure you want to remove {input_character} from your harem? [Y/N]\n").lower()

            if response == "y":
                for i, h in enumerate(harem):
                    if h[0].lower() == input_character.lower():
                        del harem[i]
                        break
            
            else : print("Action canceled \n")

        elif input_action == "s":
            for i, h in enumerate(harem):
                if h[0].lower() == input_character.lower():
                    ch_to_change = i
                    old_series = h[1]
            
            print(f"Current serie for {input_character} is {old_series}")
            new_serie = input(f"Write a new serie for {input_character}, [ESC] to exit: \n")
            if new_serie == "esc" : pass
            else:
                harem[ch_to_change][1] = new_serie


def generate_sm():
    sm = "$sm " 
    for c, s in harem:
        sm = sm + "$" + c
    print()
    print(sm)
    print()


def add_character():
    while True:
        new_character = input("Write character you want to add to your harem, use [ESC] to exit: \n")
        if new_character.lower() == "esc" : break
        new_serie = input("Serie of that character, use [ESC] to exit?: \n")
        if new_serie == "esc" : break
        input_action = input(f"Do you want to add {new_character} : {new_serie}? [Y/N]\n").lower()
        if input_action == "n" : break
        show_harem()
        input_ch = input(f"Write character from your harem, {new_character} will be put above in $sm command: \n"
                          "[LAST] for last position \n")
        if input_ch.lower() == "last":
            harem.append((new_character, new_serie))
        else:
            for i, h in enumerate(harem):
                if h[0].lower() == input_ch.lower():
                    harem.insert(i, (new_character, new_serie))
                    break


if __name__ == "__main__":
    
    user_input = input("Write command to use below, use [ESC] to exit, [HELP] for help: \n").lower()
    while user_input != "esc":
        
        if user_input == "help":
            help_command()
        if user_input == "harem":
            show_harem()
        if user_input == "fullharem":
            show_full_harem()
        if user_input == "sort":
            sort_harem()
        if user_input == "add":
            add_character()
        if user_input == "sm":
            generate_sm()
        
        user_input = input("Write another command or use [ESC] to exit, [HELP] for help: \n").lower()
    user_final = input("Save changes?: [Y/N] \n")
    if user_final == "y":
        with open("harem.txt", "w") as f:
            f.write("\n".join(f"{x[0]}\n{x[1]}" for x in harem))