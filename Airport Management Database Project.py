#===My First Python Project===
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Airport:
    def __init__(self,root):
        self.root=root
        self.root.title("Airport Management Database")
        self.root.geometry("1980x1080+0+0")

        #===Variable===
        self.Fno_var=StringVar()
        self.Fname_var=StringVar()
        self.Airline_var=StringVar()
        self.Destination_var=StringVar()
        self.DepartTime_var=StringVar()
        self.PassID_var=StringVar()
        self.TicID_var=StringVar()
        
        lbltitle=Label(self.root,bd=15,relief=RIDGE,text="🛩AIRPORT MANAGEMENT SYSTEM🛩",fg="dark orange",font=("hp simplified",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #===DateFrame===
        DataFrame=Frame(self.root,bd=15,relief=RIDGE)
        DataFrame.place(x=0,y=110,width=1270,height=300)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,pady=25,fg="dark orange",font=("lucida calligraphy",12, "bold"),text="Flight Information")
        DataFrameLeft.place(x=0,y=5,width=800,height=260)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=2,fg="dark orange",font=("lucida calligraphy",12, "bold"),text="Flight Data")
        DataFrameRight.place(x=805,y=4.5,width=430,height=260)

        #===ButtonsFrame===
        ButtonFrame=Frame(self.root,bd=10,relief=RIDGE)
        ButtonFrame.place(x=0,y=415,width=1270,height=55)

        BtnAddData=Button(ButtonFrame,command=self.insert_data,text="Insert Data",font=("hp simplified",12,"bold"),width=20,bg="Dark orange",fg="white")
        BtnAddData.grid(row=0,column=0,padx=30)

        BtnShowData=Button(ButtonFrame,command=self.show_data,text="Show Data",font=("hp simplified",12,"bold"),width=20,bg="Dark orange",fg="white")
        BtnShowData.grid(row=0,column=1,padx=15)

        BtnUpdateData=Button(ButtonFrame,command=self.update_data,text="Update Data",font=("hp simplified",12,"bold"),width=20,bg="Dark orange",fg="white")
        BtnUpdateData.grid(row=0,column=2,padx=15)

        BtnDeleteData=Button(ButtonFrame,command=self.delete_data,text="Delete Data",font=("hp simplified",12,"bold"),width=20,bg="Dark orange",fg="white")
        BtnDeleteData.grid(row=0,column=3,padx=15)

        BtnReset=Button(ButtonFrame,command=self.reset,text="Reset",font=("hp simplified",12,"bold"),width=20,bg="Dark orange",fg="white")
        BtnReset.grid(row=0,column=4,padx=15)

        BtnExit=Button(ButtonFrame,command=self.Exit,text="Exit",font=("hp simplified",12,"bold"),width=20,bg="Dark orange",fg="white")
        BtnExit.grid(row=0,column=5,padx=15)

        #===DetailsFrame===
        DetailsFrame=Frame(self.root,bd=10,relief=RIDGE)
        DetailsFrame.place(x=0,y=470,width=1270,height=190)

        TableFrame=Frame(DetailsFrame,bd=6,relief=RIDGE)
        TableFrame.place(x=0,y=2,width=1250,height=170)

        yscroll=ttk.Scrollbar(TableFrame,orient=VERTICAL)
        self.airport_table=ttk.Treeview(TableFrame,column=("F_No","F_Name","Airline","Destination",'Depart_Time',"Passenger_ID","Ticket_ID"),yscrollcommand=yscroll.set)
        yscroll.pack(side=RIGHT,fill=Y)
        yscroll.config(command=self.airport_table.yview)
        
        self.airport_table.heading("F_No",text="F_No")
        self.airport_table.heading("F_Name",text="F_Name")
        self.airport_table.heading("Airline",text="Airline")
        self.airport_table.heading("Destination",text="Destination")
        self.airport_table.heading("Depart_Time",text="Depart_Time")
        self.airport_table.heading("Passenger_ID",text="Passenger_ID")
        self.airport_table.heading("Ticket_ID",text="Ticket_ID")
        self.airport_table["show"]="headings"
        self.airport_table.pack(fill=BOTH,expand=1)

        self.airport_table.column("F_No",width=100)
        self.airport_table.column("F_Name",width=100)
        self.airport_table.column("Airline",width=100)
        self.airport_table.column("Destination",width=100)
        self.airport_table.column("Depart_Time",width=100)
        self.airport_table.column("Passenger_ID",width=100)
        self.airport_table.column("Ticket_ID",width=100)

        #===DataFrameLeft===
        lblFNo=Label(DataFrameLeft,text="Flight No",font=("arial rounded mt",15,"bold"),padx=2,pady=5)
        lblFNo.grid(row=0,column=0)
        txtFNo=Entry(DataFrameLeft,font=("arial rounded mt",15,"bold"),textvariable=self.Fno_var,width=20)
        txtFNo.grid(row=0,column=1)

        lblFName=Label(DataFrameLeft,text="Flight Name",font=("arial rounded mt",15,"bold"),padx=2,pady=5)
        lblFName.grid(row=1,column=0)
        txtFName=Entry(DataFrameLeft,font=("arial rounded mt",15,"bold"),textvariable=self.Fname_var,width=20)
        txtFName.grid(row=1,column=1)

        lblAirline=Label(DataFrameLeft,text="Airline",font=("arial rounded mt",15,"bold"),padx=2,pady=5)
        lblAirline.grid(row=2,column=0)
        txtAirline=Entry(DataFrameLeft,font=("arial rounded mt",15,"bold"),textvariable=self.Airline_var,width=20)
        txtAirline.grid(row=2,column=1)

        lblDestination=Label(DataFrameLeft,text="Destination",font=("arial rounded mt",15,"bold"),padx=2,pady=5)
        lblDestination.grid(row=3,column=0)
        txtDestination=Entry(DataFrameLeft,font=("arial rounded mt",15,"bold"),textvariable=self.Destination_var,width=20)
        txtDestination.grid(row=3,column=1)

        lblDepartTime=Label(DataFrameLeft,text="Departure/Arrival Time",font=("arial rounded mt",15,"bold"),padx=2,pady=5)
        lblDepartTime.grid(row=0,column=2)
        txtDepartTime=Entry(DataFrameLeft,font=("arial rounded mt",15,"bold"),textvariable=self.DepartTime_var,width=15)
        txtDepartTime.grid(row=0,column=3)

        lblPID=Label(DataFrameLeft,text="Passenger ID",font=("arial rounded mt",15,"bold"),padx=2,pady=5)
        lblPID.grid(row=1,column=2)
        txtPID=Entry(DataFrameLeft,font=("arial rounded mt",15,"bold"),textvariable=self.PassID_var,width=15)
        txtPID.grid(row=1,column=3)

        lblTID=Label(DataFrameLeft,text="Ticket ID",font=("arial rounded mt",15,"bold"),padx=2,pady=5)
        lblTID.grid(row=2,column=2)
        txtTID=Entry(DataFrameLeft,font=("arial rounded mt",15,"bold"),textvariable=self.TicID_var,width=15)
        txtTID.grid(row=2,column=3)

        #===DataFrameRight===
        self.txtFlightData=Text(DataFrameRight,font=("arial rounded mt",12,"bold"),width=44,height=11,padx=2,pady=5)
        self.txtFlightData.grid(row=0,column=0)

        self.fetch_data()
        self.airport_table.bind("<ButtonRelease-1>",self.get_cursor)
    
    def insert_data(self):
        mycon=mysql.connector.connect(host='localhost', user='root', passwd='Ar@080704', database='mydb')
        cursor=mycon.cursor()
        cursor.execute("insert into flight_details values(%s,%s,%s,%s,%s,%s,%s)",(
            self.Fno_var.get(),
            self.Fname_var.get(),
            self.Airline_var.get(),
            self.Destination_var.get(),
            self.DepartTime_var.get(),
            self.PassID_var.get(),
            self.TicID_var.get()
            ))
        mycon.commit()
        self.fetch_data()
        mycon.close()
        messagebox.showinfo("Success","Flight Record has been inserted")

    def fetch_data(self):
        mycon=mysql.connector.connect(host='localhost', user='root', passwd='Ar@080704', database='mydb')
        cursor=mycon.cursor()
        cursor.execute("select * from flight_details")
        row=cursor.fetchall()
        if len(row)!=0:
            self.airport_table.delete(*self.airport_table.get_children())
            for i in row:
                self.airport_table.insert("",END,values=i)
        mycon.close() 

    def get_cursor(self,event=""):
        cursor_row=self.airport_table.focus()
        content=self.airport_table.item(cursor_row)
        row=content['values'] 

        self.Fno_var.set(row[0]),
        self.Fname_var.set(row[1]),
        self.Airline_var.set(row[2]),
        self.Destination_var.set(row[3]),
        self.DepartTime_var.set(row[4]),
        self.PassID_var.set(row[5]),
        self.TicID_var.set(row[6])

    def show_data(self):
        self.txtFlightData.insert(END,"Flight No\t\t" + self.Fno_var.get() + "\n")
        self.txtFlightData.insert(END,"Flight Name\t\t" + self.Fname_var.get() + "\n") 
        self.txtFlightData.insert(END,"Airline\t\t" + self.Airline_var.get() + "\n")   
        self.txtFlightData.insert(END,"Destination\t\t" + self.Destination_var.get() + "\n")
        self.txtFlightData.insert(END,"Depature/Arrival Time\t\t" + self.DepartTime_var.get() + "\n")
        self.txtFlightData.insert(END,"Passenger Identification\t\t" + self.PassID_var.get() + "\n")
        self.txtFlightData.insert(END,"Ticket Identification\t\t" + self.TicID_var.get() + "\n")

    def update_data(self):
        mycon=mysql.connector.connect(host='localhost', user='root', passwd='Ar@080704', database='mydb')
        cursor=mycon.cursor()
        cursor.execute("update flight_details set F_Name=%s,Airline=%s,Destination=%s,Depart_Time=%s,Passenger_ID=%s,Ticket_ID=%s where F_No=%s",(
            self.Fname_var.get(),
            self.Airline_var.get(),
            self.Destination_var.get(),
            self.DepartTime_var.get(),
            self.PassID_var.get(),
            self.TicID_var.get(),
            self.Fno_var.get()
            ))
        mycon.commit()
        self.fetch_data()
        self.reset()
        mycon.close()
        messagebox.showinfo("Success","Flight Record has been updated")

    def delete_data(self):
        if self.Fno_var.get()=="" or self.TicID_var.get()=="":
            messagebox.showerror("Error","Please select a Flight Record!")
        else:
          mycon=mysql.connector.connect(host='localhost', user='root', passwd='Ar@080704', database='mydb')
          cursor=mycon.cursor()
          query="delete from flight_details where F_No=%s"
          value=(self.Fno_var.get(),)
          cursor.execute(query,value) 
          Input=messagebox.askyesno("Flight Record Deletion","Do you want to commit?")
          if Input>0:
              mycon.commit()
              messagebox.showinfo("Commit","Flight Record has been deleted")
          else:
              mycon.rollback()
              messagebox.showinfo("Rollback","Flight Record has not been deleted")
          self.fetch_data()
          self.reset()
          mycon.close()        

    def reset(self):
        self.Fno_var.set(""),
        self.Fname_var.set(""),
        self.Airline_var.set(""),
        self.Destination_var.set(""),
        self.DepartTime_var.set(""),
        self.PassID_var.set(""),
        self.TicID_var.set(""),
        self.txtFlightData.delete("1.0",END)

    def Exit(self):
        Exit=messagebox.askyesno("Airport Management Database","Do you want to exit?")
        if Exit>0:
            self.root.destroy()
            
        else:
            return

root=Tk()
ob=Airport(root)
root.mainloop()
