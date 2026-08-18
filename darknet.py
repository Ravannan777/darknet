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

WIDTH = shutil.get_terminal_size((100, 24)).columns
WIDTH = max(80, min(WIDTH, 110))

# =====================================================================
# FICTIONAL MOCK DATA — all names / numbers / emails below are made up
# for the movie prop. None of it refers to a real person or device.
# =====================================================================
MOCK_EMAIL_DATA = {
    "agent.doe@example.com": {
        "Phone": "+91 90000 11111",
        "Device": "Fictional Model X1",
        "IMEI": "000011112222333",
        "Status": "AUTHENTICATED / ONLINE",
    },
    "ghost.user@example.com": {
        "Phone": "+91 90000 22222",
        "Device": "Fictional Model Z9",
        "IMEI": "000022223333444",
        "Status": "AUTHENTICATED / ONLINE",
    },
}

MOCK_PHONE_DATA = {
    "9876543210": {"Location": "Kochi Sector 3, Kerala",   "Status": "ENCRYPTED / ACTIVE", "ISP": "Airtel 5G Mesh",    "IP": "192.168.1.104"},
    "8289804072": {"Location": "Chala, Kannur, Kerala",    "Status": "ENCRYPTED / ACTIVE", "ISP": "Jio 5G Node",       "IP": "192.168.1.105"},
    "7012933061": {"Location": "Chala, Kannur, Kerala",    "Status": "ENCRYPTED / ACTIVE", "ISP": "Jio 5G Node",       "IP": "192.168.5.106"},
    "9605976244": {"Location": "Chala, Kannur, Kerala",    "Status": "ENCRYPTED / ACTIVE", "ISP": "Airtel",            "IP": "192.168.5.107"},
    "9633417318": {"Location": "Chala, Kannur, Kerala",    "Status": "ENCRYPTED / ACTIVE", "ISP": "Airtel 5G Mesh",    "IP": "192.168.1.109"},
    "9400195146": {"Location": "Chala, Kannur, Kerala",    "Status": "ENCRYPTED / ACTIVE", "ISP": "Jio 5G Node",       "IP": "192.168.1.113"},
    "9400794072": {"Location": "Chala, Kannur, Kerala",    "Status": "ENCRYPTED / ACTIVE", "ISP": "Jio 5G Node",       "IP": "192.168.1.114"},
}

MOCK_IP_DATA = {
    "192.168.1.104": {
        "Gateway": "RED-ROUTER NODE #804",
        "Location": "Fictional City Sector 4",
        "Status": "FIREWALL BYPASSED",
    },
}

MOCK_FORENSICS_DATA = {
    "dump.bin": {
        "Artifacts": "450 MB RAW DATA RECOVERED",
        "Messages": "128 Deleted SMS Restored",
        "Key": "AES-256 MASTER KEY ENGAGED",
    },
}

LOCATIONS = ["Kannur", "Kozhikode City", "Kerala"]
ISPS      = ["Jio 5G Alpha Node", "Airtel 5G Mesh", "Vi 4G Satellite Bridge", "BSNL Quantum Fiber"]
DEVICES   = [
    "Android Rogue Terminal", "Infinix Custom Kernel",  "Encrypted Linux Phone",
    "Samsung Cyber-Node",     "iOS Jailbreak Device",   "Pixel Quantum Phone",
    "OnePlus Stealth Edition","Redmi Shadow Device",     "Nokia Secure Comm",
    "Motorola Phantom Device",
]


def get_random_ip():
    return f"10.{random.randint(10,99)}.{random.randint(1,254)}.{random.randint(1,254)}"


# =====================================================================
#  VISUAL HELPERS
# =====================================================================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def line(char="─", color=Fore.GREEN):
    print(color + char * WIDTH)


def dline(color=Fore.RED):
    print(color + "═" * WIDTH)


def center(text, color=Fore.WHITE):
    print(color + text.center(WIDTH))


def type_effect(text, delay=0.010, color=Fore.GREEN):
    for ch in text:
        sys.stdout.write(color + ch + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def glitch_text(text, cycles=8, delay=0.025, color=Fore.GREEN):
    glitch_chars = "!<>-_\\/[]{}—=+*^?#@%$█▓▒░"
    for _ in range(cycles):
        scrambled = "".join(
            random.choice(glitch_chars) if random.random() < 0.40 and ch != " " else ch
            for ch in text
        )
        sys.stdout.write("\r" + color + Style.BRIGHT + scrambled)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\r" + color + Style.BRIGHT + text + "    \n")
    sys.stdout.flush()


def matrix_rain(duration=1.2, density=0.07):
    chars = "01アイウエオカキクケコABCDEF#$%&*█▓░"
    cols  = WIDTH
    end   = time.time() + duration
    bright_rows = 0
    while time.time() < end:
        bright_rows = (bright_rows + 1) % 4
        row = "".join(
            (Style.BRIGHT if random.random() < 0.15 else Style.DIM) + random.choice(chars)
            if random.random() < density else " "
            for _ in range(cols)
        )
        print(Fore.GREEN + row)
        time.sleep(0.018)


def hex_dump_flash(lines=6):
    """Quick scrolling hex-dump effect."""
    for _ in range(lines):
        addr  = f"0x{random.randint(0x1000, 0xFFFF):04X}"
        chunk = " ".join(f"{random.randint(0,255):02X}" for _ in range(16))
        ascii_= "".join(chr(random.randint(33,126)) if random.random()<0.6 else "." for _ in range(16))
        print(Fore.GREEN + Style.DIM + f"  {addr}  {chunk}  |{ascii_}|")
        time.sleep(0.04)


def boot_sequence():
    clear()
    matrix_rain(duration=0.8, density=0.07)
    print()
    glitch_text("  ██ BOOTSTRAPPING DARK-NET LOCATOR KERNEL ██", color=Fore.GREEN)
    print()
    boot_lines = [
        ("Mounting encrypted volumes",                 Fore.CYAN),
        ("Loading 7-hop proxy chain modules",          Fore.CYAN),
        ("Calibrating sub-orbital telemetry receiver", Fore.CYAN),
        ("Handshaking with RED-ROUTER master node",    Fore.CYAN),
        ("Initialising AES-512 cipher engine",         Fore.CYAN),
        ("Injecting stealth packet headers",           Fore.YELLOW),
        ("Dark-net bridge authenticated",              Fore.GREEN),
    ]
    for label, col in boot_lines:
        filled = random.randint(34, 44)
        bar    = "█" * filled + "░" * (44 - filled)
        sys.stdout.write(col + f"  [·] {label}  [{bar}]")
        sys.stdout.flush()
        time.sleep(random.uniform(0.20, 0.45))
        print(Fore.GREEN + Style.BRIGHT + "  ✔")
    time.sleep(0.25)
    hex_dump_flash(4)
    print()


def progress_bar(label, width=50, steps=30, delay=0.028, color=Fore.CYAN):
    for i in range(steps + 1):
        pct    = int((i / steps) * 100)
        filled = int((i / steps) * width)
        bar    = "█" * filled + "░" * (width - filled)
        speed  = random.randint(800, 9999)
        sys.stdout.write(
            f"\r{color}[+] {label}: [{Fore.GREEN}{bar}{color}] "
            f"{Fore.WHITE}{pct:3d}%  {Fore.YELLOW}{speed} KB/s"
        )
        sys.stdout.flush()
        time.sleep(delay)
    print()


def cinematic_loader(target_name):
    print()
    line("─", Fore.YELLOW)
    print(Fore.CYAN + Style.BRIGHT + f"  [*] INITIATING TARGET ANALYSIS  »  " + Fore.WHITE + f"[ {target_name} ]")
    line("─", Fore.YELLOW)

    steps = [
        ("Connecting to 7-hop proxy relay chain",     Fore.CYAN),
        ("Bypassing perimeter firewall layer",         Fore.CYAN),
        ("Establishing AES-encrypted dark tunnel",     Fore.CYAN),
        ("Relaying request via RED-ROUTER node",       Fore.CYAN),
        ("Cross-referencing telemetry packet headers", Fore.CYAN),
        ("Triangulating geo-coordinate estimate",      Fore.YELLOW),
        ("Querying shadow identity index",             Fore.YELLOW),
        ("Verifying encrypted session token",          Fore.YELLOW),
        ("Reassembling fragmented data payload",       Fore.GREEN),
        ("Confirming payload integrity hash",          Fore.GREEN),
    ]

    for idx, (step, col) in enumerate(steps, 1):
        dots = "." * random.randint(1, 4)
        sys.stdout.write(
            f"\r{Fore.RED} [{idx:02d}/{len(steps):02d}] {col}{step}{Fore.WHITE}{dots}"
            + " " * 10
        )
        sys.stdout.flush()
        time.sleep(random.uniform(0.18, 0.28))
        print(Fore.GREEN + Style.BRIGHT + "  [✔ OK]" + " " * 6)

    line("─", Fore.YELLOW)
    progress_bar("PAYLOAD DECRYPTION", width=50, steps=32, delay=0.022)
    print(f"\n{Fore.GREEN + Style.BRIGHT}  [✔] TARGET ACQUIRED — PAYLOAD READY\n")


# =====================================================================
#  FIREWALL LOCKDOWN WARNING — call after result_block() in email_tracker
# =====================================================================
def firewall_lockdown_warning():
    """Simulated Google-firewall counter-intrusion cinematic alert."""
    time.sleep(0.4)
    print()
    # ── glitch burst ───────────────────────────────────────────────
    glitch_text("  [!!] ANOMALY DETECTED ON MAIL RELAY NODE  [!!]", color=Fore.RED + Style.BRIGHT)
    time.sleep(0.15)

    # ── warning banner ─────────────────────────────────────────────
    dline(Fore.RED)
    print()
    center("▓▓  GOOGLE ACCOUNT DEFENSE SYSTEM — INTRUSION DETECTED  ▓▓",
           Fore.RED + Style.BRIGHT)
    center("Automated Countermeasure Protocol v9.3 Engaged",
           Fore.YELLOW + Style.BRIGHT)
    print()
    dline(Fore.RED)

    # ── countermeasure log ─────────────────────────────────────────
    warn_steps = [
        ("Suspicious packet signature flagged on mail gateway",    Fore.YELLOW, "[FLAGGED ]"),
        ("Origin IP routed through illegal proxy detected",        Fore.YELLOW, "[DETECTED]"),
        ("Google Account Defense System — ALERT RAISED",          Fore.RED,    "[ALERT   ]"),
        ("Tracing back intrusion vector — source triangulated",   Fore.RED,    "[TRACING ]"),
        ("Remote firewall countermeasures deployed",              Fore.RED,    "[DEPLOYED]"),
        ("Session credentials revoked by remote node",            Fore.RED,    "[REVOKED ]"),
        ("Reporting incident to Cyber-Crime Division",            Fore.RED,    "[REPORTED]"),
    ]
    for msg, col, tag in warn_steps:
        sys.stdout.write(col + f"  [!] {msg}  ")
        sys.stdout.flush()
        time.sleep(random.uniform(0.28, 0.45))
        print(Fore.RED + Style.BRIGHT + tag)

    time.sleep(0.3)
    print()
    dline(Fore.RED)

    # ── LOCKED message with glitch ──────────────────────────────────
    glitch_text("  🔒  ACCESS BLOCKED — SYSTEM LOCKED BY REMOTE FIREWALL  🔒",
                color=Fore.RED + Style.BRIGHT)
    center("ALL FURTHER REQUESTS WILL BE TRACED AND LOGGED", Fore.YELLOW + Style.BRIGHT)
    dline(Fore.RED)
    print()

    # ── trace-back countdown ────────────────────────────────────────
    print(Fore.RED + Style.BRIGHT + "  [!] INCOMING TRACE-BACK DETECTED — ABORT IN:")
    for n in range(5, 0, -1):
        bar = "█" * (n * 8) + "░" * ((5 - n) * 8)
        sys.stdout.write(
            f"\r  {Fore.RED}[{Fore.WHITE}{bar}{Fore.RED}]  {Fore.WHITE + Style.BRIGHT}{n}s REMAINING  "
        )
        sys.stdout.flush()
        time.sleep(0.9)
    print()
    print()
    glitch_text("  CONNECTION SEVERED — DARK-NET SESSION TERMINATED BY FIREWALL",
                color=Fore.RED + Style.BRIGHT)
    print()


# =====================================================================
#  SHARED UI BLOCKS
# =====================================================================
def end_session():
    print()
    dline(Fore.RED)
    center("[!] PROCESS COMPLETE — SESSION LOGS PURGED — TUNNEL CLOSED", Fore.RED + Style.BRIGHT)
    dline(Fore.RED)


def result_block(title, rows, value_color=Fore.GREEN):
    print()
    inner = WIDTH - 6
    tl, tr, bl, br = "╔", "╗", "╚", "╝"
    ml, mr         = "╠", "╣"
    hl, vl         = "═", "║"

    print(Fore.MAGENTA + Style.BRIGHT + f"  {tl}{hl * (inner + 2)}{tr}")
    title_line = (" " + title.upper() + " ").center(inner + 2, hl)
    print(Fore.MAGENTA + Style.BRIGHT + f"  {vl}{title_line}{vl}")
    print(Fore.MAGENTA + Style.BRIGHT + f"  {ml}{hl * (inner + 2)}{mr}")

    label_w = max(len(r[0]) for r in rows) + 2
    for label, value, color in rows:
        left  = Fore.YELLOW + f"    {label.ljust(label_w)}"
        right = color + Style.BRIGHT + str(value)
        sep   = Fore.WHITE + "  »  "
        # pad to box width
        content = left + sep + right
        raw_len = len(label.ljust(label_w)) + len("  »  ") + len(str(value)) + 4
        pad = " " * max(0, inner - raw_len)
        print(Fore.MAGENTA + Style.BRIGHT + f"  {vl}" + content + pad + Fore.MAGENTA + Style.BRIGHT + f" {vl}")

    print(Fore.MAGENTA + Style.BRIGHT + f"  {bl}{hl * (inner + 2)}{br}")


def header():
    dline(Fore.RED)
    print(Fore.GREEN + Style.BRIGHT + r"""
  ██████╗  █████╗ ██████╗ ██╗  ██╗    ███╗   ██╗███████╗████████╗
  ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ████╗  ██║██╔════╝╚══██╔══╝
  ██║  ██║███████║██████╔╝█████╔╝     ██╔██╗ ██║█████╗     ██║
  ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║╚██╗██║██╔══╝     ██║
  ██████╔╝██║  ██║██║  ██║██║  ██╗    ██║ ╚████║███████╗   ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝
""")
    center("D A R K - N E T   L O C A T O R   v 5 . 0", Fore.CYAN  + Style.BRIGHT)
    center("━━━━━━  D E V E L O P E D   B Y   S R E E N A N D   K  ━━━━━━", Fore.RED   + Style.BRIGHT)
    dline(Fore.RED)
    center("[ ⚠ ]  SENSITIVE NETWORK INFILTRATOR — AUTHORISED USE ONLY  [ ⚠ ]",
           Fore.RED    + Style.BRIGHT)
    center("[ ! ]  TRAFFIC ENCRYPTED VIA RED-ROUTER 7-HOP PROXY CHAIN",
           Fore.YELLOW + Style.BRIGHT)
    center("[ ! ]  UNBALANCED PAYLOAD MAY CAUSE PERMANENT HARDWARE BURNOUT",
           Fore.YELLOW)
    dline(Fore.RED)
    print()


def clock_str():
    return time.strftime("%Y-%m-%d  %H:%M:%S")


def menu():
    clear()
    header()
    options = [
        ("1", "Email-Based Device Lookup",         Fore.WHITE),
        ("2", "Phone Number Tracer",               Fore.WHITE),
        ("3", "IP Address Locator",                Fore.WHITE),
        ("4", "Digital Forensics & Dump Reader",   Fore.WHITE),
        ("0", "Exit Framework",                    Fore.RED),
    ]
    line("─", Fore.GREEN)
    print(Fore.GREEN + Style.DIM + f"  SYSTEM CLOCK : {clock_str()}")
    print(Fore.RED   + Style.DIM + f"  RED-ROUTER   : NODE #804  |  STATUS: ACTIVE  |  HOPS: 7")
    line("─", Fore.GREEN)
    print()
    for key, label, col in options:
        arrow = "▶" if key != "0" else "✖"
        print(col + Style.BRIGHT + f"     [{key}]  {arrow}  {label}")
    print()
    line("─", Fore.GREEN)
    return input(Fore.YELLOW + Style.BRIGHT + "\n  DARK-NET-LOCATOR ▸ " + Fore.WHITE)


# =====================================================================
#  PAGES
# =====================================================================
def email_tracker():
    clear()
    header()
    center("━━  EMAIL-BASED DEVICE LOOKUP  ━━", Fore.CYAN + Style.BRIGHT)
    print()
    email = input(Fore.YELLOW + "  [?] Enter Target Email Address : " + Fore.WHITE)
    cinematic_loader(email)

    if email in MOCK_EMAIL_DATA:
        data = MOCK_EMAIL_DATA[email]
    else:
        data = {
            "Phone":  "",
            "Device": "",
            "IMEI":   "",
            "Status": "",
        }

    result_block("Device Profile", [
        ("Target Device",  data["Device"], Fore.GREEN),
        ("IMEI Code",      data["IMEI"],   Fore.GREEN),
        ("Linked Mobile",  data["Phone"],  Fore.CYAN),
        ("Cloud Status",   data["Status"], Fore.RED),
    ])

    # ─── FIREWALL WARNING fires here, after results are shown ──────
    firewall_lockdown_warning()
    # ───────────────────────────────────────────────────────────────

    end_session()


def phone_tracker():
    clear()
    header()
    center("━━  PHONE NUMBER TRACER  ━━", Fore.CYAN + Style.BRIGHT)
    print()
    num = input(Fore.YELLOW + "  [?] Enter Mobile Number (+91) : " + Fore.WHITE)
    cinematic_loader(num)

    if num in MOCK_PHONE_DATA:
        data = MOCK_PHONE_DATA[num]
    else:
        data = {
            "Location": random.choice(LOCATIONS),
            "Status":   "ENCRYPTED / ACTIVE",
            "ISP":      random.choice(ISPS),
            "IP":       get_random_ip(),
        }

    result_block("Signal Trace", [
        ("Target Location", data["Location"], Fore.GREEN),
        ("Carrier Node",    data["ISP"],      Fore.CYAN),
        ("Current IP",      data["IP"],       Fore.GREEN),
        ("Cellular Status", data["Status"],   Fore.RED),
    ])
    end_session()


def ip_tracker():
    clear()
    header()
    center("━━  IP ADDRESS LOCATOR  ━━", Fore.CYAN + Style.BRIGHT)
    print()
    ip = input(Fore.YELLOW + "  [?] Enter IPv4 / IPv6 Address : " + Fore.WHITE)
    cinematic_loader(ip)

    if ip in MOCK_IP_DATA:
        data = MOCK_IP_DATA[ip]
    else:
        data = {
            "Gateway":  f"RED-ROUTER NODE #{random.randint(100,999)}",
            "Location": random.choice(LOCATIONS),
            "Status":   "FIREWALL BYPASSED",
        }

    result_block("Network Trace", [
        ("IP Node",         ip,               Fore.GREEN),
        ("Gateway Bridge",  data["Gateway"],  Fore.CYAN),
        ("Location Region", data["Location"], Fore.GREEN),
        ("Infiltration",    data["Status"],   Fore.RED),
    ])
    end_session()


def forensics():
    clear()
    header()
    center("━━  DIGITAL FORENSICS & DUMP READER  ━━", Fore.CYAN + Style.BRIGHT)
    print()
    dump = input(Fore.YELLOW + "  [?] Select Device / Memory Dump File : " + Fore.WHITE)
    cinematic_loader(dump)

    if dump in MOCK_FORENSICS_DATA:
        data = MOCK_FORENSICS_DATA[dump]
    else:
        data = {
            "Artifacts": f"{random.randint(100,900)} MB RAW ARTIFACTS RECOVERED",
            "Messages":  f"{random.randint(50,300)} Deleted Items Restored",
            "Key":       "AES-256 MASTER KEY ENGAGED",
        }

    result_block("Extraction Report", [
        ("Extraction Log", data["Artifacts"], Fore.GREEN),
        ("Deleted Items",  data["Messages"],  Fore.GREEN),
        ("Decryption Key", data["Key"],       Fore.RED),
    ])
    end_session()


# =====================================================================
#  ENTRY POINT
# =====================================================================
def run():
    boot_sequence()
    while True:
        choice = menu()
        if   choice == '1': email_tracker()
        elif choice == '2': phone_tracker()
        elif choice == '3': ip_tracker()
        elif choice == '4': forensics()
        elif choice == '0':
            print()
            glitch_text("  ██ SHUTTING DOWN DARK-NET LOCATOR PROTOCOL ██", color=Fore.RED)
            time.sleep(0.5)
            glitch_text("  CONNECTION CLOSED — PROXY CHAIN DISSOLVED",    color=Fore.RED)
            time.sleep(0.3)
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\n  [!] Invalid selection — access denied.")
        input(Fore.WHITE + Style.DIM + "\n  Press [ENTER] to return to Main Menu...")


if __name__ == "__main__":
    run()
