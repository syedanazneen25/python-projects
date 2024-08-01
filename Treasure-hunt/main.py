logo = r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
'''

island = r'''
         |
         \ _ /
       -= (_) =-
         /   \         _\/_
           |           //o\  _\/_
    _____ _ __ __ ____ _ | __/o\\ _
  =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
   =- _=-=- -_=-=_,-"          |
    =- =- -=.--" 
'''

over = r'''
 ,adPPYba,  8b       d8  ,adPPYba, 8b,dPPYba,  
a8"     "8a `8b     d8' a8P_____88 88P'   "Y8   
8b       d8  `8b   d8'  8PP""""""" 88           
"8a,   ,a8"   `8b,d8'   "8b,   ,aa 88           
 `"YbbdP"'      "8"      `"Ybbd8"' 88  
'''

shark = r'''
        _________         .    .
       (..       \_    ,  |\  /|
        \       0  \  /|  \ \/ /
         \______    \/ |   \  /
            vvvv\    \ |   /  |
            \^^^^  ==   \_/   |
             `\_   ===    \.  |
             / /\_   \ /      |
             |/   \_  \|      /
                    \________/snd
'''

wolf = r'''
                        __
                             .d$$b
                           .' TO$;\
                          /  : TP._;
                         / _.;  :Tb|
                        /   /   ;j$j
                    _.-"       d$$$$
                  .' ..       d$$$$;
                 /  /P'      d$$$$P. |\
                /   "      .d$$$P' |\^"l
              .'           `T$P^"""""  :
          ._.'      _.'                ;
       `-.-".-'-' ._.       _.-"    .-"
     `.-" _____  ._              .-"
    -(.g$$$$$$$b.              .'
      ""^^T$$$P^)            .(:
        _/  -"  /.'         /:/;
     ._.'-'`-'  ")/         /;/;
  `-.-"..--""   " /         /  ;
 .-" ..--""        -'          :
 ..--""--.-"         (\      .-(\
   ..--""              `-\(\/;`
     _.                      :
                             ;`-
                            :\
                            ;  bug
'''

print("Welcome to Treasure Hunt!!")
print(logo)

path = input("Choose a path to go. Left or Right?\n").lower()

if path == "left":
    print("You have reached the end of the sea. There's an island in the middle of the sea.")
    print("Your goal is to find treasure on that island.")
    print(island)
    reach_way = input("Do you want to wait for the boat or swim to the island?\n").lower()
    if reach_way == "wait":
        print("Congrats! You've successfully reached the island, and there are three doors")
        door = input("Choose a door: Blue, Red, or Yellow?\n").lower()
        if door == "red":
            print("Game Over!! Wolf attack..")
            print(wolf)
            print(over)
        elif door == "yellow":
            print("You found nothing!! Game Over...")
            print(over)
        else:
            print("Wohooo!! You found the treasure.\nYou Won..")
    else:
        print("Ohhhh!! Shark attack...Game Over!")
        print(shark)
        print(over)   
else:
    print("Oops! Fell in a hole. Game Over!")
    print(over)
