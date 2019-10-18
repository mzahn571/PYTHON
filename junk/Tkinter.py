import Tkinter as tk
# adapted from http://www.python-course.eu/python_tkinter.php
counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
def restart(*args, **kwargs):
  from kernilis.utils import restart_program
  restart_program()
print("Hello from tkinter counter example!")
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
button = tk.Button(root, text='Restart Program', width=25, command=restart)
button.pack()
root.mainloop()