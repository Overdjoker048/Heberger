from http.server import SimpleHTTPRequestHandler, HTTPServer
from subprocess import run
from requests import get

print(""" /$$   /$$                       /$$    
| $$  | $$                      | $$    
| $$  | $$  /$$$$$$   /$$$$$$$ /$$$$$$  
| $$$$$$$$ /$$__  $$ /$$_____/|_  $$_/  
| $$__  $$| $$  \ $$|  $$$$$$   | $$    
| $$  | $$| $$  | $$ \____  $$  | $$ /$$
| $$  | $$|  $$$$$$/ /$$$$$$$/  |  $$$$/
|__/  |__/ \______/ |_______/    \___/  
""")

path = str(input("[Server] Enter your site directory path:\n>>>"))
try:
    port = int(input("[Server] Enter a port:\n>>>"))
    if 1000 < port < 65535:
        run(["powershell", "-Command", "python -m pip install -r requirements.txt"])
        run(["powershell", "-Command", "python -m pip install --upgrade pip"])
        run(["powershell", "-Command", f"Remove-NetFirewallRule -DisplayName 'Host'"])
        run(["powershell", "-Command", f"New-NetFirewallRule -DisplayName 'Host' -Profile 'Public' -Direction Inbound -Action Allow -Protocol TCP -LocalPort {port}"])
        run(["powershell", "-Command", f"New-NetFirewallRule -DisplayName 'Host' -Profile 'Public' -Direction Inbound -Action Allow -Protocol UDP -LocalPort {port}"])
        print("\n[Server] I'm ready.")
        print(f"[Server] Ip: {get('https://api.ipify.org').text}:{port}")
        class Handler(SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=path, **kwargs)

        HTTPServer(("0.0.0.0", port), Handler).serve_forever()
    else:
        print("[Server] The port must be between 1000 and 65535.")
except ValueError:
    print("[Server] The chosen port is not valid.")
