
import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("My First App")
app.geometry("350x200")

tk.Label(
    app, text="Hello! My Windows EXE works.",
    font=("Arial", 12)
).pack(pady=30)

tk.Button(
    app, text="Click Me",
    command=lambda: messagebox.showinfo("App", "Success!")
).pack()

app.mainloop()
