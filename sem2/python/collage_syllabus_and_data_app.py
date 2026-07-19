import pyttsx3
from tabulate import*
import datetime
import colorama
import subprocess

#date time 

xy = datetime.datetime.now()
x1 = xy.strftime("%Y")
x2 = xy.strftime("%m")
x3 = xy.strftime("%b")
x4 = xy.strftime("%d")
x5 = xy.strftime("%I")
x6 = xy.strftime("%M")
x7 = xy.strftime("%S")
x8 = xy.strftime("%p")
time = [x4,"/",x2,"(",x3,")","/",x1,"   ",x5,"-",x6,"-",x7,"-",x8]
print(colorama.Fore.LIGHTRED_EX + str(time))
print(colorama.Fore.MAGENTA)

#voice syntax

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id,)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

#voice function

def speak(text):
    engine.say(text)
    engine.runAndWait()

print(colorama.Fore.RESET)
speak("Hello")

#name input page
a = input("enter your name :-")

#gender
b = input(""" male as m and female as f
male or female ?  """)
m = ("m")
f = ("f")
if b == m:
    x = ("Sir")
elif b == f:
    x = ("mam")
else:
    speak,print('valid gender input')

#speak name and gender

speak(a)
speak(x)

#welcome page

print("""                       -----------------  welcome  -----------------      """)
print("""           *-*_*-*-------- Sir bhavshiji politecnik institute *-*_*-*-------       """)
speak("welcome to Sir bhavshiji politecnik institute")

#table


branch_short_name  = ["IT","MACH","ELC","EC","CIVIL","COMPUTER","AUTO","FEB","CAM"]
branch_code_for_gtu = [16,10,10,10,10,10,10,10,10]

table = {
            "branch(Name)": branch_short_name,
            "branch code for gtu": branch_code_for_gtu,
        }

print(colorama.Fore.GREEN+(tabulate(table, headers="keys" , tablefmt="psql",showindex="always")))
print(colorama.Fore.RESET)
speak("which branch in you study")

#branch name enter 

aa = "no data"
aa =input("enter branch_code (as per as bellow this table):-")

#branch condision

if aa == "IT":
    speak('good choise ')
    print(a,"""good choise """)


#user input it condition

    if aa == "IT":

        speak('what do yo want ?')
        abcd1 = input("what do yo want ? (sub = subject details , stu = student details) :-")
        

#it is condition for syllBUS OR STUdent

        if abcd1 == "sub":
        
            speak,print('welcome to it syllabus page')

            semeter_it = [1,2,3,4,5,6]
            num_of_subject = [6,7,0,0,0,0]
            num_of_credit_subject = [5,6,0,0,0,0]

            table1 = {
                "semeter_it": semeter_it,
                "number of subject": num_of_subject
            }
            print(colorama.Fore.BLUE+(tabulate(table1, headers="keys", tablefmt="pqsl",showindex="always")))
            print(colorama.Fore.RESET)
            speak('whose semster in if you want subject details ?')
            acb = "no data"
            acb = input("whose semster in if you want subject details ?")

#it semeter wise syllabus details

            if acb == '1':
                speak('this details of IT semester:-1 subject and syllbus')
                sub_name_1 = ["basic mathematics","comunication skills and english","information to IT system","python programmimg","stetic web page desing","sport yoga","indaction program"]
                credits_1 = [4,3,5,5,2,0,0]
                subject_codes = [4300001,4300002,4311601,4311602,4311603,4300015]

                table2 = {
                    "subject name":sub_name_1,
                    "subject code":subject_codes,
                    "credits":credits_1
                    }
                    
                print(tabulate(table2,headers="keys",tablefmt="pqsl",showindex="always"))
                
                aabb = input("enter subject code (for a syllabus pdf) :-")
                
                if aabb == "4300001":  
                    speak,print('basic mathematics syllabus pdf') 
                    path = "D:\\syllabus\\4300001.pdf"
                    subprocess.Popen([path], shell=True)
                
                elif aabb == "4300002":
                    speak,print('comunication english syllabus pdf') 
                    path = "D:\\syllabus\\4300002.pdf"
                    subprocess.Popen([path], shell=True)

                elif aabb == "4311601":
                    speak,print('information to it system syllabus pdf') 
                    path = "D:\\syllabus\\4311601.pdf"
                    subprocess.Popen([path], shell=True)

                elif aabb == "4311602":
                    speak,print('python programing syllabus pdf') 
                    path = "D:\\syllabus\\4311602.pdf"
                    subprocess.Popen([path], shell=True)

                elif aabb == "4311603":
                    speak,print('static web page desing syllabus pdf') 
                    path = "D:\\syllabus\\4311603.pdf"
                    subprocess.Popen([path], shell=True)

                elif aabb == "4300015":
                    path = "D:\\syllabus\\4300015.pdf"
                    subprocess.Popen([path], shell=True)
                    speak,print('sports and yoga syllabus pdf') 

                else :
                    print("sorry try later")
                
            elif acb == '2':
                speak('this details of IT semester:-2 subject and syllbus')
            
            elif acb == '3':
                speak('this details of IT semester:-3 subject and syllbus')

            elif acb == '4':
                speak('this details of IT semester:-4 subject and syllbus')

            elif acb == '5':
                speak('this details of IT semester:-5 subject and syllbus')

            elif acb == '6':
                speak('this details of IT semester:-6 subject and syllbus')

            else:
                speak,print('sorry wrong in input only 6th semester in it please try later')

# stu detail

        elif abcd1 == "stu":

            speak,print('this is student name list')

            speak,print('this is only admin enter name and show more details of student')

            admin = ["dhj","vsg","ngs","jnv","hpj","gmp"]

            adcb = "no data"
            adcb = input("enter admin name :-")

            if adcb in admin:
                password = ("jay hind")

                speak,print('plese enter password')
                acbd = "no data"
                acbd = input("enter password")

                if acbd == password:
                    speak,print('this is student more details')
                else:
                    speak,print('wrong password please try later')   
            
            else:
                speak,print('your not admin')

#it is a branch (IT) name else code         
    else:
        print,speak('wrong input')

# wrong branch enter branch else condition 

else:
    print,speak('sorry try later')

#file in store input values

#details=["\ntime :- ",str(time),"\nName:- ",a,"\nGender:- ",b, "\nbranch:- ",aa,"\nsubject or student:- ",abcd1,"\nsub_sem:- ",acb,"\nsubject_code:-",aabb,"\nsemester:- "]
#f=open("D:\\New_3.txt","a+")
#f.writelines(details)
#f.close()

