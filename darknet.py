"""
DARK-NET LOCATOR — cinematic terminal prop
-------------------------------------------
FOR FILM / SCREEN-PROP USE ONLY.
This tool performs NO real network access, tracking, or hacking of any kind.
All "results" are fictional placeholder data or randomly generated strings,
purely for visual effect on camera.
"""

import sys
import time
import os
import random
import shutil
from colorama import Fore, Back, Style, init

init(autoreset=True)

WIDTH = shutil.get_terminal_size((78, 20)).columns
WIDTH = max(60, min(WIDTH, 78))

# =====================================================================
# FICTIONAL MOCK DATA — all names / numbers / emails below are made up
# for the movie prop. None of it refers to a real person or device.
# =====================================================================
MOCK_EMAIL_DATA = {
    "agent.doe@example.com": {"Phone": "+91 90000 11111", "Device": "Fictional Model X1", "IMEI": "000011112222333", "Status": "AUTHENTICATED / ONLINE"},
    "ghost.user@example.com": {"Phone": "+91 90000 22222", "Device": "Fictional Model Z9", "IMEI": "000022223333444", "Status": "AUTHENTICATED / ONLINE"},
}

MOCK_PHONE_DATA = {
    "9876543210": {"Location": " Kochi Sector 3, Kerala", "Status": "ENCRYPTED / ACTIVE", "ISP": "Airtel 5G Mesh", "IP": "192.168.1.104"},
    "8289804072": {"Location": "Chala, Kannur, Kerala", "Status": "ENCRYPTED / ACTIVE", "ISP": "Jio 5G Node", "IP": "192.168.1.105"},
    "7012933061": {"Location": "Chala, Kannur, Kerala", "Status": "ENCRYPTED / ACTIVE", "ISP": "Jio 5G Node", "IP": "192.168.5.106"},
    "9605976244": {"Location": "Chala, Kannur, Kerala", "Status": "ENCRYPTED / ACTIVE", "ISP": "Airtel", "IP": "192.168.5.107"},
    "9633417318": {"Location": "Chala, Kannur, Kerala", "Status": "ENCRYPTED / ACTIVE", "ISP": "Airtel 5G Mesh", "IP": "192.168.1.109"},
    "9400195146": {"Location": "Chala, Kannur, Kerala", "Status": "ENCRYPTED / ACTIVE", "ISP": "Jio 5G Node", "IP": "192.168.1.113"},
    "9400794072": {"Location": "Chala, Kannur, Kerala", "Status": "ENCRYPTED / ACTIVE", "ISP": "BSNL Quantum Fiber", "IP": "192.168.1.114"},
    "9745097282": {"Location": "karandakkad,kasaragod, Kerala", "Status": "ENCRYPTED / ACTIVE", "ISP": "Airtel 5G Mesh", "IP": "192.168.1.115"},
}

MOCK_IP_DATA = {
    "192.168.1.104": {"Gateway": "RED-ROUTER NODE #804", "Location": "Fictional City Sector 4", "Status": "FIREWALL BYPASSED"},
}

MOCK_FORENSICS_DATA = {
    "dump.bin": {"Artifacts": "450 MB RAW DATA RECOVERED", "Messages": "128 Deleted SMS Restored", "Key": "AES-256 MASTER KEY ENGAGED"},
}

# Dynamic random arrays — clearly fictional place / device names
LOCATIONS = [" Kannur", "Kozhikode City", "kerala"]
ISPS = ["Jio 5G Alpha Node", "Airtel 5G Mesh", "Vi 4G Satellite Bridge", "BSNL Quantum Fiber"]
DEVICES = ["Android Rogue Terminal", "Infinix Custom Kernel", "Encrypted Linux Phone", "Samsung Cyber-Node", "iOS Jailbreak Device", "Pixel Quantum Phone", "OnePlus Stealth Edition", "Redmi Shadow Device", "Nokia Secure Comm", "Motorola Phantom Device"]


def get_random_ip():
    return f"10.{random.randint(10, 99)}.{random.randint(1, 254)}.{random.randint(1, 254)}"


# =====================================================================
# VISUAL HELPERS
# =====================================================================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def line(char="─", color=Fore.GREEN):
    print(color + char * WIDTH)


def center(text, color=Fore.WHITE):
    print(color + text.center(WIDTH))


def type_effect(text, delay=0.012, color=Fore.GREEN):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def glitch_text(text, cycles=6, delay=0.03, color=Fore.GREEN):
    """Flickers the text through glitch characters before settling."""
    glitch_chars = "!<>-_\\/[]{}—=+*^?#@%$"
    for _ in range(cycles):
        scrambled = "".join(
            random.choice(glitch_chars) if random.random() < 0.35 and c != " " else c
            for c in text
        )
        sys.stdout.write("\r" + color + scrambled)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\r" + color + text + " " * 4 + "\n")
    sys.stdout.flush()


def matrix_rain(duration=1.0, density=0.05):
    """Brief matrix-style rain burst used during boot."""
    chars = "01ABCDEF#$%&*"
    cols = WIDTH
    end_time = time.time() + duration
    while time.time() < end_time:
        row = "".join(
            random.choice(chars) if random.random() < density else " "
            for _ in range(cols)
        )
        print(Fore.GREEN + Style.DIM + row)
        time.sleep(0.02)


def boot_sequence():
    clear()
    matrix_rain(duration=0.6, density=0.06)
    glitch_text("  BOOTSTRAPPING DARK-NET LOCATOR KERNEL...", color=Fore.GREEN)
    boot_lines = [
        "Mounting encrypted volumes",
        "Loading proxy chain modules",
        "Calibrating telemetry receivers",
        "Handshaking with master node",
    ]
    for b in boot_lines:
        sys.stdout.write(Fore.CYAN + f"  [·] {b}")
        sys.stdout.flush()
        time.sleep(0.35)
        print(Fore.GREEN + "  [OK]")
    time.sleep(0.3)


def progress_bar(label, width=44, steps=25, delay=0.03, color=Fore.CYAN):
    for i in range(steps + 1):
        pct = int((i / steps) * 100)
        filled = int((i / steps) * width)
        bar = "█" * filled + "░" * (width - filled)
        sys.stdout.write(f"\r{color}[+] {label}: [{bar}] {pct:3d}%")
        sys.stdout.flush()
        time.sleep(delay)
    print()


def cinematic_loader(target_name):
    print(Fore.CYAN + f"\n[*] INITIATING TARGET ANALYSIS: [{target_name}]")
    line("─", Fore.YELLOW)

    steps = [
        "Connecting to proxy relay chain (4 hops)",
        "Bypassing perimeter firewall",
        "Establishing encrypted tunnel",
        "Relaying request through gateway node",
        "Cross-referencing telemetry headers",
        "Triangulating coordinate estimate",
        "Querying identity index",
        "Verifying session token",
        "Reassembling data fragments",
        "Confirming payload integrity",
    ]

    for idx, step in enumerate(steps, 1):
        time.sleep(0.22)
        dots = "." * random.randint(1, 3)
        sys.stdout.write(f"\r{Fore.RED} [{idx:02d}/{len(steps):02d}]{Fore.WHITE} {step}{dots}")
        sys.stdout.flush()
        time.sleep(0.18)
        print(Fore.GREEN + "  [OK]" + " " * 10)

    line("─", Fore.YELLOW)
    progress_bar("DECRYPTION PROGRESS", steps=30, delay=0.025)
    print(f"\n{Fore.GREEN}[✔] TARGET ACQUIRED — DATA READY\n")


def firewall_lockdown_warning():
    """Simulated 'Google firewall detected & locked the system' alert."""
    print()
    time.sleep(0.3)
    glitch_text("  [!!] ANOMALY DETECTED ON MAIL RELAY  [!!]", color=Fore.RED + Style.BRIGHT)
    time.sleep(0.2)
    line("═", Fore.RED)
    center("⚠  GOOGLE SECURITY FIREWALL — INTRUSION DETECTED  ⚠", Fore.RED + Style.BRIGHT)
    line("═", Fore.RED)
    warn_lines = [
        "Suspicious access pattern flagged on mail gateway...",
        "Google Account Defense System engaged...",
        "Tracing back intrusion signature...",
        "Countermeasures deployed by remote firewall...",
    ]
    for w in warn_lines:
        sys.stdout.write(Fore.YELLOW + f"  [!] {w}")
        sys.stdout.flush()
        time.sleep(0.35)
        print(Fore.RED + "  [BLOCKED]")
    time.sleep(0.3)
    center("🔒  SYSTEM ACCESS LOCKED BY REMOTE FIREWALL  🔒", Fore.RED + Style.BRIGHT)
    line("═", Fore.RED)
    print()


def end_session():
    print()
    line("─", Fore.RED)
    center("[!] PROCESS COMPLETE — SESSION TERMINATED", Fore.RED)
    line("─", Fore.RED)


def result_block(title, rows, value_color=Fore.GREEN):
    """rows: list of (label, value, color) tuples"""
    print()
    print(Fore.MAGENTA + Style.BRIGHT + f"  ┌{'─' * (WIDTH - 4)}┐")
    center(title.upper(), Fore.MAGENTA + Style.BRIGHT)
    print(Fore.MAGENTA + Style.BRIGHT + f"  ├{'─' * (WIDTH - 4)}┤")
    label_w = max(len(r[0]) for r in rows) + 2
    for label, value, color in rows:
        print(Fore.YELLOW + f"    {label.ljust(label_w)}: " + color + str(value))
    print(Fore.MAGENTA + Style.BRIGHT + f"  └{'─' * (WIDTH - 4)}┘")


def emblem():
    print(Fore.RED + Style.BRIGHT + r"""
%%%%#######%%%%##%###########*****##**######**########*##################%%%%%%%
%%###########%%%%%#############*******#*************##*****###########%%##%%%%%%
%##############%%%%%############*******************###*******##########%####%%%%
#%################################*+****************####*****################%%%
################################+-::::::::::::-=****####******##################
##########################*=-::::::::::::::......:::-+*#******##################
#################%%%%%+-----------::::::::.............:******##################
###################*-------------:::::::::.:.........::.:-#*****################
#################*==---------------::::::::..........::::::*****################
##***##########*++==------------------::::::..........:::::-++***#############%%
##****#######*++===---===---:------=---::::::::::...........=*+++**###########%%
###*****###*+++++++++++**##*+-:---===--::::-*#+-:::..:.:::=::=****++****#######%
##*******#*++++++++++*#%*#####=::-=+=-:::--=#%##+*:.:#+::-%#*=:+#*#****######%%#
##********+++=+==+==++#%%#####%-::-::+%%%%%%%%%%%%%*#-.=*#@@@@@@++********######
##*******+++++++=====+*####**##+-=--%%%@%%%%%%%@#**=#*-:*@@@@@%%%+*###****#*####
##*******+*++++++++==++*+**#***+==+%@@@%%%%%#####*#=*%#=-:-*%%%%%#######*****#*#
*********++++++++++==+++++++***=---#@@@%%%#####%++#-+*#%=*%**####+########******
*********+++++=====+++++*++=++++-=-:%@%%%##*###*++::+=++=@%@*+**#+*###########**
*******#***++++=++++++*++***++*=+==::=#***#*#**-:::--*+%@%%%%-:-=+-+######%%%%#+
*******##***+++++++++++*#*****##++==-:::::.:.::::::-==*%%%%##=:+=*--+###%%%%%%%%
********#***++++++++*++*#****+==+**+-::-*=*-=%#%*+==*++##**+*%=+*#-:-##%%%%%%%%%
*********#*********+***####++*+=**+==:=--:=#*--=#***-=====+=:=:--=---#%%%%%%%%#%
*********###*********##%%*++##==#*+++-:----::::-+#==-:-==+=--===:--%#*%%%%%%%##%
**********##*****##*+++#**%%**%%**+*%#*+#%#=:::-+*++==:**=+--::--:*##%%%%%%%%%%%
**********###++++*##*##%#*#@@@@@@@%%@@@@@@%%#*=:---#=+=:-+--=:+-:-.*#%%%%%%%%##%
##*********#%#*+**##%%@@%*%%@@@@@#%+#@@%%%%###%%-***#+#=-#-.%-.=:::=############
***********#%%##**#%@%%%%%**##%%%###=%%#*%%%#**#*=#++**#=---+**%%#@+++++++++++++
***********##%%%#%%%%%%%%%%++#####*#+#%*+%%*%%*+#==@=#%%@@*%=#-*=+-#%%%%%%%%%%%%
****##########%%%%##*#%%%%%%*+#*#+##+=*%*###+%*#%%%#%*##*@=%*%*#+==+%%%%%%%%%%%%
******#########@%****+*#%%%%@*+*#++#*+=-%#%%@#%%#%#+##+@#*#==-=--+-=************
********########@%%##%**%@%%%%*+%#+*+**+-*@@#%@%#%%#+=-==---::-::-:-#%%%%#######
********#########%@@@@@@@@%%#%%*+%+%+%%*++-*@%#*##*-====-:--:::::-:-=***********
***********########%@%@@%%%%%%#%+**#+%@#**+=-*#====+*%#+--+*=--::::==+**********
**##*******#########%@@%%##%@%#%%#++*+#+#**++=-==+##+=+==---::::-=--:-#%########
###############%%%%%%%%@%%####%%%@#*++++*+*++======+=-----=++**%####%###########
################%%%%%%%@@@@@@@@@@@@@@#*******#*#**+++++++++*%%####%#############
###################%%%%%%%%%%%%%%%%%%##**###################%%##################
################%%%%%%%%%%%%%%%%%%####**####****************####################
################%%%%%%%%%%%%%%%%%%##*#######*******#***++==+=====++++*#%%%%%%%%%
##########################%%%%%######%%###**###**#******+++++=====++*#%%%%%%%%%%

""")


def header():
    line("═", Fore.RED)
    emblem()
    print(Fore.GREEN + Style.BRIGHT + r"""
  ██████╗  █████╗ ██████╗ ██╗  ██╗   ███╗   ██╗███████╗████████╗
  ██╔══██╗██╔══██╗██╔══██╗██║  ██║   ████╗  ██║██╔════╝╚══██╔══╝
  ██║  ██║███████║██████╔╝███████║   ██╔██╗ ██║█████╗     ██║
  ██║  ██║██╔══██║██╔══██╗██╔══██║   ██║╚██╗██║██╔══╝     ██║
  ██████╔╝██║  ██║██║  ██║██║  ██║   ██║ ╚████║███████╗   ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝
""")
    center("D A R K - N E T   L O C A T O R   v5.0", Fore.CYAN + Style.BRIGHT)
    center("—  DEVELOPED BY Sreenand K —", Fore.RED + Style.BRIGHT)
    line("═", Fore.RED)
    center("[⚠️] DANGER: SENSITIVE NETWORK INFILTRATOR ACTIVE", Fore.RED + Style.BRIGHT)
    center("[!] USE WITH EXTREME CAUTION. TRAFFIC IS ENCRYPTED VIA RED-ROUTER NODE.", Fore.RED)
    center("[!] ANY UNBALANCED PAYLOAD MAY CAUSE PERMANENT HARDWARE BURNOUT.", Fore.RED)
    print()


def clock_str():
    return time.strftime("%H:%M:%S")


def menu():
    clear()
    header()
    options = [
        ("1", "Email-Based Device Lookup"),
        ("2", "Phone Number Tracer"),
        ("3", "IP Address Locator"),
        ("4", "Digital Forensics & Dump Reader"),
        ("0", "Exit Framework"),
    ]
    for key, label in options:
        color = Fore.RED if key == "0" else Fore.WHITE
        print(color + f"   [{key}]  {label}")
    print()
    line("─", Fore.GREEN)
    print(Fore.GREEN + f"  SYSTEM TIME: {clock_str()}" + Fore.WHITE)
    return input(Fore.YELLOW + Style.BRIGHT + "\n  DARK-NET-LOCATOR> " + Fore.WHITE)


# =====================================================================
# PAGES
# =====================================================================
def email_tracker():
    clear()
    header()
    center("EMAIL-BASED DEVICE LOOKUP", Fore.CYAN + Style.BRIGHT)
    print()
    email = input(Fore.YELLOW + "  [?] Enter Target Email Address : " + Fore.WHITE)
    cinematic_loader(email)

    if email in MOCK_EMAIL_DATA:
        data = MOCK_EMAIL_DATA[email]
    else:
        data = {
            "Phone": f"+91 {random.randint(70000, 99999)} {random.randint(10000, 99999)}",
            "Device": random.choice(DEVICES),
            "IMEI": str(random.randint(100000000000000, 999999999999999)),
            "Status": "AUTHENTICATED / ONLINE",
        }

    result_block("Device Profile", [
        ("Target Device", data["Device"], Fore.GREEN),
        ("IMEI Code", data["IMEI"], Fore.GREEN),
        ("Linked Mobile", data["Phone"], Fore.CYAN),
        ("Cloud Status", data["Status"], Fore.RED),
    ])
    firewall_lockdown_warning()
    end_session()


def phone_tracker():
    clear()
    header()
    center("PHONE NUMBER TRACER", Fore.CYAN + Style.BRIGHT)
    print()
    num = input(Fore.YELLOW + "  [?] Enter Mobile Number (+91) : " + Fore.WHITE)
    cinematic_loader(num)

    if num in MOCK_PHONE_DATA:
        data = MOCK_PHONE_DATA[num]
    else:
        data = {
            "Location": random.choice(LOCATIONS),
            "Status": "ENCRYPTED / ACTIVE",
            "ISP": random.choice(ISPS),
            "IP": get_random_ip(),
        }

    result_block("Signal Trace", [
        ("Target Location", data["Location"], Fore.GREEN),
        ("Carrier Node", data["ISP"], Fore.CYAN),
        ("Current IP", data["IP"], Fore.GREEN),
        ("Cellular Status", data["Status"], Fore.RED),
    ])
    end_session()


def ip_tracker():
    clear()
    header()
    center("IP ADDRESS LOCATOR", Fore.CYAN + Style.BRIGHT)
    print()
    ip = input(Fore.YELLOW + "  [?] Enter IPv4 / IPv6 Address : " + Fore.WHITE)
    cinematic_loader(ip)

    if ip in MOCK_IP_DATA:
        data = MOCK_IP_DATA[ip]
    else:
        data = {
            "Gateway": f"RED-ROUTER NODE #{random.randint(100, 999)}",
            "Location": random.choice(LOCATIONS),
            "Status": "FIREWALL BYPASSED",
        }

    result_block("Network Trace", [
        ("IP Node", ip, Fore.GREEN),
        ("Gateway Bridge", data["Gateway"], Fore.CYAN),
        ("Location Region", data["Location"], Fore.GREEN),
        ("Infiltration", data["Status"], Fore.RED),
    ])
    end_session()


def forensics():
    clear()
    header()
    center("DIGITAL FORENSICS & DUMP READER", Fore.CYAN + Style.BRIGHT)
    print()
    dump = input(Fore.YELLOW + "  [?] Select Device / Memory Dump File : " + Fore.WHITE)
    cinematic_loader(dump)

    if dump in MOCK_FORENSICS_DATA:
        data = MOCK_FORENSICS_DATA[dump]
    else:
        data = {
            "Artifacts": f"{random.randint(100, 900)} MB RAW ARTIFACTS RECOVERED",
            "Messages": f"{random.randint(50, 300)} Deleted Items Restored",
            "Key": "AES-256 MASTER KEY ENGAGED",
        }

    result_block("Extraction Report", [
        ("Extraction Log", data["Artifacts"], Fore.GREEN),
        ("Deleted Items", data["Messages"], Fore.GREEN),
        ("Decryption Key", data["Key"], Fore.RED),
    ])
    end_session()


def run():
    boot_sequence()
    while True:
        choice = menu()
        if choice == '1':
            email_tracker()
        elif choice == '2':
            phone_tracker()
        elif choice == '3':
            ip_tracker()
        elif choice == '4':
            forensics()
        elif choice == '0':
            print()
            glitch_text("  SHUTTING DOWN DARK-NET LOCATOR PROTOCOL...", color=Fore.RED)
            time.sleep(0.4)
            break
        else:
            print(Fore.RED + "\n  [!] Invalid selection.")
        input(Fore.WHITE + "\n  Press [ENTER] to return to Main Menu...")


if __name__ == "__main__":
    run()