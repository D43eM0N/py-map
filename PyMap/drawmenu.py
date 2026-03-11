import os

# ANSI Color Codes
G = "\033[92m"  # Green
C = "\033[96m"  # Cyan
W = "\033[0m"   # Reset
B = "\033[1m"   # Bold

def draw_menu():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    menu = f"""
{C}┌────────────────────────────────────────┐{W}
{G}{B}
     | < > |    PYMAP NETWORK    | < > |
    
      _____       __  __                
     |  __ \     |  \/  |               
     | |__) |   _| \  / | __ _ _ __     
     |  ___/ | | | |\/| |/ _` | '_ \    
     | |   | |_| | |  | | (_| | |_) |   
     |_|    \__, |_|  |_|\__,_| .__/    
             __/ |            | |       
            |___/             |_|       
{W}
{C}└────────────────────────────────────────┘{W}
{B}
  [1] [PingSweep Module] Scan LAN/Gather Information about Net
  [2] [Port Scan]
{W}
{C}──────────────────────────────────────────{W}
    """
    print(menu)
