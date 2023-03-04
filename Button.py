import tkinter as tk
import subprocess

root = tk.Tk()
root.geometry("1500x1500")

# Set the background image to a water image
background_image = tk.PhotoImage(file="/Users/adishsundar/Desktop/Untitled design (7).png")
background_label = tk.Label(root, image=background_image)
background_label.place(relx=0.5, rely=0.5, anchor="center")


# Add a raindrop image as an overlay on top of the water image

def on_button_click():
    subprocess.run(["python", "Survey.py"])
    button.configure(fg="teal")


# Create a Label widget for the title

raindrop_image = tk.PhotoImage(file="/Users/adishsundar/Desktop/Screen Shot 2023-03-04 at 3.46.19 PM.png")

# Scale the image to half its original size
raindrop_image = raindrop_image.subsample(2)

# Create the Button widget with the raindrop image
button = tk.Button(root, text="Water Usage - Sprinkler Recommendation!",
                   command=on_button_click, image=raindrop_image,
                   font=("Helvetica", 16), relief="flat", bd=0)

# Set the size of the button to match the size of the image
button.config(width=raindrop_image.width(), height=raindrop_image.height())

# Add custom styling to the button
button.config(highlightthickness=0, highlightbackground=root.cget("bg"), highlightcolor=root.cget("bg"))
button.config(borderwidth=0, relief="flat", bd=0)
button.config(background="blue", foreground="white")

# Position the button
button.place(relx=0.5, rely=.7, anchor="center")

root.mainloop()
