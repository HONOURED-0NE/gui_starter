import tkinter as tk
window = tk.Tk()
window.title('Mile to Km Converter')
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)


input = tk.Entry(width=10)
input.grid(column=2, row=1)

miles = tk.Label(text="miles", font=('Ariel', 10 ))
miles.grid(column=3, row=1)

def conv():
    miless =float(input.get())
    km = miless*1.609
    result.config(text= km)
    

is_equal_to = tk.Label(text='is equal to', font=('Ariel', 10))
is_equal_to.grid(column=1, row=2)

result  = tk.Label(text=' 0',font=('Ariel', 10) )
result.grid(column=2, row=2)

conv_but = tk.Button(text='Convert', command=conv)
conv_but.grid(column=2, row=3)






















window.mainloop()

