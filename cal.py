import tkinter as tk
class CalculatorApp:
def _ _init_ _(self, root):
self.root = root
self.root.title("Simple Calculator")

self.expression = ""
self.result_var = tk.StringVar()
self.result_var.set("0")

# Entry widget to display the expression and result
self.display = tk.Entry(root, textvariable=self.result_var, font=("Arial", 20), bd=5, justify="right")
self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Buttons for numbers and operators
buttons = [
("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
btn = tk.Button(root, text=text, font=("Arial", 16), bd=5, command=lambda t=text: self.on_button_click(t))
btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

 # Clear button
clear_btn = tk.Button(root, text="C", font=("Arial", 16), bd=5, command=self.clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

def on_button_click(self, char):
if char == "=":
try:
result = str(eval(self.expression))
self.result_var.set(result)
except Exception as e:
self.result_var.set("Error")
else:
if char == "C":
self.clear()
else:
self.expression += char
self.result_var.set(self.expression)

def clear(self):
self.expression = ""
self.result_var.set("0")

def main():
root = tk.Tk()
app = CalculatorApp(root)
 root.mainloop()

if _ _name_ _ == "_ _main_ _":
main()