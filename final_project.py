#Gaming PC builder

import os
import sys
from dataclasses import dataclass, field
from typing import Optional

# ─────────────────────────────────────────────────────────────
# COLOR HELPERS
# ─────────────────────────────────────────────────────────────
RESET  = "re"
BOLD   = "bo"
DIM    = "dim"
RED    = "red"
GREEN  = "green"
YELLOW = "yellow"
CYAN   = "cyan"
MAGENTA= "magenta"
BLUE   = "blue"
WHITE  = "white"

def clr(text, *codes):
    return "".join(codes) + str(text) + RESET

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input(clr("Press ENTER to continue…", DIM))

# ─────────────────────────────────────────────────────────────
# Data
# ─────────────────────────────────────────────────────────────
@dataclass
class Part:
    name: str
    price: float
    specs: dict = field(default_factory=dict)

    def __str__(self):
        return f"{self.name}  (${self.price:.2f})"


# ─────────────────────────────────────────────────────────────
# Parts catalogue 
# All prices in USD (approximate street prices)
# Compatibility keys:
#   socket   – CPU/Motherboard socket type
#   chipset  – Motherboard chipset family (AMD / Intel)
#   ddr      – RAM generation (DDR4 / DDR5)
#   tdp      – CPU thermal design power (watts) for cooler matching
#   pcie     – GPU PCIe slot version required (4 / 5)
#   wattage  – PSU recommended minimum wattage
# ─────────────────────────────────────────────────────────────

CATALOG: dict[str, list[Part]] = {

    # ── CPUs ──────────────────────────────────────────────────
    "CPU": [
        Part("Intel Core i5-13600K",   319.99, {"socket": "LGA1700", "chipset": "Intel", "tdp": 125, "ddr": ["DDR4","DDR5"]}),
        Part("Intel Core i7-13700K",   419.99, {"socket": "LGA1700", "chipset": "Intel", "tdp": 125, "ddr": ["DDR4","DDR5"]}),
        Part("Intel Core i9-13900K",   589.99, {"socket": "LGA1700", "chipset": "Intel", "tdp": 253, "ddr": ["DDR4","DDR5"]}),
        Part("Intel Core i5-14600K",   329.99, {"socket": "LGA1700", "chipset": "Intel", "tdp": 125, "ddr": ["DDR4","DDR5"]}),
        Part("Intel Core i9-14900K",   549.99, {"socket": "LGA1700", "chipset": "Intel", "tdp": 253, "ddr": ["DDR4","DDR5"]}),
        Part("AMD Ryzen 5 7600X",      249.99, {"socket": "AM5",     "chipset": "AMD",   "tdp": 105, "ddr": ["DDR5"]}),
        Part("AMD Ryzen 7 7700X",      349.99, {"socket": "AM5",     "chipset": "AMD",   "tdp": 105, "ddr": ["DDR5"]}),
        Part("AMD Ryzen 9 7900X",      449.99, {"socket": "AM5",     "chipset": "AMD",   "tdp": 170, "ddr": ["DDR5"]}),
        Part("AMD Ryzen 9 7950X",      699.99, {"socket": "AM5",     "chipset": "AMD",   "tdp": 170, "ddr": ["DDR5"]}),
        Part("AMD Ryzen 5 5600X",      149.99, {"socket": "AM4",     "chipset": "AMD",   "tdp":  65, "ddr": ["DDR4"]}),
        Part("AMD Ryzen 7 5800X3D",    249.99, {"socket": "AM4",     "chipset": "AMD",   "tdp": 105, "ddr": ["DDR4"]}),
    ],

    # ── GPUs ──────────────────────────────────────────────────
    "GPU": [
        Part("NVIDIA GeForce RTX 4060",        299.99, {"wattage": 550, "pcie": 4}),
        Part("NVIDIA GeForce RTX 4060 Ti",     399.99, {"wattage": 650, "pcie": 4}),
        Part("NVIDIA GeForce RTX 4070",        599.99, {"wattage": 650, "pcie": 4}),
        Part("NVIDIA GeForce RTX 4070 Ti",     799.99, {"wattage": 700, "pcie": 4}),
        Part("NVIDIA GeForce RTX 4080",        999.99, {"wattage": 750, "pcie": 4}),
        Part("NVIDIA GeForce RTX 4090",       1599.99, {"wattage": 850, "pcie": 4}),
        Part("AMD Radeon RX 7600",             269.99, {"wattage": 550, "pcie": 4}),
        Part("AMD Radeon RX 7700 XT",          349.99, {"wattage": 600, "pcie": 4}),
        Part("AMD Radeon RX 7800 XT",          499.99, {"wattage": 650, "pcie": 4}),
        Part("AMD Radeon RX 7900 XTX",         999.99, {"wattage": 800, "pcie": 4}),
    ],

    # ── Motherboards ──────────────────────────────────────────
    "Motherboard": [
        Part("ASUS ROG Strix B760-F (DDR5)",         249.99, {"socket": "LGA1700", "chipset": "Intel", "ddr": "DDR5", "pcie": 4}),
        Part("MSI PRO B760M-A (DDR4)",               149.99, {"socket": "LGA1700", "chipset": "Intel", "ddr": "DDR4", "pcie": 4}),
        Part("Gigabyte Z790 AORUS Elite AX (DDR5)",  349.99, {"socket": "LGA1700", "chipset": "Intel", "ddr": "DDR5", "pcie": 5}),
        Part("ASUS TUF Gaming Z790-Plus (DDR4)",     249.99, {"socket": "LGA1700", "chipset": "Intel", "ddr": "DDR4", "pcie": 4}),
        Part("MSI MEG Z790 ACE (DDR5)",              549.99, {"socket": "LGA1700", "chipset": "Intel", "ddr": "DDR5", "pcie": 5}),
        Part("ASUS ROG Crosshair X670E (DDR5)",      599.99, {"socket": "AM5",     "chipset": "AMD",   "ddr": "DDR5", "pcie": 5}),
        Part("MSI MAG X670E Tomahawk (DDR5)",        299.99, {"socket": "AM5",     "chipset": "AMD",   "ddr": "DDR5", "pcie": 4}),
        Part("Gigabyte B650 AORUS Elite AX (DDR5)",  229.99, {"socket": "AM5",     "chipset": "AMD",   "ddr": "DDR5", "pcie": 4}),
        Part("ASRock B550 Phantom Gaming-ITX (DDR4)",159.99, {"socket": "AM4",     "chipset": "AMD",   "ddr": "DDR4", "pcie": 4}),
        Part("MSI MAG B550 TOMAHAWK (DDR4)",         179.99, {"socket": "AM4",     "chipset": "AMD",   "ddr": "DDR4", "pcie": 4}),
    ],

    # ── RAM ───────────────────────────────────────────────────
    "RAM": [
        Part("Corsair Vengeance 16GB DDR4-3200",    49.99, {"ddr": "DDR4", "capacity_gb": 16}),
        Part("G.Skill Ripjaws V 32GB DDR4-3600",    74.99, {"ddr": "DDR4", "capacity_gb": 32}),
        Part("Corsair Vengeance 64GB DDR4-3200",   124.99, {"ddr": "DDR4", "capacity_gb": 64}),
        Part("Kingston Fury Beast 16GB DDR5-5200",  69.99, {"ddr": "DDR5", "capacity_gb": 16}),
        Part("G.Skill Trident Z5 32GB DDR5-6000",  109.99, {"ddr": "DDR5", "capacity_gb": 32}),
        Part("Corsair Dominator Platinum 64GB DDR5-5600", 219.99, {"ddr": "DDR5", "capacity_gb": 64}),
        Part("TeamGroup T-Force Delta 32GB DDR5-5200",     89.99, {"ddr": "DDR5", "capacity_gb": 32}),
    ],

    # ── Cases ─────────────────────────────────────────────────
    "Case": [
        Part("Fractal Design Meshify C",        89.99,  {"form": "ATX"}),
        Part("NZXT H510",                       79.99,  {"form": "ATX"}),
        Part("Lian Li PC-O11 Dynamic",         149.99,  {"form": "ATX"}),
        Part("Corsair 4000D Airflow",           104.99, {"form": "ATX"}),
        Part("Phanteks Eclipse P500A",          139.99, {"form": "ATX"}),
        Part("Fractal Design Define 7 Compact",  99.99, {"form": "ATX"}),
        Part("NZXT H9 Flow",                   149.99,  {"form": "ATX"}),
        Part("Cooler Master HAF 700 EVO",      299.99,  {"form": "ATX"}),
    ],

    # ── Storage ───────────────────────────────────────────────
    "Storage": [
        Part("Seagate Barracuda 2TB HDD (7200rpm)",   54.99, {"type": "HDD", "capacity_tb": 2}),
        Part("WD Blue 4TB HDD (5400rpm)",             84.99, {"type": "HDD", "capacity_tb": 4}),
        Part("Samsung 870 EVO 1TB SATA SSD",          89.99, {"type": "SSD", "capacity_tb": 1}),
        Part("Samsung 870 EVO 2TB SATA SSD",         149.99, {"type": "SSD", "capacity_tb": 2}),
        Part("WD Black SN850X 1TB NVMe SSD",         119.99, {"type": "NVMe","capacity_tb": 1}),
        Part("WD Black SN850X 2TB NVMe SSD",         199.99, {"type": "NVMe","capacity_tb": 2}),
        Part("Samsung 990 Pro 1TB NVMe SSD",         109.99, {"type": "NVMe","capacity_tb": 1}),
        Part("Seagate FireCuda 530 2TB NVMe SSD",    219.99, {"type": "NVMe","capacity_tb": 2}),
    ],

    # ── PSUs ──────────────────────────────────────────────────
    "PSU": [
        Part("Corsair RM550x 550W 80+ Gold",    89.99, {"wattage": 550, "rating": "Gold"}),
        Part("Seasonic Focus GX-650 650W 80+ Gold",  104.99, {"wattage": 650, "rating": "Gold"}),
        Part("EVGA SuperNOVA 750 G6 750W 80+ Gold",   99.99, {"wattage": 750, "rating": "Gold"}),
        Part("Corsair HX850 850W 80+ Platinum",      164.99, {"wattage": 850, "rating": "Platinum"}),
        Part("Seasonic Prime TX-1000 1000W 80+ Titanium", 269.99, {"wattage": 1000, "rating": "Titanium"}),
        Part("be quiet! Dark Power 13 1000W 80+ Titanium", 299.99, {"wattage": 1000, "rating": "Titanium"}),
    ],

    # ── CPU Coolers ───────────────────────────────────────────
    "CPU Cooler": [
        Part("Cooler Master Hyper 212 (Air)",          34.99, {"type": "Air",   "max_tdp": 150, "sockets": ["LGA1700","AM5","AM4"]}),
        Part("Noctua NH-D15 (Air)",                    99.99, {"type": "Air",   "max_tdp": 250, "sockets": ["LGA1700","AM5","AM4"]}),
        Part("be quiet! Dark Rock Pro 4 (Air)",        89.99, {"type": "Air",   "max_tdp": 250, "sockets": ["LGA1700","AM5","AM4"]}),
        Part("NZXT Kraken X53 240mm AIO",             119.99, {"type": "AIO",   "max_tdp": 200, "sockets": ["LGA1700","AM5","AM4"]}),
        Part("Corsair iCUE H100i Elite 240mm AIO",    134.99, {"type": "AIO",   "max_tdp": 250, "sockets": ["LGA1700","AM5","AM4"]}),
        Part("LIAN LI GALAHAD 360mm AIO",             159.99, {"type": "AIO",   "max_tdp": 300, "sockets": ["LGA1700","AM5","AM4"]}),
        Part("EK-AIO 360 D-RGB AIO",                  179.99, {"type": "AIO",   "max_tdp": 300, "sockets": ["LGA1700","AM5","AM4"]}),
    ],

    # ── OS ────────────────────────────────────────────────────
    "OS": [
        Part("Windows 11 Home",         139.99, {"type": "Windows"}),
        Part("Windows 11 Pro",          199.99, {"type": "Windows"}),
        Part("Ubuntu 24.04 LTS",          0.00, {"type": "Linux"}),
        Part("Fedora 40 Workstation",     0.00, {"type": "Linux"}),
        Part("Pop!_OS 22.04 LTS",         0.00, {"type": "Linux"}),
        Part("Linux Mint 21.3",           0.00, {"type": "Linux"}),
    ],
}

CATEGORY_ORDER = ["CPU", "GPU", "Motherboard", "RAM", "Case", "Storage", "PSU", "CPU Cooler", "OS"]

CATEGORY_ICONS = {
    "CPU":        "🧠",
    "GPU":        "🎮",
    "Motherboard":"🔌",
    "RAM":        "💾",
    "Case":       "🗄️",
    "Storage":    "💿",
    "PSU":        "⚡",
    "CPU Cooler": "❄️",
    "OS":         "💻",
}


# ─────────────────────────────────────────────────────────────
# Compatibility engine
# ─────────────────────────────────────────────────────────────
def check_compatibility(build: dict[str, Optional[Part]]) -> list[str]:
    """Return a list of human-readable compatibility warnings."""
    issues = []
    cpu  = build.get("CPU")
    mobo = build.get("Motherboard")
    ram  = build.get("RAM")
    gpu  = build.get("GPU")
    psu  = build.get("PSU")
    cool = build.get("CPU Cooler")

    # CPU ↔ Motherboard socket
    if cpu and mobo:
        if cpu.specs["socket"] != mobo.specs["socket"]:
            issues.append(
                f"❌ CPU socket ({cpu.specs['socket']}) ≠ Motherboard socket ({mobo.specs['socket']})"
            )

    # CPU ↔ Motherboard chipset family
    if cpu and mobo:
        if cpu.specs["chipset"] != mobo.specs["chipset"]:
            issues.append(
                f"❌ CPU chipset family ({cpu.specs['chipset']}) ≠ Motherboard family ({mobo.specs['chipset']})"
            )

    # Motherboard ↔ RAM generation
    if mobo and ram:
        if mobo.specs["ddr"] != ram.specs["ddr"]:
            issues.append(
                f"❌ Motherboard supports {mobo.specs['ddr']} but selected RAM is {ram.specs['ddr']}"
            )

    # CPU ↔ RAM generation
    if cpu and ram:
        if ram.specs["ddr"] not in cpu.specs.get("ddr", []):
            issues.append(
                f"❌ CPU ({cpu.name}) does not support {ram.specs['ddr']} RAM"
            )

    # PSU wattage vs GPU requirement
    if gpu and psu:
        if psu.specs["wattage"] < gpu.specs["wattage"]:
            issues.append(
                f"❌ GPU requires ≥{gpu.specs['wattage']}W PSU but selected PSU is {psu.specs['wattage']}W"
            )

    # CPU cooler socket support
    if cpu and cool:
        if cpu.specs["socket"] not in cool.specs.get("sockets", []):
            issues.append(
                f"❌ CPU Cooler does not support socket {cpu.specs['socket']}"
            )

    # CPU cooler TDP vs CPU TDP
    if cpu and cool:
        if cool.specs["max_tdp"] < cpu.specs["tdp"]:
            issues.append(
                f"⚠️  CPU TDP ({cpu.specs['tdp']}W) exceeds cooler max TDP ({cool.specs['max_tdp']}W) — consider a bigger cooler"
            )

    return issues


def is_compatible_with_build(category: str, part: Part, build: dict[str, Optional[Part]]) -> list[str]:
   
    trial = dict(build)
    trial[category] = part
    return check_compatibility(trial)


# ─────────────────────────────────────────────────────────────
# Display helpers
# ─────────────────────────────────────────────────────────────
def header():
    print(clr("╔══════════════════════════════════════════════════════════╗", CYAN, BOLD))
    print(clr("║          🖥️   GAMING PC BUILDER  🖥️                      ║", CYAN, BOLD))
    print(clr("╚══════════════════════════════════════════════════════════╝", CYAN, BOLD))
    print()


def print_build_summary(build: dict[str, Optional[Part]]):
    
    print(clr("  YOUR CURRENT BUILD", BOLD, WHITE))
    
    total = 0.0
    for cat in CATEGORY_ORDER:
        icon  = CATEGORY_ICONS.get(cat, "•")
        part  = build.get(cat)
        label = clr(f"{icon} {cat:<14}", CYAN)
        if part:
            price_str = clr(f"${part.price:>8.2f}", GREEN)
            print(f"  {label} {part.name:<30} {price_str}")
            total += part.price
        else:
            print(f"  {label} {clr('(not selected)', DIM):<30} {clr('   —', DIM)}")
    print(clr("─" * 62, DIM))
    print(f"  {'TOTAL':>46}  {clr(f'${total:>8.2f}', YELLOW, BOLD)}")
    print(clr("─" * 62, DIM))
    print()

    # Compatibility check
    issues = check_compatibility(build)
    if issues:
        print(clr("  ⚠️  COMPATIBILITY ISSUES:", RED, BOLD))
        for issue in issues:
            print(f"     {issue}")
        print()
    else:
        selected = [v for v in build.values() if v is not None]
        if len(selected) == len(CATEGORY_ORDER):
            print(clr("All parts are compatible!", GREEN, BOLD))
        elif selected:
            print(clr("No issues with parts selected so far!", GREEN))
        print()


def print_parts_list(category: str, parts: list[Part], build: dict[str, Optional[Part]]):
    current = build.get(category)
    print(clr(f"{CATEGORY_ICONS.get(category,'')} {category.upper()} OPTIONS", BOLD, MAGENTA))
    

    # Spec columns to show per category
    SPEC_SHOW = {
        "CPU":         ["socket", "tdp"],
        "GPU":         ["wattage"],
        "Motherboard": ["socket", "ddr"],
        "RAM":         ["ddr", "capacity_gb"],
        "Storage":     ["type", "capacity_tb"],
        "PSU":         ["wattage", "rating"],
        "CPU Cooler":  ["type", "max_tdp"],
        "OS":          ["type"],
        "Case":        ["form"],
    }
    show_keys = SPEC_SHOW.get(category, [])

    for idx, part in enumerate(parts, 1):
        incompat = is_compatible_with_build(category, part, build)
        
        marker = clr("►", GREEN, BOLD) if (current and current.name == part.name) else " "

        # Build spec hints
        spec_hints = []
        for k in show_keys:
            v = part.specs.get(k)
            if v is not None:
                if k == "tdp":
                    spec_hints.append(f"TDP:{v}W")
                elif k == "wattage":
                    spec_hints.append(f"PSU≥{v}W")
                elif k == "max_tdp":
                    spec_hints.append(f"max {v}W")
                elif k == "capacity_gb":
                    spec_hints.append(f"{v}GB")
                elif k == "capacity_tb":
                    spec_hints.append(f"{v}TB")
                else:
                    spec_hints.append(str(v))
        spec_str = "  " + clr(f"[{', '.join(spec_hints)}]", DIM) if spec_hints else ""

        price_str = clr(f"${part.price:>8.2f}", GREEN if not incompat else DIM)
        name_col  = clr(part.name, WHITE) if not incompat else clr(part.name, DIM)

        compat_flag = ""
        if incompat:
            compat_flag = clr("  ✗ incompatible", RED)

        print(f"  {marker} {clr(str(idx)+'.',CYAN):<6} {name_col:<36} {price_str}{spec_str}{compat_flag}")

    print(clr("─" * 62, DIM))
    print(clr("  0. Cancel / Go back", DIM))
    print()


# ─────────────────────────────────────────────────────────────
# MENUS
# ─────────────────────────────────────────────────────────────
def select_part(category: str, build: dict[str, Optional[Part]]) -> Optional[Part]:
    """Show category list, return chosen Part or None to cancel."""
    parts = CATALOG[category]
    while True:
        clear()
        header()
        print_build_summary(build)
        print_parts_list(category, parts, build)

        raw = input(clr(f"  Select {category} [1-{len(parts)}] or 0 to cancel: ", YELLOW)).strip()
        if raw == "0":
            return None
        if raw.isdigit():
            idx = int(raw)
            if 1 <= idx <= len(parts):
                chosen = parts[idx - 1]
                incompat = is_compatible_with_build(category, chosen, build)
                if incompat:
                    print()
                    print(clr("  ⚠️  This part has compatibility issues with your current build:", YELLOW, BOLD))
                    for issue in incompat:
                        print(f"     {issue}")
                    ans = input(clr("\n  Add it anyway? [y/N]: ", YELLOW)).strip().lower()
                    if ans != "y":
                        continue
                return chosen
        print(clr("  Invalid choice. Try again.", RED))
        pause()


def main_menu(build: dict[str, Optional[Part]]):
    while True:
        clear()
        header()
        print_build_summary(build)

        print(clr("  MAIN MENU", BOLD, WHITE))
        print()
        for i, cat in enumerate(CATEGORY_ORDER, 1):
            icon    = CATEGORY_ICONS.get(cat, "•")
            status  = clr("✓", GREEN) if build.get(cat) else clr("○", DIM)
            print(f"  {clr(str(i)+'.', CYAN):<6} {status} {icon} {cat}")
        print()
        print(f"  {clr('C.', CYAN)}   Clear all parts")
        print(f"  {clr('Q.', CYAN)}   Quit")
        print()

        raw = input(clr("  Choose an option: ", YELLOW)).strip().lower()

        if raw == "q":
            clear()
            header()
            print(clr("  Thanks for using Gaming PC Builder! Happy gaming! 🎮\n", GREEN, BOLD))
            sys.exit(0)
        elif raw == "c":
            confirm = input(clr("  Clear all selections? [y/N]: ", RED)).strip().lower()
            if confirm == "y":
                for k in build:
                    build[k] = None
        elif raw.isdigit():
            idx = int(raw)
            if 1 <= idx <= len(CATEGORY_ORDER):
                category = CATEGORY_ORDER[idx - 1]
                chosen = select_part(category, build)
                if chosen is not None:
                    build[category] = chosen
            else:
                print(clr("  Invalid choice.", RED))
                pause()
        else:
            print(clr("  Invalid choice.", RED))
            pause()


# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────
def main():
    build: dict[str, Optional[Part]] = {cat: None for cat in CATEGORY_ORDER}

    clear()
    header()
    print(clr("  Welcome! Build your perfect gaming PC step by step.", WHITE))
    print(clr("  Select each component and the builder will warn you", DIM))
    print(clr("  about any compatibility issues in real time.\n", DIM))
    pause()

    main_menu(build)


if __name__ == "__main__":
    main()