import tkinter as tk

# Function
def add():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = num1 + num2
    result_label.config(text=result)

# Main Windows
root = tk.Tk()
root.title("Add two Numbers")

# Create the widgets
num1_label = tk.Label(root,text="Number 1:")
num1_entry = tk.Entry(root)
num2_label = tk.Label(root,text="Number 2:")
num2_entry = tk.Entry(root)
add_button = tk.Button(root,text="Add",command=add)
result_label = tk.Label(root,text="Result: ")

# Layout the widgets
num1_label.grid(row=0,column=0,sticky="e")
num1_entry.grid(row=0,column=1)
num2_label.grid(row=1,column=0,sticky="e")
num2_entry.grid(row=1,column=1)
add_button.grid(row=2,column=0,columnspan=2,pady=10)
result_label.grid(row=3,column=0,columnspan=2)

#Main Loop
root.mainloop()