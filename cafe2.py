from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialize main window
root = Tk()
root.title("Cafe Management System")
root.geometry("1000x600")
root.configure(bg="#f5f5f5")

# Menu Items with prices and image paths
menu_items = {
    "Coffee": {"price": 50, "image": r"C:\Users\Adars\Desktop\Mini project\cofeeeeee.jpg"},
    "Tea": {"price": 30, "image": r"C:\Users\Adars\Desktop\Mini project\tea.jpg"},
    "Burger": {"price": 120, "image":r"C:\Users\Adars\Desktop\Mini project\burger.jpg"},
    "Pizza": {"price": 250, "image":r"C:\Users\Adars\Desktop\Mini project\pizza.jpg"},
    "Sandwich": {"price": 100, "image": r"C:\Users\Adars\Desktop\Mini project\sandwitch.jpg",
    "Pasta": {"price": 150, "image": r"C:\Users\Adars\Desktop\Mini project\pasta.jpg"},
    "Cold Drink": {"price": 40, "image": r"C:\Users\Adars\Desktop\Mini project\cold drink.jpeg"},
    "samosa": {"price": 80, "image": r"C:\Users\Adars\Desktop\Mini project\samosa.jpeg"},
    "Ice Cream": {"price": 60, "image": r"C:\Users\Adars\Desktop\Mini project\ice cream.jpeg"},
    
}}




# Variables
qty_vars = {}
item_images = {}

# Functions
def calculate_bill():
    total = 0
    receipt_text.delete(1.0, END)
    receipt_text.insert(END, "********** Receipt **********\n")
    receipt_text.insert(END, f"{'Item':<15}{'Qty':<10}{'Price':<10}{'Total':<10}\n")
    receipt_text.insert(END, "-" * 40 + "\n")
    for item, data in menu_items.items():
        qty = qty_vars[item].get()
        if qty > 0:
            price = data["price"]
            total += qty * price
            receipt_text.insert(END, f"{item:<15}{qty:<10}{price:<10}{qty * price:<10}\n")
    receipt_text.insert(END, "-" * 40 + "\n")
    receipt_text.insert(END, f"Total: {total} INR\n")
    receipt_text.insert(END, "******************************")

def clear_all():
    for var in qty_vars.values():
        var.set(0)
    receipt_text.delete(1.0, END)

def place_order():
    if not any(qty_var.get() > 0 for qty_var in qty_vars.values()):
        messagebox.showerror("Error", "No items selected!")
    else:
        messagebox.showinfo("Success", "Order placed successfully!")
        clear_all()

# Header
header_label = Label(root, text="Cafe Management System", font=("Helvetica", 24, "bold"), bg="#f5f5f5")
header_label.pack(pady=10)





# Menu Frame
menu_frame = Frame(root, bg="#f5f5f5", bd=2, relief=SOLID)
menu_frame.pack(side=LEFT, padx=20, pady=20, fill=Y)

menu_label = Label(menu_frame, text="                      Menu Card", font=("Helvetica", 20, "bold"), bg="#f5f5f5")
menu_label.grid(row=0, column=0, columnspan=2, pady=10)  # Adjust grid placement for the label

# Load item images and create menu in grid layout
row = 1
col = 0
for item, data in menu_items.items():
    # Load the item image
    img = ImageTk.PhotoImage(Image.open(data["image"]).resize((50, 50)))  # Adjust image size
    item_images[item] = img

    # Item Frame
    item_frame = Frame(menu_frame, bg="#f5f5f5", bd=1, relief=SOLID)
    item_frame.grid(row=row, column=col, padx=8, pady=5, sticky="n")

    item_img_label = Label(item_frame, image=img, bg="#f5f5f5")
    item_img_label.pack()

    item_info_label = Label(
        item_frame,
        text=f"{item}\nPrice: {data['price']} INR",
        font=("Helvetica", 14),
        bg="#f5f5f5",
        justify=CENTER
    )
    item_info_label.pack()

    qty_vars[item] = IntVar()
    qty_label = Label(item_frame, text="Qty:", font=("Helvetica", 10), bg="#f5f5f5")
    qty_label.pack()

    qty_entry = Entry(item_frame, textvariable=qty_vars[item], width=5, font=("Helvetica", 12), justify=CENTER)
    qty_entry.pack()

    # Adjust column and row indices for grid placement
    col += 1
    if col == 3:  # Move to the next row after 2 items
        col = 0
        row += 1








# Order & Receipt Frame
order_frame = Frame(root, bg="#f5f5f5", bd=2, relief=SOLID)
order_frame.pack(side=RIGHT, padx=20, pady=10, fill=Y)

receipt_label = Label(order_frame, text="Receipt", font=("Helvetica", 16, "bold"), bg="#f5f5f5")
receipt_label.pack(pady=10)
receipt_text = Text(order_frame, width=40, height=20, font=("Helvetica", 12))
receipt_text.pack(padx=10, pady=10)

# Buttons
button_frame = Frame(root, bg="#f5f5f5")
button_frame.pack(pady=20)

calculate_button = Button(button_frame, text="Calculate Bill", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=calculate_bill)
calculate_button.grid(row=0, column=0, padx=10)

clear_button = Button(button_frame, text="Clear All", font=("Helvetica", 14), bg="#f44336", fg="white", command=clear_all)
clear_button.grid(row=1, column=0, padx=10,pady=30)



# Run the application
root.mainloop()
