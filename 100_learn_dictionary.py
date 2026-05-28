""" counts = {}
data = [2,3,4,5,2,5,6,4]
for elem in data:
    counts[elem] = counts.get(elem, 0) + 1
for k in sorted(counts.keys(), reverse=True):
    print(k, counts[k]) """


""" counts={}
letters = ['e','a','e','b','a','e','c']
for elem in letters:
    counts[elem] = counts.get(elem, 0) + 1

print(counts) """


""" d = {"a": 5, "b": 2, "c": 9}
most = max(d, key=d.get)
least = min(d, key=d.get)

print(least,most) """


""" prices = {"apple": 2, "fig": 5, "banana": 3}

for k in sorted(prices.keys()):
    print(k, prices[k]) """

""" keys = ["name", "age", "city"]
values = ["Ana", 19, "Lisbon"]

person = dict(zip(keys,values))
 """

""" students = ["Ana", "Tomás", "João"]
grades = [15, 12, 18]

results = dict(zip(students, grades))
print(results) """


""" marks = {"math": 15, "history": 12, "physics": 18, "english": 14}
res = 0

for k, v in marks.items():
    res+=v

if res == 0:
    print("NO data")
else:
    print(res/len(marks)) """


""" text = input("Enter a sentence ")

for ch in text:
    if ch in ",.!?;:":
        text = text.replace(ch, "")
words = text.split()


freq = {}
for word in words:
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1

print("Vocabulary size:", len(freq))

for w in sorted(freq.keys()):
    print(w, "→", freq[w])

top = max(freq, key=freq.get)
print("Most frequent:", top, freq[top]) """

from datetime import datetime
import random

MENU = {
 "espresso": 2.00,
 "latte": 3.50,
 "tea": 1.80,
 "sandwich": 5.20,
 "cake": 3.00
}

def is_item_available(name):
    if name in MENU:
        return True
    else:
        return False



def checkout(orders):
    subtotal = 0
    grand_total = 0


    now = datetime.now().time()

    start_time = datetime.strptime("15:00", "%H:%M").time()
    end_time = datetime.strptime("17:00", "%H:%M").time()

    for order in orders:
            subtotal += order['line_total']

    if start_time <= now <= end_time:
        for order in orders:
            if order['name'] in ["espresso", "latte", "tea"]:
                grand_total += (order['line_total']*0.9)
            else:
                grand_total += order['line_total']
    else:
        grand_total = subtotal

    return {"subtotal": subtotal, 
            "discount": round(subtotal - grand_total, 2), 
            "grand_total": grand_total}


def build_order():
    orders = []
    for pro,price in MENU.items():
        print(f"{pro:<10} --> {price:>5}")

    order = input("What do you order or (done to finish): ").lower()
    while order != "done":
        if is_item_available(order):
            quantity = -1
            while quantity < 0:
                try:
                    quantity = int(input("Please specify a quantity: "))
                except:
                    print("Please enter a number")
            orders.append({
                            "name": order,
                            "quantity": quantity,
                            "unit_price": MENU[order],
                            "line_total":quantity*MENU[order]
                           })
        else:
            print("Item not on menu")
        order = input("What do you order or (done to finish): ").lower()
    return orders


def generate_receipt(orders, totals):
    random.seed(41)
    receipt_number = random.randint(10000, 99999)
    now = datetime.now()
    string_date = now.strftime("%Y-%m-%d %H:%M")
    print("\n")
    print(f"# {receipt_number} {string_date}")
    print("\n"+30*"-")
    print(f"{'item':<7}{'Qty':>5}{'Unit':>5}{'Line':>5}")
    for order in orders:
        print(f"{order['name']:<7}{order['quantity']:>5}{order['unit_price']:>5}{order['line_total']:>5}")
    print("\n"+30*"-")
    print(f"{'subtotal':<15}{totals['subtotal']:>5}")
    print(f"{'subtotal':<15}{totals['discount']:>5}")
    print(f"{'subtotal':<15}{totals['grand_total']:>5}")

order = build_order()

def save_receipt(text):
    


generate_receipt(order , checkout(order))