import streamlit as st
import hashlib
import os
import datetime
import random
import json
from pathlib import Path

# ============================================================================
# CONFIGURATION AND SETUP
# ============================================================================

st.set_page_config(page_title="Agentic Dashboard", layout="wide")

# Bob Ross-style background
def apply_bob_ross_theme():
    st.markdown("""
        <style>
            .main {
                background-color: #2C1810;
                color: #F5DEB3;
            }
            .stSidebar {
                background-color: #1A0F0A;
                color: #F5DEB3;
            }
            .stButton > button {
                background-color: #8B4513;
                color: #F5DEB3;
                border: 2px solid #D2B48C;
            }
            .stTextInput > div > div > input {
                background-color: #3E2723;
                color: #F5DEB3;
            }
            .stSelectbox > div > div > div {
                background-color: #3E2723;
                color: #F5DEB3;
            }
            h1, h2, h3 {
                color: #FFD700;
                font-family: Georgia, serif;
            }
            .stMarkdown {
                color: #F5DEB3;
            }
        </style>
    """, unsafe_allow_html=True)

apply_bob_ross_theme()

# ============================================================================
# USER AUTHENTICATION
# ============================================================================

DATA_DIR = Path(st.secrets.get("data_dir", "./user_data"))
DATA_DIR.mkdir(exist_ok=True)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def user_exists(username):
    user_file = DATA_DIR / f"{username}.txt"
    return user_file.exists()

def register_user(username, password):
    if user_exists(username):
        return False, "Username already exists"
    user_file = DATA_DIR / f"{username}.txt"
    user_data = {
        "password_hash": hash_password(password),
        "created": datetime.datetime.now().isoformat(),
        "orders": []
    }
    user_file.write_text(json.dumps(user_data))
    return True, "User registered successfully"

def authenticate_user(username, password):
    if not user_exists(username):
        return False, "User not found"
    user_file = DATA_DIR / f"{username}.txt"
    user_data = json.loads(user_file.read_text())
    if user_data["password_hash"] == hash_password(password):
        return True, "Login successful"
    return False, "Incorrect password"

def get_user_data(username):
    user_file = DATA_DIR / f"{username}.txt"
    return json.loads(user_file.read_text())

def update_user_data(username, data):
    user_file = DATA_DIR / f"{username}.txt"
    user_file.write_text(json.dumps(data))

# ============================================================================
# FEATURE: AUTHENTICATION PAGES
# ============================================================================

def feature_registration():
    st.subheader("Register New Account")
    with st.form("registration_form"):
        username = st.text_input("Username", key="reg_username")
        password = st.text_input("Password", type="password", key="reg_password")
        confirm = st.text_input("Confirm Password", type="password", key="reg_confirm")
        submitted = st.form_submit_button("Register")
        
        if submitted:
            if not username or not password:
                st.error("Username and password required")
            elif password != confirm:
                st.error("Passwords do not match")
            else:
                success, msg = register_user(username, password)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)

def feature_login():
    st.subheader("Login")
    with st.form("login_form"):
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        submitted = st.form_submit_button("Login")
        
        if submitted:
            success, msg = authenticate_user(username, password)
            if success:
                st.session_state.logged_in = True
                st.session_state.current_user = username
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)

# ============================================================================
# FEATURES: 20 INTEGRATED FEATURES
# ============================================================================

def feature_atm():
    st.subheader("ATM Simulator")
    balance = st.number_input("Current Balance", min_value=0.0, step=0.01)
    action = st.radio("Select Action", ["Withdraw", "Deposit", "Check Balance"])
    
    if action in ["Withdraw", "Deposit"]:
        amount = st.number_input(f"{action} Amount", min_value=0.0, step=0.01)
        if st.button(f"Submit {action}"):
            if action == "Withdraw":
                if amount > balance:
                    st.error("Insufficient funds")
                else:
                    new_balance = balance - amount
                    st.success(f"Withdrew \. New balance: \")
            else:
                new_balance = balance + amount
                st.success(f"Deposited \. New balance: \")
    else:
        st.info(f"Current Balance: \")

def feature_budget():
    st.subheader("Budget Planner")
    income = st.number_input("Monthly Income", min_value=0.0, step=0.01)
    expenses = {}
    categories = ["Housing", "Food", "Transportation", "Utilities", "Entertainment", "Savings"]
    
    for category in categories:
        expenses[category] = st.number_input(f"{category} Expenses", min_value=0.0, step=0.01)
    
    total_expenses = sum(expenses.values())
    remaining = income - total_expenses
    
    st.write("---")
    st.write("Budget Summary:")
    for category, amount in expenses.items():
        percentage = (amount / income * 100) if income > 0 else 0
        st.write(f"{category}: \ ({percentage:.1f}%)")
    
    st.write(f"**Total Expenses: \**")
    if remaining >= 0:
        st.success(f"**Remaining: \**")
    else:
        st.error(f"**Over Budget: \**")

def feature_buffet():
    st.subheader("Buffet Order System")
    foods = ["Pizza", "Chicken", "Beef", "Fish", "Vegetables", "Rice", "Pasta", "Salad"]
    selected_foods = st.multiselect("Select Foods", foods)
    portions = st.slider("Number of Portions", 1, 10, 1)
    
    prices = {"Pizza": 2.50, "Chicken": 4.00, "Beef": 5.00, "Fish": 4.50, 
              "Vegetables": 1.50, "Rice": 1.00, "Pasta": 2.00, "Salad": 2.25}
    
    total = sum(prices.get(food, 0) for food in selected_foods) * portions
    
    if st.button("Add to Order"):
        user_data = get_user_data(st.session_state.current_user)
        order = {
            "type": "Buffet",
            "items": selected_foods,
            "portions": portions,
            "total": total,
            "timestamp": datetime.datetime.now().isoformat()
        }
        user_data["orders"].append(order)
        update_user_data(st.session_state.current_user, user_data)
        st.success(f"Order total: \")

def feature_magic_8_ball():
    st.subheader("Magic 8 Ball")
    question = st.text_input("Ask the Magic 8 Ball a yes/no question")
    
    responses = [
        "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
        "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
        "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
        "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
        "Don't count on it", "My reply is no", "My sources say no", "Outlook not good",
        "Very doubtful"
    ]
    
    if st.button("Shake"):
        if question:
            response = random.choice(responses)
            st.info(f"Question: {question}\n\nAnswer: **{response}**")
        else:
            st.warning("Please ask a question first")

def feature_madlibs():
    st.subheader("MadLibs Game")
    noun1 = st.text_input("Enter a noun")
    verb1 = st.text_input("Enter a verb")
    adj1 = st.text_input("Enter an adjective")
    noun2 = st.text_input("Enter another noun")
    verb2 = st.text_input("Enter another verb")
    
    if st.button("Generate Story"):
        story = f"Yesterday, I saw a {adj1} {noun1} {verb1} down the street. It was chasing a {noun2}. "
        story += f"I decided to {verb2} away as fast as I could!"
        st.success(story)

def feature_smoothie_bar():
    st.subheader("Smoothie Bar")
    fruits = ["Strawberry", "Banana", "Mango", "Blueberry", "Raspberry", "Pineapple"]
    bases = ["Yogurt", "Milk", "Coconut Milk", "Almond Milk"]
    toppings = ["Granola", "Honey", "Chia Seeds", "Coconut Flakes"]
    
    selected_fruits = st.multiselect("Select Fruits", fruits, max_selections=3)
    base = st.selectbox("Select Base", bases)
    selected_toppings = st.multiselect("Select Toppings", toppings)
    
    if st.button("Order Smoothie"):
        smoothie = {
            "type": "Smoothie",
            "fruits": selected_fruits,
            "base": base,
            "toppings": selected_toppings,
            "timestamp": datetime.datetime.now().isoformat()
        }
        user_data = get_user_data(st.session_state.current_user)
        user_data["orders"].append(smoothie)
        update_user_data(st.session_state.current_user, user_data)
        st.success("Smoothie ordered!")

def feature_pizza_engine():
    st.subheader("Pizza Engine")
    size = st.radio("Pizza Size", ["Small (10\")", "Medium (12\")", "Large (14\")", "XLarge (16\")"])
    crust = st.selectbox("Crust Type", ["Thin", "Regular", "Thick", "Stuffed"])
    
    toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Cheese", "Olives", "Bacon", "Spinach"]
    selected_toppings = st.multiselect("Select Toppings", toppings)
    
    prices = {"Small (10\")": 8.99, "Medium (12\")": 11.99, "Large (14\")": 14.99, "XLarge (16\")": 17.99}
    base_price = prices.get(size, 11.99)
    topping_cost = len(selected_toppings) * 1.50
    total = base_price + topping_cost
    
    st.write(f"Base Price: \")
    st.write(f"Topping Cost: \")
    st.write(f"**Total: \**")
    
    if st.button("Order Pizza"):
        order = {"type": "Pizza", "size": size, "crust": crust, "toppings": selected_toppings, "total": total, "timestamp": datetime.datetime.now().isoformat()}
        user_data = get_user_data(st.session_state.current_user)
        user_data["orders"].append(order)
        update_user_data(st.session_state.current_user, user_data)
        st.success("Pizza ordered!")

def feature_bug_tracker():
    st.subheader("Bug Tracker")
    bug_title = st.text_input("Bug Title")
    severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
    description = st.text_area("Bug Description")
    
    if st.button("Report Bug"):
        if bug_title and description:
            bug = {"title": bug_title, "severity": severity, "description": description, "timestamp": datetime.datetime.now().isoformat()}
            user_data = get_user_data(st.session_state.current_user)
            if "bugs" not in user_data:
                user_data["bugs"] = []
            user_data["bugs"].append(bug)
            update_user_data(st.session_state.current_user, user_data)
            st.success("Bug reported!")
        else:
            st.error("Please fill in all fields")

def feature_nato_translator():
    st.subheader("NATO Phonetic Translator")
    nato_dict = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"}
    
    text = st.text_input("Enter text to translate").upper()
    
    if st.button("Translate"):
        translated = " ".join([nato_dict.get(char, char) for char in text if char.isalpha()])
        if translated:
            st.success(f"Translated: {translated}")

def feature_theater_tickets():
    st.subheader("Theater Ticket Booking")
    movie = st.selectbox("Select Movie", ["The Matrix", "Inception", "Interstellar", "The Dark Knight", "Tenet"])
    time = st.selectbox("Select Time", ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"])
    num_tickets = st.number_input("Number of Tickets", min_value=1, max_value=10, step=1)
    
    ticket_price = 12.50
    total = num_tickets * ticket_price
    
    st.write(f"Movie: {movie}")
    st.write(f"Time: {time}")
    st.write(f"Tickets: {num_tickets} x \ = \")
    
    if st.button("Book Tickets"):
        order = {"type": "Theater", "movie": movie, "time": time, "tickets": num_tickets, "total": total, "timestamp": datetime.datetime.now().isoformat()}
        user_data = get_user_data(st.session_state.current_user)
        user_data["orders"].append(order)
        update_user_data(st.session_state.current_user, user_data)
        st.success("Tickets booked!")

def feature_logic_checks():
    st.subheader("Logic Checks")
    st.write("Check logical conditions:")
    
    a = st.number_input("Enter value A", value=5)
    b = st.number_input("Enter value B", value=3)
    
    st.write(f"A > B: {a > b}")
    st.write(f"A < B: {a < b}")
    st.write(f"A == B: {a == b}")
    st.write(f"A != B: {a != b}")
    st.write(f"A >= B: {a >= b}")
    st.write(f"A <= B: {a <= b}")
    st.write(f"A AND B (both > 0): {a > 0 and b > 0}")
    st.write(f"A OR B (at least one > 0): {a > 0 or b > 0}")

def feature_string_mastery():
    st.subheader("String Mastery")
    text = st.text_area("Enter Text")
    
    if text:
        st.write(f"Length: {len(text)}")
        st.write(f"Uppercase: {text.upper()}")
        st.write(f"Lowercase: {text.lower()}")
        st.write(f"Reversed: {text[::-1]}")
        st.write(f"Word Count: {len(text.split())}")
        st.write(f"Character Count (no spaces): {len(text.replace(' ', ''))}")

def feature_loop_tasks():
    st.subheader("Loop Tasks")
    n = st.number_input("Enter a number", min_value=1, max_value=100, step=1)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Multiplication Table:**")
        result = [f"{n} × {i} = {n*i}" for i in range(1, 11)]
        for r in result:
            st.write(r)
    
    with col2:
        st.write("**Fibonacci Sequence:**")
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        for f in fib[:n]:
            st.write(f)

def feature_rpg_profile():
    st.subheader("RPG Profile Generator")
    character_name = st.text_input("Character Name")
    character_class = st.selectbox("Class", ["Warrior", "Mage", "Rogue", "Paladin", "Ranger"])
    race = st.selectbox("Race", ["Human", "Elf", "Dwarf", "Orc", "Gnome"])
    
    if st.button("Generate Stats"):
        stats = {
            "Strength": random.randint(10, 20),
            "Dexterity": random.randint(10, 20),
            "Constitution": random.randint(10, 20),
            "Intelligence": random.randint(10, 20),
            "Wisdom": random.randint(10, 20),
            "Charisma": random.randint(10, 20)
        }
        
        st.write(f"**{character_name}** - {race} {character_class}")
        for stat, value in stats.items():
            st.write(f"{stat}: {value}")

def feature_joke():
    st.subheader("Joke Generator")
    jokes = [
        ("Why don't scientists trust atoms?", "Because they make up everything!"),
        ("What do you call a fake noodle?", "An impasta!"),
        ("Why did the scarecrow win an award?", "Because he was outstanding in his field!"),
        ("What's the best thing about Switzerland?", "I don't know, but their flag is a big plus."),
        ("Why don't eggs tell jokes?", "They'd crack each other up!"),
    ]
    
    if st.button("Tell Me a Joke"):
        joke = random.choice(jokes)
        st.write(f"**{joke[0]}**")
        st.write(f"_{joke[1]}_")

def feature_locked_calendar():
    st.subheader("Locked Calendar")
    st.write("Calendar with locked events")
    month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    year = st.number_input("Year", min_value=2020, max_value=2050)
    
    events = {
        "January": ["New Year's Day"],
        "February": ["Valentine's Day"],
        "July": ["Independence Day"],
        "December": ["Christmas"]
    }
    
    st.write(f"Events in {month} {year}:")
    for event in events.get(month, []):
        st.write(f"📌 {event}")

def feature_audit_menu():
    st.subheader("Audit & Menu")
    user_data = get_user_data(st.session_state.current_user)
    
    st.write("**User Information:**")
    st.write(f"Username: {st.session_state.current_user}")
    st.write(f"Account Created: {user_data['created']}")
    st.write(f"Total Orders: {len(user_data.get('orders', []))}")
    
    if st.checkbox("Show All Orders"):
        for i, order in enumerate(user_data.get("orders", []), 1):
            st.write(f"Order {i}: {order}")

def feature_gaming_pc_builder():
    st.subheader("Gaming PC Builder")
    
    components = {
        "CPU": ["Intel i9-13900K", "AMD Ryzen 9 7950X", "Intel i7-13700K"],
        "GPU": ["RTX 4090", "RTX 4080", "RTX 4070 Ti"],
        "RAM": ["64GB DDR5", "32GB DDR5", "16GB DDR5"],
        "Storage": ["4TB SSD", "2TB SSD", "1TB SSD"],
        "PSU": ["1200W Gold", "1000W Gold", "850W Gold"]
    }
    
    total = 0
    prices = {
        "Intel i9-13900K": 689, "AMD Ryzen 9 7950X": 699, "Intel i7-13700K": 429,
        "RTX 4090": 1599, "RTX 4080": 1199, "RTX 4070 Ti": 799,
        "64GB DDR5": 349, "32GB DDR5": 199, "16GB DDR5": 99,
        "4TB SSD": 299, "2TB SSD": 149, "1TB SSD": 89,
        "1200W Gold": 249, "1000W Gold": 179, "850W Gold": 139
    }
    
    build = {}
    for component, options in components.items():
        selected = st.selectbox(component, options)
        build[component] = selected
        total += prices.get(selected, 0)
    
    st.write(f"**Total Cost: \**")

def feature_menu_item_object():
    st.subheader("Menu Item Object")
    
    class MenuItem:
        def __init__(self, name, price, description):
            self.name = name
            self.price = price
            self.description = description
        
        def display(self):
            return f"{self.name} - \\n{self.description}"
    
    items = [
        MenuItem("Burger", 9.99, "Fresh beef patty with lettuce and tomato"),
        MenuItem("Pizza", 11.99, "Cheese and pepperoni"),
        MenuItem("Salad", 7.99, "Fresh vegetables"),
        MenuItem("Soda", 2.99, "Cold carbonated beverage"),
    ]
    
    for item in items:
        st.write(item.display())

# ============================================================================
# MAIN APP
# ============================================================================

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    if not st.session_state.logged_in:
        st.title("🎨 Agentic Dashboard")
        col1, col2 = st.columns(2)
        with col1:
            feature_registration()
        with col2:
            feature_login()
    else:
        st.sidebar.title("Navigation")
        st.title(f"🎨 Welcome, {st.session_state.current_user}!")
        
        page = st.sidebar.radio("Select Feature", [
            "Dashboard",
            "ATM",
            "Budget",
            "Buffet",
            "Magic 8 Ball",
            "MadLibs",
            "Smoothie Bar",
            "Pizza Engine",
            "Bug Tracker",
            "NATO Translator",
            "Theater Tickets",
            "Logic Checks",
            "String Mastery",
            "Loop Tasks",
            "RPG Profile",
            "Joke",
            "Locked Calendar",
            "Audit & Menu",
            "Gaming PC Builder",
            "Menu Item Object"
        ])
        
        if page == "Dashboard":
            st.write("Welcome to your dashboard!")
            user_data = get_user_data(st.session_state.current_user)
            st.write(f"Total Orders: {len(user_data.get('orders', []))}")
        elif page == "ATM":
            feature_atm()
        elif page == "Budget":
            feature_budget()
        elif page == "Buffet":
            feature_buffet()
        elif page == "Magic 8 Ball":
            feature_magic_8_ball()
        elif page == "MadLibs":
            feature_madlibs()
        elif page == "Smoothie Bar":
            feature_smoothie_bar()
        elif page == "Pizza Engine":
            feature_pizza_engine()
        elif page == "Bug Tracker":
            feature_bug_tracker()
        elif page == "NATO Translator":
            feature_nato_translator()
        elif page == "Theater Tickets":
            feature_theater_tickets()
        elif page == "Logic Checks":
            feature_logic_checks()
        elif page == "String Mastery":
            feature_string_mastery()
        elif page == "Loop Tasks":
            feature_loop_tasks()
        elif page == "RPG Profile":
            feature_rpg_profile()
        elif page == "Joke":
            feature_joke()
        elif page == "Locked Calendar":
            feature_locked_calendar()
        elif page == "Audit & Menu":
            feature_audit_menu()
        elif page == "Gaming PC Builder":
            feature_gaming_pc_builder()
        elif page == "Menu Item Object":
            feature_menu_item_object()
        
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.current_user = None
            st.rerun()

if __name__ == "__main__":
    main()
