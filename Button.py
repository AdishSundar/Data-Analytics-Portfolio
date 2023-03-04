import tkinter as tk
import subprocess

root = tk.Tk()
root.geometry("1500x1500")
root.configure(bg="beige")

def on_button_click():
    subprocess.run(["python", "Survey.py"])
    button.configure(fg="teal")

# Create a Label widget for the title
title_label = tk.Label(root, text="Sustainability", font=("Helvetica", 50), bg="green", justify="center")
title_label.grid(row=0, column=0, columnspan=2, padx=575, pady=250)

button = tk.Button(root, text="Water Usage - Sprinkler Recommendation!", command=on_button_click, bg="#00bfff", fg="black", font=("Helvetica", 16), relief="raised", bd=5)
button.config(height=3, width=50)

# Add custom styling to the button
button.config(highlightbackground="#00bfff", highlightthickness=5)
button.config(activebackground="#009acd", activeforeground="white")

# Position the button
button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()