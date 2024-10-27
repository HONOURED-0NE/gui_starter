import  tkinter as tk
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_let= [random.choice(letters) for x in range(random.randint(8,10))]
    pass_sym = [random.choice(symbols) for x in range(random.randint(2,4))]
    pass_num = [random.choice(numbers) for x in range(random.randint(2,4))]

    password_entry.delete(0, 'end')
    pass_list = pass_let + pass_num + pass_sym
    random.shuffle(pass_list)
    password = "".join(pass_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title='Password copied', message= 'Password has been copied to clipbaord')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_info():
    website = website_entry.get()
    credentials = credentials_entry.get()
    password = password_entry.get()
    
    if len(website)==0 or len(password)==0 or len(credentials)==0:
        messagebox.showinfo(title='Failure', message= 'Please dont leave any fields empty!')
    else:    
        is_ok = messagebox.askokcancel(title=website, message=f'Click ok to confirm your credentials')
        if is_ok:
            with open("./password_manager/data.docx", mode='a') as info:
                info.write(f"{website} | {credentials} | {password}\n")
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')

    
    


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

canvas  = tk.Canvas(width=200, height=200)
lock = tk.PhotoImage(file='./password_manager/logo.png')
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = tk.Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


credentials_label = tk.Label(text="Email/Username:")
credentials_label.grid(column=0, row=2)

credentials_entry =tk.Entry(width=51)
credentials_entry.grid(column=1, row=2, columnspan=2)
credentials_entry.insert(0, "rahmanmide271@gmail.com")


password_label =tk.Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry= tk.Entry(width=33)
password_entry.grid(column=1, row=3)


gen_pass = tk.Button(text="Generate Password", highlightthickness=2, command=generate_password)
gen_pass.grid(column=2 , row=3)

add_but = tk.Button(text="Add", width=44,highlightthickness=1, command=get_info)
add_but.grid(column=1, row=4, columnspan=2)



window.mainloop()
