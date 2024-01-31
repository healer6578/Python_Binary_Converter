import tkinter as tk

def decimal_to_binary():
    try:
        decimal_num = int(input_field.get())
        binary_num = bin(decimal_num).replace("0b", "")
        output_label.config(text=f"Binary: {binary_num}")
    except ValueError:
        show_error("Invalid input. Please enter a decimal number.")

def binary_to_decimal():
    try:
        binary_num = input_field.get()
        decimal_num = int(binary_num, 2)
        output_label.config(text=f"Decimal: {decimal_num}")
    except ValueError:
        show_error("Invalid input. Please enter a valid binary number.")

def binary_to_words():
    try:
        binary_num = input_field.get()
        decimal_num = int(binary_num, 2)
        words = convert_to_words(decimal_num)
        output_label.config(text=f"Decimal: {decimal_num}\nWords: {words}")
    except ValueError:
        show_error("Invalid input. Please enter a valid binary number.")

def words_to_binary():
    try:
        words = input_field.get()
        binary_num = convert_to_binary(words)
        output_label.config(text=f"Binary: {binary_num}")
    except ValueError:
        show_error("Invalid input. Please enter a valid word representation.")

def convert_to_words(decimal_num):
    if decimal_num == 0:
        return "Zero"
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return ones[decimal_num]

def convert_to_binary(words):
    binary_num = ""
    for char in words:
        binary_num += format(ord(char), '08b')  # Convert each character to 8-bit binary representation
    return binary_num

def show_error(message):
    output_label.config(text=message, fg="red")

def clear_output():
    output_label.config(text="")

root = tk.Tk()
root.title("Binary-Decimal Converter")

menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

decimal_to_binary_button = tk.Button(menu_frame, text="Decimal to Binary", command=decimal_to_binary)
decimal_to_binary_button.pack(side=tk.LEFT, padx=5)

binary_to_decimal_button = tk.Button(menu_frame, text="Binary to Decimal", command=binary_to_decimal)
binary_to_decimal_button.pack(side=tk.LEFT, padx=5)

binary_to_words_button = tk.Button(menu_frame, text="Binary to Words", command=binary_to_words)
binary_to_words_button.pack(side=tk.LEFT, padx=5)

words_to_binary_button = tk.Button(menu_frame, text="Words to Binary", command=words_to_binary)
words_to_binary_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(root, text="Clear", command=clear_output)
clear_button.pack(pady=5)

input_field = tk.Entry(root)
input_field.pack(pady=5)

output_label = tk.Label(root, text="", pady=10)
output_label.pack()

root.mainloop()
