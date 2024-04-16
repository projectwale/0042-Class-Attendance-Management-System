from flask import Flask, flash, session, redirect,url_for
from flask import render_template,request,send_file
import pymysql
from mark_attendance import mark_your_attendance,mark_your_attendance_singlepic
from register1 import register_yourself
# import json ,jsonify
import pathlib
import os
import pandas as pd
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import pandas as pd 
from werkzeug.utils import secure_filename

# import pandas as pd

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] ='static/teacher'

app.config['UPLOAD_FOLDER1'] ='static/users'

app.config['UPLOAD_FOLDER2'] ='static/uploadimage'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.secret_key = 'any random string'




##################################   Mail to  #########################################################################

def sendemailtouser(usermail,ogpass):   
    fromaddr = "pranalibscproject@gmail.com"
    toaddr = usermail
   
    #instance of MIMEMultipart 
    msg = MIMEMultipart() 
  
    # storing the senders email address   
    msg['From'] = fromaddr 
  
    # storing the receivers email address  
    msg['To'] = toaddr 
  
    # storing the subject  
    msg['Subject'] = "WEB_ATTENDANCE SYSTEM"
  
    # string to store the body of the mail 
    body = ogpass
  
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
  
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
  
    # start TLS for security 
    s.starttls() 
  
    # Authentication 
    s.login(fromaddr, "wkwfgosewcljcpqh") 
  
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
  
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
  
    # terminating the session 
    s.quit()
    



##################################   Mail to blooddoner #########################################################################


##################################   database connection #########################################################################
def dbConnection():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="root", database="040-weattendance", autocommit=True)
        return connection
    except:
        print("Something went wrong in database Connection")

def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")

con = dbConnection()
cursor = con.cursor()

################################## database connection #########################################################################



##################################  ngo login register #########################################################################
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        
        return render_template("main.html") 
    return render_template("main.html") 
        
        
@app.route('/SessionHandle1',methods=['POST','GET'])
def SessionHandle1():
    if request.method == "POST":
        username= request.form.get("username")
        password= request.form.get("password")
        if username=="admin" and password=="admin":
             session['name'] = username
             flash('you are sucessfully login...')
             return redirect(url_for('adminindex'))
        else:
            message = "admin can not login because of an incorrect username and password."
            # return redirect(url_for('admin',message=message))
            return render_template('admin.html', message=message)

        # strofuser = name
        # print (strofuser.encode('utf8', 'ignore'))
        # return strofuser           
       
    
@app.route('/addteacherregister', methods=['GET', 'POST'])
def addteacherregister():
    if request.method == 'POST':
        
        return render_template("addteacherregister.html") 
    return render_template("addteacherregister.html") 

##################################   ngo login register #########################################################################
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        return render_template("index.html") 
    return render_template("index.html") 

@app.route('/adminindex', methods=['GET', 'POST'])
def adminindex():
    if request.method == 'POST':
        
        return render_template("adminindex.html") 
    return render_template("adminindex.html") 
##################################  blooddoner login /register#########################################################################

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        
        return render_template("contact.html") 
    return render_template("contact.html")          
##################################   blooddoner login/ register#########################################################################        
@app.route('/addteacher', methods=['GET', 'POST'])
def addteacher():
    con = dbConnection()
    cursor = con.cursor()
    print("printing hii before querry execusion")
    cursor.execute('SELECT * FROM teacheregister')
    result = cursor.fetchall()
    print(result)
    return render_template("addteacher.html",result=result)

@app.route('/addstudents', methods=['GET', 'POST'])
def addstudents():
    con = dbConnection()
    cursor = con.cursor()
    print("printing hii before querry execusion")
    cursor.execute('SELECT * FROM userdetails')
    result = cursor.fetchall()
    print(result)
    return render_template("addstudents.html",result=result)




@app.route('/course', methods=['GET', 'POST'])
def course():
    con = dbConnection()
    cursor = con.cursor()
    print("printing hii before querry execusion")
    cursor.execute('SELECT * FROM teacheregister')
    result = cursor.fetchall()
    print(result)
    return render_template("course.html",result=result)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    con = dbConnection()
    cursor = con.cursor()
    print("printing hii before querry execusion")
    cursor.execute('SELECT * FROM userdetails')
    result = cursor.fetchall()
    print(result)
    return render_template("registration.html",result=result)
 

@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        
        return render_template("login.html") 
    return render_template("login.html") 

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        
        return render_template("admin.html") 
    return render_template("admin.html") 
###########################################################################################################        
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        
        return render_template("about.html") 
    return render_template("about.html") 
    
###########################################################################################################        
@app.route('/teacherlogin', methods=['GET', 'POST'])
def teacherlogin():
    if request.method == 'POST':
        username= request.form.get("Username")
        email = request.form.get("Email")
        password= request.form.get("Password")
        mobile= request.form.get("Mobile")
        uploaded_file =request.files['file']
        
        filename_secure = secure_filename(uploaded_file.filename)
        print(filename_secure)
        pathlib.Path(app.config['UPLOAD_FOLDER'], username).mkdir(exist_ok=True)
        print("print saved")
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], username, filename_secure))
        filename1 =os.path.join(app.config['UPLOAD_FOLDER'], username+"/", filename_secure)
     
        print(username,email,password,mobile,filename1)
        con = dbConnection()
        cursor = con.cursor()
        sql = "INSERT INTO teacheregister(Teachername, Temailaddress, Tpassword, Tmobileno, file) VALUES (%s, %s, %s, %s, %s)"
        val = ( username, email,password,mobile,filename1)
        cursor.execute(sql, val)
        con.commit()
        dbClose()
        message = "teacher successfully added by admin side"
        usermail = email
        ogpass = "teacher successfully added by admin side."+"username is-"+username +" "+"password is-"+password
        sendemailtouser(usermail,ogpass)
        return render_template('addteacherregister.html', message=message)
        print("Exception occured at register")

       
    return render_template("addstudenteacher.html")    
    

##################################  ngo verify register user#########################################################################        
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username= request.form.get("name")
#         email = request.form.get("email")
#         password= request.form.get("password")
#         mobile= request.form.get("mobile")
#         uploaded_file =request.files['file']
        
#         filename_secure = secure_filename(uploaded_file.filename)
#         print(filename_secure)
#         pathlib.Path(app.config['UPLOAD_FOLDER1'], username).mkdir(exist_ok=True)
#         print("print saved")
#         uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER1'], username, filename_secure))
#         filename1 =os.path.join(app.config['UPLOAD_FOLDER1'], username+"/", filename_secure)
     
#         print(username,email,password,mobile,filename1)
#         con = dbConnection()
#         cursor = con.cursor()
#         sql = "INSERT INTO useregister(username, email, password, mobile, file) VALUES (%s, %s, %s, %s, %s)"
#         val = ( username, email,password,mobile,filename1)

#         cursor.execute(sql, val)
#         con.commit()
#         dbClose()
#         # flash("user added sucessfully" )
#         # return redirect(url_for('addstudenteacher'))
#         message = "student successfully added by admin side"
#         usermail = email
#         ogpass = "student successfully added by admin side."+"username is-"+username +" "+"password is-"+password
#         sendemailtouser(usermail,ogpass)
      
#         return render_template('addstudenteacher.html', message=message)
    
#     return render_template("addstudenteacher.html")     
    

    
##################################  verify register user#########################################################################        
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("name")
        password = request.form.get("password")
        print(username,password)
        con = dbConnection()
        cursor = con.cursor()
        print("printing hii before querry execusion")
        cursor.execute('SELECT * FROM userdetails WHERE Username = %s AND password = %s', (username, password))
        result = cursor.fetchone()
        print(result)
        if result:
            session['user'] = result[1]
            # session['user'] = username
            print("querry submitted")
            flash('You have successfully logged in..')
            return redirect(url_for('index'))
        else:
            # return redirect(url_for('main'))
            message = "Incorrect username and password."
            return render_template('main.html', message=message)
        
       
    return render_template("main.html") 
    



@app.route('/tlogin', methods=['GET', 'POST'])
def tlogin():
    if request.method == 'POST':
        username = request.form.get("Username1")
        password = request.form.get("Password1")
        print(username,password)
        con = dbConnection()
        cursor = con.cursor()
        print("printing hii before querry execusion")
        cursor.execute('SELECT * FROM teacheregister WHERE Teachername = %s AND Tpassword = %s', (username, password))
        result = cursor.fetchone()
        print(result)
        if result:
            session['user'] = result[1]
            print("querry submitted")
            flash('you are sucessfully login...')
            return redirect(url_for('teacherindex'))
        else:
            message = "Incorrect username and password."
            return render_template('login.html', message=message)
       
    return render_template("login.html") 
    
   
@app.route('/logout')
def logout():
    session.pop('user', None)
    
    return redirect(url_for('main'))
    
   
###########################################################################################################        
import random
@app.route('/createprofile', methods=['GET', 'POST'])
def createprofile():
    if request.method == 'POST':
        id1= request.form.get("id")
        Username = request.form.get("Username")
        EmailId= request.form.get("EmailId")
        MobileNo= request.form.get("MobileNo")
        pass1 = request.form.get("PRNNo")
        
        print(id1,Username,EmailId,MobileNo,pass1)
        
      
        year= request.form.get("year")
        DEPARTMENT= request.form.get("DEPARTMENT")
        class1= request.form.get("class1")
        
        print(year,DEPARTMENT)
        
        
        caddress= request.form.get("caddress")
        paddress= request.form.get("paddress")
        pincode= request.form.get("pincode")
        print(caddress,paddress,pincode)
        
        
        DISTICT= request.form.get("DISTICT")
        STATE= request.form.get("STATE")
        
        print(DISTICT,STATE)
        
        register_yourself(id1,Username,EmailId, MobileNo,year,DEPARTMENT,caddress,paddress,pincode,DISTICT,STATE,class1,pass1)
        print("Registration Successful")
        
      
        
        
        
        # flash("Registration Successful", category='success')
        msg = "The collage administrator successfully created the student's profile for the college."
        usermail = EmailId
        ogpass = "student successfully added by admin side."+"username is-"+Username +" "+"password is-"+pass1
        sendemailtouser(usermail,ogpass)
        return render_template("createprofile.html",msg=msg) 
    return render_template("createprofile.html") 
 
################################## NGO REQUEST TO DONATE BLOOD NEAR BY HOSPITALr#########################################################################        



################################## Donor blood donate in hospital sucessfully#########################################################################        

@app.route('/teacherindex', methods=['GET', 'POST'])
def teacherindex():
    if request.method == 'POST':
        
        return render_template("Teacherindex.html") 
    return render_template("Teacherindex.html") 

    
    


################################## Donor blood donate in hospital sucessfully#########################################################################        
        
@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == "POST":
        teachername=session.get("user")
        # print(username)
        SUBJECT= request.form.get("subject")
        DEPARTMENT= request.form.get("DEPARTMENT")
        year= request.form.get("year")
        date= request.form.get("date")
        print(SUBJECT,year,DEPARTMENT,date)
        
        uploaded_files =request.files.getlist('upload_imgs[]')
        print("------------------------------")
        print(uploaded_files)
        
        print("------------------------------")

        
        # print(SUBJECT,year,DEPARTMENT,date,uploaded_file)
        # filename_secure = secure_filename(uploaded_file.filename)
        # print(filename_secure)
        # pathlib.Path(app.config['UPLOAD_FOLDER2'], username).mkdir(exist_ok=True)
        # # print("print saved")
        # uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER2'], username, filename_secure))
        # filename1 =os.path.join(app.config['UPLOAD_FOLDER2'], username+"/", filename_secure)
        
        for uploaded_file in uploaded_files:
            filename_secure = secure_filename(uploaded_file.filename)
            print(filename_secure)
            upload_folder = os.path.join(app.config['UPLOAD_FOLDER2'], date)
            pathlib.Path(upload_folder).mkdir(exist_ok=True)
            uploaded_file.save(os.path.join(upload_folder, filename_secure))
            
            # print(filename1)
            marked,studentname = mark_your_attendance_singlepic(date,filename_secure)
            print()
            print("---------- attendance result -------------------")
            print(marked,studentname)
            print()
            attend_status = 1
            
            for i in studentname:
                con = dbConnection()
                cursor = con.cursor()
                cursor.execute("select class1,Username from userdetails where ROLL_ID=%s and DEPARTMENT=%s",(i,DEPARTMENT))
                row = cursor.fetchall() 
                print(row)
                count = cursor.rowcount
                print(count)
                
                if count>0: 
                    cursor.execute("select * from marking_attendance where Roll_no=%s and department=%s",(i,DEPARTMENT))
                    countdfsdf = cursor.rowcount
                    if countdfsdf>=0:
                        name=row[0][1]
                        class1=row[0][0]
                        print(name,class1)  
                        sql1 ="INSERT into marking_attendance (Roll_no, department, subject, date, Attendance,classname,username,teachername) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                        val1 = (i, DEPARTMENT, SUBJECT, date, attend_status,class1,name,teachername)
                        cursor.execute(sql1,val1)
                        con.commit()
                
                
        cursor.execute("SELECT * FROM userdetails WHERE NOT EXISTS (SELECT * FROM marking_attendance WHERE userdetails.ROLL_ID = marking_attendance.Roll_no AND marking_attendance.date = %s)",(date))
        count = cursor.rowcount
        print(count)
         
        if count>0: 
            studentdata = cursor.fetchall()
            for i in studentdata:
                absent="0"
                sql1 ="INSERT into marking_attendance (Roll_no, department, subject, date, Attendance,classname,username,teachername) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                val1 = (str(i[1]),str(i[6]),str(SUBJECT),str(date),str(absent),str(i[13]),str(i[2]),str(teachername))
                cursor.execute(sql1,val1)
                con.commit()
                            
        msg="Student mark attendance was done successfully by the teacher side."              
        return render_template("attedance.html",msg=msg) 
    return render_template("attedance.html") 
  
################################## add#########################################################################        
@app.route('/addstudenteacher', methods=['GET', 'POST'])
def addstudenteacher():
    username=session.get("user")
    print(username)
    return render_template("addstudenteacher.html")     
    
@app.route('/attendancereportadmin', methods=['GET', 'POST'])
def attendancereportadmin():
    username=session.get("name")
    con = dbConnection()
    cursor = con.cursor()
    print("printing hii before querry execusion")
    cursor.execute('SELECT Username FROM userdetails')
    result = cursor.fetchall()
    
    cursor = con.cursor()
    cursor.execute('SELECT Teachername FROM teacheregister')
    result2 = cursor.fetchall()
    print(result)
    
    
    
    return render_template("attendancereportadmin.html",result=result,result2=result2) 
    
@app.route('/attendancereport', methods=['GET', 'POST'])
def attendancereport():
    username=session.get("name")
    return render_template("attendancereport.html") 
 
    
@app.route('/attendancereportstudent', methods=['GET', 'POST'])
def attendancereportstudent():
    username=session.get("user")
    print(username)
    
    

    return render_template("attendancereportstudent.html") 
   
################################## add#########################################################################        
  
@app.route('/studentdata', methods=['GET', 'POST'])
def studentdata():
    if request.method == 'POST':
        
        return render_template("student_report.html") 
    return render_template("student_report.html") 
 
    

################################## user show profile#########################################################################        
               
@app.route('/reportadmin', methods=['GET','POST'])
def report():
    if request.method=="POST":
        fname=session.get('user')
        subject = request.form.get("filename")
        classname = request.form.get("classname")
        Teachers = request.form.get("Teachers")
        Students = request.form.get("Students")
        dt = request.form['input']
        print(subject,dt)
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * from marking_attendance where subject =%s and classname =%s and teachername =%s and username =%s and date =%s',(subject,classname,Teachers,Students,dt))
        result = cursor.fetchall()
        print("Printing result")
        print(result)  
        dat = list(result)
        
        ownername  = [] 
        attendance_date = []
        attendance_time = []
        subject = [] 
        attend = [] 
        classname = []
        username = [] 
        teachername = [] 

        for i in dat:
            a=i[1]
            ownername.append(a)
            b=i[2]
            attendance_date .append(b)
            c=i[3]
            attendance_time.append(c)
            d=i[4]
            subject.append(d)
            f=i[6]
            classname.append(f)
            g=i[7]
            username.append(g)
            h=i[8]
            teachername.append(h)
            e=i[5]
            if e=="1":
                op = "Present"
                attend.append(op)
            else:
                op="Absent"
                attend.append(op)
        final_data=zip(ownername ,attendance_date,attendance_time,subject,attend,classname,username,teachername)
        return render_template('attendancereportadmin.html', final_data=final_data )
    return redirect(url_for('login'))    

    
################################## user show profile#########################################################################        
@app.route('/reportteacher', methods=['GET','POST'])
def reportstu():
    if request.method=="POST":
        fname=session.get('user')
        subject = request.form.get("filename")
        Class = request.form.get("Class")
        dt = request.form['input']
        print(subject,dt,Class)
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * from marking_attendance where subject =%s and date =%s and classname =%s',(subject ,dt ,Class))
        result = cursor.fetchall()
        print("Printing result")
        print(result)  
        dat = list(result)
        
        ownername  = [] 
        attendance_date = []
        attendance_time = []
        subject = [] 
        attend = [] 
        classname = []
        username = [] 
        teachername = [] 
        for i in dat:
            a=i[1]
            ownername.append(a)
            b=i[2]
            attendance_date .append(b)
            c=i[3]
            attendance_time.append(c)
            d=i[4]
            subject.append(d)
            f=i[6]
            classname.append(f)
            g=i[7]
            username.append(g)
            h=i[8]
            teachername.append(h)
            
            e=i[5]
            if e=="1":
                op = "Present"
                attend.append(op)
            else:
                op="Absent"
                attend.append(op)
        final_data=zip(ownername ,attendance_date,attendance_time,subject,attend,classname,username,teachername)
        return render_template('attendancereport.html', final_data=final_data )
    return redirect(url_for('login'))   
        

################################## user show profile#########################################################################        
@app.route('/reportstudent', methods=['GET','POST'])
def reportteacher():
    if request.method=="POST":
        fname=session.get('user')
        subject = request.form.get("filename")
        dt = request.form['input']
        print(subject,dt)
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * from marking_attendance where subject =%s and date =%s',(subject ,dt))
        result = cursor.fetchall()
        print("Printing result")
        print(result)  
        dat = list(result)
        
        ownername  = [] 
        attendance_date = []
        attendance_time = []
        subject = [] 
        attend = [] 
        
        classname = []
        username = [] 
        teachername = [] 

        for i in dat:
            a=i[1]
            ownername.append(a)
            b=i[2]
            attendance_date .append(b)
            c=i[3]
            attendance_time.append(c)
            d=i[4]
            subject.append(d)
            
            f=i[6]
            classname.append(f)
            g=i[7]
            username.append(g)
            h=i[8]
            teachername.append(h)
            
            e=i[5]
            if e=="1":
                op = "Present"
                attend.append(op)
            else:
                op="Absent"
                attend.append(op)
        final_data=zip(ownername ,attendance_date,attendance_time,subject,attend,classname,username,teachername)
        return render_template('attendancereportstudent.html', final_data=final_data )
    return redirect(url_for('index'))   
        
    
if __name__ == "__main__":
    app.run("0.0.0.0")
    # app.run(debug=True)
