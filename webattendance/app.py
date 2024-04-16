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
from datetime import datetime
# import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem import PorterStemmer
import datetime

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] ='static/teacher'

app.config['UPLOAD_FOLDER1'] ='static/users'

app.config['UPLOAD_FOLDER2'] ='static/uploadimage'

app.config['UPLOAD_FOLDER3'] ='static/Notice'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.secret_key = 'any random string'




##################################   Mail to  #########################################################################

def sendemailtouser(usermail,ogpass):   
    fromaddr = "nikitapawar202001@Gmail.Com"
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
    s.login(fromaddr, "lftzhrijsrrymcbn") 
  
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
  
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
  
    # terminating the session 
    s.quit()
    



##################################   Mail to blooddoner #########################################################################
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
import string
punc=string.punctuation
def remove_stopwords(data):
    output_array=[]
    for sentence in data:
        temp_list=[]
        for word in sentence.split():
            if word.lower() not in stop_words:
                temp_list.append(word)
        output_array.append(' '.join(temp_list))
    return output_array
def remove_punc(data):
    output_array=[]
    for sentence in data:
        temp_list=[]
        for word in nltk.word_tokenize(sentence):
            if word not in punc:
                temp_list.append(word)
        output_array.append(' '.join(temp_list))
    return output_array
from nltk.corpus import wordnet
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)
def lemmatization(data):
    output_array=[]
    for sentence in data:
        temp_list=[]
        for word in sentence.split():
            word=word.lower()
            from nltk.stem import WordNetLemmatizer
            lemma=WordNetLemmatizer()
            new_word=lemma.lemmatize(word, get_wordnet_pos(word))
            #print(new_word)
            temp_list.append(new_word)
        output_array.append(' '.join(temp_list))
    return output_array

##################################   database connection #########################################################################
def dbConnection():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="root", database="042-attendence", autocommit=True)
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
 

@app.route('/Tlogin', methods=['GET', 'POST'])
def Tlogin():
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
            session['id'] = result[0]
            session['name'] = result[2]
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
                cursor.execute('SELECT * FROM marking_attendance WHERE Roll_no = %s AND department = %s AND date = %s', (i,DEPARTMENT,date))
                count = cursor.rowcount
                if count == 0:   
                    
                    cursor.execute("select class1,Username from userdetails where ROLL_ID=%s and DEPARTMENT=%s",(i,DEPARTMENT))
                    usercount = cursor.rowcount
                    if usercount > 0:
                        userdata = cursor.fetchone() 
                    
                        print("Insert call")
                        sql1 = "INSERT into marking_attendance (Roll_no, department, subject, date, Attendance,classname,username,teachername) values (%s,%s,%s,%s,%s,%s,%s,%s);"
                        val1 = (i, DEPARTMENT, SUBJECT, date, attend_status,userdata[0],userdata[1],teachername)
                        cursor.execute(sql1,val1)
                        con.commit()
                        
        cursor.execute("SELECT * FROM userdetails WHERE NOT EXISTS (SELECT * FROM marking_attendance WHERE userdetails.ROLL_ID = marking_attendance.Roll_no AND marking_attendance.date = %s)",(date))
        count = cursor.rowcount
        print(count)
         
        if count>0: 
            studentdata = cursor.fetchall()
            for i in studentdata:
                absent="0"
                print("Out call")
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
        
######################################################################################################

@app.route('/Notice', methods=['GET', 'POST'])
def Notice():
    if request.method == 'POST':
        recipient = request.form.get("recipient")
        noticeTitle= request.form.get("noticeTitle")
        noticeContent= request.form.get("noticeContent")
      
        uploaded_file =request.files['file']
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print("Formatted Date and Time:", formatted_datetime)
        
        filename_secure = secure_filename(uploaded_file.filename)
        print(filename_secure)
        pathlib.Path(app.config['UPLOAD_FOLDER3'], recipient).mkdir(exist_ok=True)
        print("print saved")
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER3'], recipient, filename_secure))
        filename1 =os.path.join(app.config['UPLOAD_FOLDER3'], recipient+"/", filename_secure)
        
        sql1 = "INSERT into notics (recipient, noticeTitle, noticeContent, uploaded_file,date) values (%s,%s,%s,%s,%s);"
        val1 = (recipient, noticeTitle, noticeContent, filename1,formatted_datetime)
        cursor.execute(sql1,val1)
        con.commit()
        msg="Notice added successfully by the admin side."  
        
        return render_template("Notice.html",msg=msg) 
    return render_template("Notice.html") 

@app.route('/Tnotice', methods=['GET', 'POST'])
def Tnotice():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM notics WHERE recipient = 'teacher';")
    result = cursor.fetchall()
    print(result)
    return render_template("Tnotice.html",result=result) 

@app.route('/Snotice', methods=['GET', 'POST'])
def Snotice():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM notics WHERE recipient = 'student'; ")
    result = cursor.fetchall()
    print(result)
    return render_template("Snotice.html",result=result) 
    
######################################################################################################
                                        #exam
######################################################################################################
@app.route('/Exam', methods=['GET', 'POST'])
def Exam():
    if request.method == "POST":
        con = dbConnection()
        cursor = con.cursor()
        for i in range(1, 6):
            question = request.form.get("question" + str(i))
            answer = request.form.get("description" + str(i))
            sql = "INSERT INTO test (Question,Answer) VALUES (%s, %s)"
            val = (question, answer)
            cursor.execute(sql, val)
            con.commit()
        msg = "TEST added successfully by the admin side."
        return render_template("Exam.html", msg=msg)
    
    return render_template("Exam.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    cursor.execute("SELECT * FROM marks")
    result = cursor.fetchall()
    # print(result)
    return render_template("result.html",result=result) 

@app.route('/Test', methods=['GET', 'POST'])
def Test():
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * from test")
    res = cursor.fetchall()
    print(res)
    if request.method == "POST":
        for i in range(1,6):
            answer=request.form.get("description"+str(i))
            print("printing answer in if", answer)
            print()
            print("printing answer in if", type(answer))
            if answer is None or answer=="":
                answer = "We submitted the exam because user switches the tab"
                sql = "INSERT INTO answers (sid ,answers) VALUES (%s,%s)"
                val = ((session['id']),answer)
                cursor.execute(sql, val)
                con.commit()
            else:
                print("printing answer in else", answer)
                print()
                sql = "INSERT INTO answers (sid ,answers) VALUES (%s,%s)"
                val = ((session['id']),answer)
                cursor.execute(sql, val)
                con.commit()
        cursor.execute("select answers from answers where sid="+str(session['id']))
        stud=cursor.fetchall()
        print()
        print("printing stud: ", stud)
        print()
        cursor.execute('SELECT Answer from test')
        teach=cursor.fetchall()
        stud1=[]
        for l in stud:
            stud1.append(l[0])
        teach1=[]
        for k in teach:
            teach1.append(k[0])
            
        print(teach1)
        print("prining stud1 :",stud1)
        print()
        output1=remove_stopwords(teach1)
        output2=remove_stopwords(stud1)
        output3=remove_punc(output1)
        output4=remove_punc(output2) 
        output5=lemmatization(output3)
        output6=lemmatization(output4)
        marks=[]
        finalmarks=[]
        print(output3)
        print(output4)
        print(output5)
        print(output6)
        for i in range(len(teach)):
            m=output5[i]
            n=output6[i]
            print(m)
            print(n)
            from fuzzywuzzy import fuzz
            c=fuzz.ratio(output5[i],output6[i])
            #d=fuzz.token_set_ratio(output6[i],output5[i])
            print(c)
            #print(d)
            a=c/10
            print(a)
            finalmarks.append(a)
        finalmarks
        a=finalmarks[0]
        b=finalmarks[1]
        c=finalmarks[2]
        d=finalmarks[3]
        e=finalmarks[4]
        for i in finalmarks:
            a=i
        total = 0
        for ele in range(0, len(finalmarks)):
            print(ele)
            total = total + finalmarks[ele]
        import math
        print(total)
        ma=math.ceil(total)
        print(ma)
        current_datetime = datetime.datetime.now()

            
        con = dbConnection()
        cursor = con.cursor()
        
        
        # Check if a record with the same datetime already exists
        check_sql = "SELECT COUNT(*) FROM marks WHERE DateTime = %s"
        cursor.execute(check_sql, (current_datetime,))
        count = cursor.fetchone()[0]
        if count == 0:
            sql="INSERT INTO marks (sid,studname,q1,q2,q3,q4,q5,marks,DateTime) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
            val=(session['user'],session['name'],a,b,c,d,e,ma,current_datetime)
            cursor.execute(sql, val)
            con.commit()
            
            msg = "test successfully added by Teacher side."+"username is-"+session['name'] 
            
            
            return render_template('Test.html',msg=msg)
        
          
        else:
            print("Record with the same datetime already exists.")
            msg = "Record with the same datetime already exists."
            return render_template('Test.html',msg=msg)
        
        return render_template('Test.html')
 
    return render_template("Test.html",res=res) 

    
if __name__ == "__main__":
    app.run("0.0.0.0")
    # app.run(debug=True)
