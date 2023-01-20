from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import system
from time import sleep

system("color a")
system("python -m pip install -r requirements.txt")
system("python -m pip install --upgrade pip")
system("cls")

print(""" /$$   /$$           /$$                                                                  
| $$  | $$          | $$                                                                  
| $$  | $$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$ 
| $$$$$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$  | $$ /$$__  $$
| $$__  $$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/| $$  \ $$| $$$$$$$$| $$  | $$| $$  \__/
| $$  | $$| $$_____/| $$  | $$| $$_____/| $$      | $$  | $$| $$_____/| $$  | $$| $$      
| $$  | $$|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$|  $$$$$$/| $$      
|__/  |__/ \_______/|_______/  \_______/|__/       \____  $$ \_______/ \______/ |__/      
                                                   /$$  \ $$                              
                                                  |  $$$$$$/                              
                                                   \______/                               
""")

path = str(input("[Server] Enter your site directory path:\n>>>"))
print("\n[Server] initialization...")
pourcentage = 0
for i in range(100):
    pourcentage += 1
    anim = "█"
    for i in range(int(pourcentage / 5)):
        anim += "█"
    print(f"{pourcentage}% | {anim}", end="\r")
    sleep(0.025)

print("[Server] I'm ready.")

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=path, **kwargs)
server = HTTPServer
server(("0.0.0.0", 8080), Handler).serve_forever()