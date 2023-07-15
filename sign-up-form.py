import tkinter as tk
window=tk.Tk()
window.geometry("400x250")
heading = tk.Label(window, text="Sign Up Form", font=("Helvetica", 16, "bold")).place(x=30,y=10)



email=tk.Label(window,text="Email").place(x=30,y=50)
username=tk.Label(window,text="Username").place(x=30,y=90)
password=tk.Label(window,text="Password").place(x=30,y=130)
confirmpassword=tk.Label(window,text="Confirm Password").place(x=30,y=170)
signupbtn = tk.Button(window, text = "Sign up", activebackground = "green", activeforeground = "blue").place(x = 30, y = 210)
entry1 = tk.Entry(window).place(x = 115, y = 50)
entry2 = tk.Entry(window).place(x = 115, y = 90)
entry3 = tk.Entry(window).place(x = 115, y = 130)
entry4 = tk.Entry(window).place(x = 150, y = 170)
window.mainloop()
