from tkinter import *
from tkinter import messagebox
root = Tk()

l_name = Label(root, text="Name: ")
l_name.grid(row=0, sticky=W)

e_name = Entry(root)
e_name.grid(row=0, column=1)

l_age = Label(root, text="Age: ")
l_age.grid(row=0, column=2, sticky=W)

e_age = Entry(root)
e_age.grid(row=0, column=3)

l_gender = Label(root, text="Gender: ")
l_gender.grid(row=1)

now = None
var_m = IntVar()
var_f = IntVar()

var_gender = [var_m, var_f]


def gen():
    global now, button
    if now is not None:
        button[now].deselect()
    val_gender = [var_gender[i].get() for i in range(2)]
    try:
        now = val_gender.index(1)
    except ValueError:
        now = None


x = ["Male", "Female"]
y = 1

button = [Checkbutton(root, text=x[i], variable=var_gender[i], command=gen) for i in range(2)]
for b in button:
    b.grid(row=1, column=y)
    y += 1

l_height = Label(root, text="Height (meters): ")
l_height.grid(row=2, sticky=W)
e_height = Entry(root)
e_height.grid(row=2, column=1)

l_weight = Label(root, text="Weight (kgs): ")
l_weight.grid(row=3, sticky=W)
e_weight = Entry(root)
e_weight.grid(row=3, column=1)

l_BP_low = Label(root, text="BP Low (mmHg): ")
l_BP_low.grid(row=4, sticky=W)
e_BP_low = Entry(root)
e_BP_low.grid(row=4, column=1)

l_BP_high = Label(root, text="BP High (mmHg): ")
l_BP_high.grid(row=5, sticky=W)
e_BP_high = Entry(root)
e_BP_high.grid(row=5, column=1)

l_pulse = Label(root, text="Pulse Rate (bpm): ")
l_pulse.grid(row=6, sticky=W)
e_pulse = Entry(root)
e_pulse.grid(row=6, column=1)

l_RBC = Label(root, text="RBC Count (million/mm3): ")
l_RBC.grid(row=7, sticky=W)
e_RBC = Entry(root)
e_RBC.grid(row=7, column=1)

l_WBC = Label(root, text="WBC Count (cells/mm3): ")
l_WBC.grid(row=8, sticky=W)
e_WBC = Entry(root)
e_WBC.grid(row=8, column=1)

l_platelets = Label(root, text="Platelets (billion/L): ")
l_platelets.grid(row=9, sticky=W)
e_platelets = Entry(root)
e_platelets.grid(row=9, column=1)

l_HB = Label(root, text="HB (g/dl): ")
l_HB.grid(row=10, sticky=W)
e_HB = Entry(root)
e_HB.grid(row=10, column=1)

l_uric_acid = Label(root, text="Uric Acid (mg/dL): ")
l_uric_acid.grid(row=11, sticky=W)
e_uric_acid = Entry(root)
e_uric_acid.grid(row=11, column=1)

l_cholesterol = Label(root, text="Cholesterol (mg/dL): ")
l_cholesterol.grid(row=12, sticky=W)
e_cholesterol = Entry(root)
e_cholesterol.grid(row=12, column=1)

# *********************** Defination **********************


def generate():
    if e_name.get() == "":
        messagebox.showinfo("Invalid Name", "Please Enter Your Name")
    elif e_age.get() == "":
        messagebox.showinfo("Invalid Age", "Please Enter Your Age")
    elif var_m.get() == 0 and var_f.get() == 0:
        messagebox.showinfo("Invalid Gender", "Please Select Your Gender")
    elif e_height.get() == "" or e_weight.get() == "" or e_BP_low.get() == "" or e_BP_high.get() == "" or e_pulse.get() == "" or e_RBC.get() == "" or e_WBC.get() == "" or e_platelets.get() == "" or e_HB.get() == "" or e_uric_acid.get() == "" or e_cholesterol.get() == "":
        messagebox.showinfo("Invalid Input", "Please Fill The Form")
        try:
            age = int(e_age.get())
        except:
            messagebox.showinfo("Invalid Age", "Age must be an integer")
        try:
            float(e_height.get())
            float(e_weight.get())
            float(e_BP_low.get())
            float(e_BP_high.get())
            float(e_pulse.get())
            float(e_RBC.get())
            float(e_WBC.get())
            float(e_platelets.get())
            float(e_HB.get())
            float(e_uric_acid.get())
            float(e_cholesterol.get())
        except:
            messagebox.showinfo("Invalid Input", "Input must be number")
    else:
        res_BMI = round((float(e_weight.get())/(float(e_height.get())**2)), 2)
        BMI_report = Label(root, text=res_BMI)
        BMI_report.grid(row=14, column=2)

        if 120 >= int(e_BP_low.get()) >= 80 and 140 >= int(e_BP_high.get()) >= 90:
            res_BP = Label(root, text="   Normal   ")
            res_BP.grid(row=15, column=2)
        elif int(e_BP_low.get()) > 120 or int(e_BP_high.get()) > 140:
            res_BP = Label(root, text="   High   ")
            res_BP.grid(row=15, column=2)
        elif int(e_BP_low.get()) < 80 or int(e_BP_high.get()) < 90:
            res_BP = Label(root, text="   Low   ")
            res_BP.grid(row=15, column=2)

        if int(e_age.get()) < 18:
            if 100 >= int(e_pulse.get()) >= 70:
                res_pulse = Label(root, text="   Normal   ")
                res_pulse.grid(row=16, column=2)
            elif int(e_pulse.get()) > 100:
                res_pulse = Label(root, text="   High   ")
                res_pulse.grid(row=16, column=2)
            elif int(e_pulse.get()) < 70:
                res_pulse = Label(root, text="   Low   ")
                res_pulse.grid(row=16, column=2)
        else:
            if 100 >= int(e_pulse.get()) >= 60:
                res_pulse = Label(root, text="   Normal   ")
                res_pulse.grid(row=16, column=2)
            elif int(e_pulse.get()) > 100:
                res_pulse = Label(root, text="   High   ")
                res_pulse.grid(row=16, column=2)
            elif int(e_pulse.get()) < 60:
                res_pulse = Label(root, text="   Low   ")
                res_pulse.grid(row=16, column=2)

        if var_m.get() == 1:
            if 5.72 >= float(e_RBC.get()) >= 4.32:
                res_RBC = Label(root, text="   Normal   ")
                res_RBC.grid(row=17, column=2)
            elif float(e_RBC.get()) > 5.72:
                res_RBC = Label(root, text="   High   ")
                res_RBC.grid(row=17, column=2)
            elif float(e_RBC.get()) < 4.32:
                res_RBC = Label(root, text="   Low   ")
                res_RBC.grid(row=17, column=2)
        elif var_f.get() == 1:
            if 5.03 >= float(e_RBC.get()) >= 3.90:
                res_RBC = Label(root, text="   Normal   ")
                res_RBC.grid(row=17, column=2)
            elif float(e_RBC.get()) > 5.03:
                res_RBC = Label(root, text="   High   ")
                res_RBC.grid(row=17, column=2)
            elif float(e_RBC.get()) < 3.90:
                res_RBC = Label(root, text="   Low   ")
                res_RBC.grid(row=17, column=2)

        if 10800 >= float(e_WBC.get()) >= 4300:
            res_WBC = Label(root, text="   Normal   ")
            res_WBC.grid(row=18, column=2)
        elif float(e_WBC.get()) > 10800:
            res_WBC = Label(root, text="   High   ")
            res_WBC.grid(row=18, column=2)
        elif float(e_WBC.get()) < 4300:
            res_WBC = Label(root, text="   Low   ")
            res_WBC.grid(row=18, column=2)

        if 450 >= float(e_platelets.get()) >= 150:
            res_platelets = Label(root, text="   Normal   ")
            res_platelets.grid(row=19, column=2)
        elif float(e_platelets.get()) > 450:
            res_platelets =Label(root, text="   High   ")
            res_platelets.grid(row=19, column=2)
        elif float(e_platelets.get()) < 150:
            res_platelets =Label(root, text="   Low   ")
            res_platelets.grid(row=19, column=2)

        if var_m.get() == 1:
            if 18 >= float(e_HB.get()) >= 14:
                res_HB = Label(root, text="   Normal   ")
                res_HB.grid(row=20, column=2)
            elif float(e_HB.get()) > 18:
                res_HB = Label(root, text="   High   ")
                res_HB.grid(row=20, column=2)
            elif float(e_HB.get()) < 14:
                res_HB = Label(root, text="   Low   ")
                res_HB.grid(row=20, column=2)
        elif var_f.get() == 1:
            if 16 >= float(e_HB.get()) >= 12:
                res_HB = Label(root, text="   Normal   ")
                res_HB.grid(row=20, column=2)
            elif float(e_HB.get()) > 16:
                res_HB = Label(root, text="   High   ")
                res_HB.grid(row=20, column=2)
            elif float(e_HB.get()) < 12:
                res_HB = Label(root, text="   Low   ")
                res_HB.grid(row=20, column=2)

        if var_m.get() == 1:
            if 7.0 >= float(e_uric_acid.get()) >= 3.4:
                res_HB = Label(root, text="   Normal   ")
                res_HB.grid(row=21, column=2)
            elif float(e_uric_acid.get()) > 7.0:
                res_HB = Label(root, text="   High   ")
                res_HB.grid(row=21, column=2)
            elif float(e_uric_acid.get()) < 3.4:
                res_HB = Label(root, text="   Low   ")
                res_HB.grid(row=21, column=2)
        elif var_f.get() == 1:
            if 6.0 >= float(e_uric_acid.get()) >= 2.4:
                res_HB = Label(root, text="   Normal   ")
                res_HB.grid(row=21, column=2)
            elif float(e_uric_acid.get()) > 6.0:
                res_HB = Label(root, text="   High   ")
                res_HB.grid(row=21, column=2)
            elif float(e_uric_acid.get()) < 2.4:
                res_HB = Label(root, text="   Low   ")
                res_HB.grid(row=21, column=2)

        if int(e_age.get()) < 18:
            if 130 >= float(e_cholesterol.get()) >= 100:
                res_cholesterol = Label(root, text="   Normal   ")
                res_cholesterol.grid(row=22, column=2)
            elif float(e_cholesterol.get()) > 130:
                res_cholesterol = Label(root, text="   High   ")
                res_cholesterol.grid(row=22, column=2)
            elif float(e_cholesterol.get()) < 100:
                res_cholesterol = Label(root, text="   Low   ")
                res_cholesterol.grid(row=22, column=2)
        elif int(e_age.get()) > 18:
            if 240 >= float(e_cholesterol.get()) >= 200:
                res_cholesterol = Label(root, text="   Normal   ")
                res_cholesterol.grid(row=22, column=2)
            elif float(e_cholesterol.get()) > 240:
                res_cholesterol = Label(root, text="   High   ")
                res_cholesterol.grid(row=22, column=2)
            elif float(e_cholesterol.get()) < 200:
                res_cholesterol = Label(root, text="   Low   ")
                res_cholesterol.grid(row=22, column=2)


def space():
    e_name.delete(0, END)
    e_name.insert(0, "")

    e_age.delete(0, END)
    e_age.insert(0, "")

    var_m.set(0)
    var_f.set(0)

    e_height.delete(0, END)
    e_height.insert(0, "")

    e_weight.delete(0, END)
    e_weight.insert(0, "")

    e_BP_low.delete(0, END)
    e_BP_low.insert(0, "")

    e_BP_high.delete(0, END)
    e_BP_high.insert(0, "")

    e_pulse.delete(0, END)
    e_pulse.insert(0, "")

    e_RBC.delete(0, END)
    e_RBC.insert(0, "")

    e_WBC.delete(0, END)
    e_WBC.insert(0, "")

    e_platelets.delete(0, END)
    e_platelets.insert(0, "")

    e_HB.delete(0, END)
    e_HB.insert(0, "")

    e_uric_acid.delete(0, END)
    e_uric_acid.insert(0, "")

    e_cholesterol.delete(0, END)
    e_cholesterol.insert(0, "")

    blank1 = Label(root, text="                                    ")
    blank2 = Label(root, text="                                    ")
    blank3 = Label(root, text="                                    ")
    blank4 = Label(root, text="                                    ")
    blank5 = Label(root, text="                                    ")
    blank6 = Label(root, text="                                    ")
    blank7 = Label(root, text="                                    ")
    blank8 = Label(root, text="                                    ")
    blank9 = Label(root, text="                                    ")
    blank1.grid(row=14, column=2)
    blank2.grid(row=15, column=2)
    blank3.grid(row=16, column=2)
    blank4.grid(row=17, column=2)
    blank5.grid(row=18, column=2)
    blank6.grid(row=19, column=2)
    blank7.grid(row=20, column=2)
    blank8.grid(row=21, column=2)
    blank9.grid(row=22, column=2)


def about():
    messagebox.showinfo("ABOUT", "Name: Utsab Sen\nEmail: utsabsen1999@gmail.com\nLOVELY PROFESSIONAL UNIVERSITY\n\t<3 INDIA <3")


button_reset = Button(root, text="Reset", command=space)
button_reset.grid(row=9, rowspan=2, column=3)

button_about = Button(root, text="        ABOUT        ", command=about)
button_about.grid(row=9, rowspan=2, column=3)

button_generate = Button(root, text="Generate Report", command=generate)
button_generate.grid(row=11, rowspan=2, column=3)

l_space = Label(root, text=" ")
l_space.grid(row=13)

l_BMI = Label(root, text="BMI (Body Mass Index): ")
l_BMI.grid(row=14, columnspan=2, sticky=W)
l_BMI_res = Label(root, text="                                       ", borderwidth=3, height=2, relief="groove")
l_BMI_res.grid(row=14, column=2)

l_BP = Label(root, text="BP: ")
l_BP.grid(row=15, columnspan=2, sticky=W)
l_BP_res = Label(root, text="                                       ", borderwidth=3, height=2, relief="groove")
l_BP_res.grid(row=15, column=2)

l_pulse_rate = Label(root, text="Pulse Rate: ")
l_pulse_rate.grid(row=16, columnspan=2, sticky=W)
l_pulse_rate_res = Label(root, text="                                       ", borderwidth=3, height=2, relief="groove")
l_pulse_rate_res.grid(row=16, column=2)

l_RBC_count = Label(root, text="RBC Count: ")
l_RBC_count.grid(row=17, columnspan=2, sticky=W)
l_RBC_count_res = Label(root, text="                                       ", borderwidth=3, height=2, relief="groove")
l_RBC_count_res.grid(row=17, column=2)

l_WBC_count = Label(root, text="WBC Count: ")
l_WBC_count.grid(row=18, columnspan=2, sticky=W)
l_WBC_count_res = Label(root, text="                                       ", borderwidth=3, height=2, relief="groove")
l_WBC_count_res.grid(row=18, column=2)

l_platelets_count = Label(root, text="Platelets: ")
l_platelets_count.grid(row=19, columnspan=2, sticky=W)
l_platelets_count_res = Label(root, text="                                       ", borderwidth=3, height=2, relief="groove")
l_platelets_count_res.grid(row=19, column=2)

l_HB_count = Label(root, text="HB: ")
l_HB_count.grid(row=20, columnspan=2, sticky=W)
l_HB_count_res = Label(root, text="                                       ", borderwidth=3, height=2, relief="groove")
l_HB_count_res.grid(row=20, column=2)

l_uric_acid_count = Label(root, text="Uric Acid: ")
l_uric_acid_count.grid(row=21, columnspan=2, sticky=W)
l_uric_acid_count_res = Label(root, text="                                       ", borderwidth=3, height=2, relief="groove")
l_uric_acid_count_res.grid(row=21, column=2)

l_cholesterol_count = Label(root, text="Cholesterol: ")
l_cholesterol_count.grid(row=22, columnspan=2, sticky=W)
l_cholesterol_count_res = Label(root, text="                                       ", borderwidth=3, height=2, relief="groove")
l_cholesterol_count_res.grid(row=22, column=2)


root.title("FITNESS CALCULATOR")
root.mainloop()
