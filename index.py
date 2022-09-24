from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Cardiovascular Disease Detector")
root.geometry("600x600")
root.config(bg="brown2")
icon = PhotoImage(file="medical-logo.png")
root.iconphoto(False, icon)
qv1 = StringVar(value="0")
q1 = Label(
    root, text="Do you experience shortness of breath during routine activities?", bg="brown2")
q1r1 = Radiobutton(root, text="Yes", variable=qv1, value="1", bg="brown2")
q1r2 = Radiobutton(root, text="No", variable=qv1, value="2", bg="brown2")
q1.pack()
q1r1.pack()
q1r2.pack()

qv2 = StringVar(value="0")
q2 = Label(
    root, text="Do you have swelling in the feet/ankles/legs(shoes feel tighter) or abdomen", bg="brown2")
q2r1 = Radiobutton(root, text="Yes", variable=qv2, value="1", bg="brown2")
q2r2 = Radiobutton(root, text="No", variable=qv2, value="2", bg="brown2")
q2.pack()
q2r1.pack()
q2r2.pack()

qv3 = StringVar(value="0")
q3 = Label(
    root, text="Do you feel any of these symptoms - confusion, disorientation or loss of memory?", bg="brown2")
q3r1 = Radiobutton(root, text="Yes", variable=qv3, value="1", bg="brown2")
q3r2 = Radiobutton(root, text="No", variable=qv3, value="2", bg="brown2")
q3.pack()
q3r1.pack()
q3r2.pack()

qv4 = StringVar(value="0")
q4 = Label(
    root, text="Do you experience shortness of breath while at rest/lying down?", bg="brown2")
q4r1 = Radiobutton(root, text="Yes", variable=qv4, value="1", bg="brown2")
q4r2 = Radiobutton(root, text="No", variable=qv4, value="2", bg="brown2")
q4.pack()
q4r1.pack()
q4r2.pack()

qv5 = StringVar(value="0")
q5 = Label(root, text="Do you experience persistent wheezing / coughing that produces White or pink blood tinged mucus?", bg="brown2")
q5r1 = Radiobutton(root, text="Yes", variable=qv5, value="1", bg="brown2")
q5r2 = Radiobutton(root, text="No", variable=qv5, value="2", bg="brown2")
q5.pack()
q5r1.pack()
q5r2.pack()


def calculate():
    score = 0
    if qv1.get() == "1":
        score += 10
    if qv2.get() == "1":
        score += 10
    if qv2.get() == "1":
        score += 10
    if qv3.get() == "1":
        score += 10
    if qv4.get() == "1":
        score += 10
    if qv5.get() == "1":
        score += 10
    if score <= 10:
        messagebox.showinfo("Report", "You Don't Need To Visit a Doctor.")
    elif score > 10 and score <= 30:
        messagebox.showinfo(
            "Report", "You Might perhaps have to visit a doctor")
    else:
        messagebox.showinfo(
            "Report", "I Strongly Advise You To Visit The Doctor")


btn = Button(root, text="Check", bg="brown2", command=calculate)
btn.pack()
root.mainloop()
