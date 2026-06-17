from tkinter import *
import pyqrcode
from fpdf import FPDF
from tkinter import messagebox

class PDFCV(FPDF):
    def header(self):
        #image
        self.image("web.png",10,8,33,title="Portfolio site")#title #x coord #y coord #width 
        #link
        website=entry_website.get()
         # Move the cursor to the right of the QR code
        self.set_xy(50, 20)      # x=50, y=20
        self.cell(
        0,10,txt="Click here ",ln=True,link=website #width #height #ln (line break , After writing this cell, move the cursor to the next line.)
    )
    def footer(self):
        pass

    def generate_cv(self,name,email,phone_num,address,skills,work_experience,education,about_me):
        self.set_font("Arial","B",26)#size
        self.add_page()
        self.ln(20) #for some space

        #displaying the name
        self.set_font("Arial","B",26)#size
        self.cell(0,10,name,new_x="LMARGIN",new_y="NEXT",align="C")#width #height

        #adding contact information header
        self.set_font("Arial","B",12)#size
        self.cell(0,10,"Contact Information",new_x="LMARGIN",new_y="NEXT",align="L")#width #height

        #adding the contact information
        self.set_font("Arial","",10)#bold #size
        self.cell(0,5,"Email: {}".format(email),new_x="LMARGIN",new_y="NEXT")#width #height
        self.cell(0,5,"Phone: {}".format(email),new_x="LMARGIN",new_y="NEXT")#width #height
        self.cell(0,5,"Address: {}".format(email),new_x="LMARGIN",new_y="NEXT")#width #height

        #skills
        self.ln(10)# give a gap

        self.set_font("Arial","",12)#bold #size
        self.cell(0,12,"Skills",new_x="LMARGIN",new_y="NEXT",align="L")#width #height

        #adding skills
        self.set_font("Arial","",10)#bold #size
        for s in skills:
            self.cell(0,5,"-{}".format(s),new_x="LMARGIN",new_y="NEXT",align="L")#width #height

        #work experience
        self.ln(10)# give a gap

        self.set_font("Arial","B",12)#bold #size
        self.cell(0,12,"Work experience",new_x="LMARGIN",new_y="NEXT",align="L")#width #height

        #adding work experience
        self.set_font("Arial","",10)#bold #size
        for w in work_experience:
            self.cell(0,5,"{}: {}".format(w["title"],w["description"]),new_x="LMARGIN",new_y="NEXT")#width #height

        #education
        self.ln(10)# give a gap

        self.set_font("Arial","B",12)#bold #size
        self.cell(0,12,"education",new_x="LMARGIN",new_y="NEXT",align="L")#width #height

        #adding education
        self.set_font("Arial","",10)#bold #size
        for e in education:
            self.cell(0,5,"{}: {}".format(e["degree"],e["university"]),new_x="LMARGIN",new_y="NEXT")#width #height

        #About me
        self.ln(10)# give a gap

        self.set_font("Arial","B",12)#bold #size
        self.cell(0,12,"About Me",new_x="LMARGIN",new_y="NEXT",align="L")#width #height

        #adding about me
        self.set_font("Arial","",10)#bold #size
        self.multi_cell(0,5,"{}".format(about_me),new_x="LMARGIN",new_y="NEXT")#width #height

        self.output("cv1.pdf")
def generate_pdf():
    name=entry_name.get()
    email=entry_email.get()
    phone_num=entry_phone.get()
    address=entry_address.get()
    website=entry_website.get()
    skills=entry_skills.get("1.0",END).strip().split('\n')
    work_experience=[]
    education=[]

    work_experience_lines=entry_experience.get("1.0",END).strip().split('\n') # gets every thing user typed
    for line in work_experience_lines:
        if ":" in line:
            title,description=line.split(":")
            work_experience.append({'title':title.strip(),'description':description.strip()})

    education_lines=entry_education.get("1.0",END).strip().split('\n')
    for line in education_lines:
        if ":" in line:
            degree,university=line.split(":") 
            education.append({'degree':degree.strip(),'university':university.strip()})

    about_me=entry_about_me.get("1.0",END)

    #create qr code
    website=entry_website.get()
    qrcode=pyqrcode.create(website)
    qrcode.png("web.png",scale=6) #name  #scale

    if not name or not email or not phone_num or not address or not skills or not education or not work_experience or not about_me:
        messagebox.showerror("Error","Please fill in all the details") #title #content
        return

    cv=PDFCV()
    cv.generate_cv(name,email,phone_num,address,skills,work_experience,education,about_me)

window=Tk()
window.title("CV Generator")

label_name=Label(window,text="Name: ")
label_name.pack()
entry_name=Entry(window)
entry_name.pack()

label_email=Label(window,text="Email: ")
label_email.pack()
entry_email=Entry(window)
entry_email.pack()

label_phone=Label(window,text="Phone number: ")
label_phone.pack()
entry_phone=Entry(window)
entry_phone.pack()

label_address=Label(window,text="Address: ")
label_address.pack()
entry_address=Entry(window)
entry_address.pack()

label_website=Label(window,text="Website: ")
label_website.pack()
entry_website=Entry(window)
entry_website.pack()

#creating a text box for skills
label_skills=Label(window,text="Skills(Enter one skill per line)")
label_skills.pack()
entry_skills=Text(window,height=5)
entry_skills.pack()

#creating a text box for education
label_education=Label(window,text="education(Enter one per line format    Degree:University)")
label_education.pack()
entry_education=Text(window,height=5)
entry_education.pack()

#creating a text box for experience
label_experience=Label(window,text="Experience(Enter one per line format    Job title:description)")
label_experience.pack()
entry_experience=Text(window,height=5)
entry_experience.pack()

#creating a text box for about me
label_about_me=Label(window,text="About me")
label_about_me.pack()
entry_about_me=Text(window,height=5)
entry_about_me.pack()

button_generate=Button(window,text="Generate CV",command=generate_pdf)
button_generate.pack()

window.mainloop()