import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen_var.set(result)
        except:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen.get() + text)

root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
