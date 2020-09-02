import cgi
import os
import smtplib
from email.message import EmailMessage
# Lire fichier automatiquement -> extrait 2 indices email / passwd









#check activity gmail -> authorized | https://www.google.com/settings/security/lesssecureapps -> select turn on




#web Interface
print("Content-type: text/html; charset=utf-8\n")
uform="""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
<script src="https://code.iconify.design/1/1.0.7/iconify.min.js"></script>
<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <style>
        /*form styles*/
#msform {
	width: 400px;
	margin: 50px auto;
	text-align: center;
	position: relative;
}
#msform fieldset {
	background: white;
	border: 0 none;
	border-radius: 3px;
	box-shadow: 0 0 15px 1px rgba(0, 0, 0, 0.4);
	padding: 20px 30px;
	box-sizing: border-box;
	width: 80%;
	margin: 0 10%;

	/*stacking fieldsets above each other*/
	position: relative;
}
/*Hide all except first fieldset*/
#msform fieldset:not(:first-of-type) {
	display: none;
}
/*inputs*/
#msform input, #msform textarea {
	padding: 15px;
	border: 1px solid #ccc;
	border-radius: 3px;
	margin-bottom: 10px;
	width: 100%;
	box-sizing: border-box;
	font-family: montserrat;
	color: #2C3E50;
	font-size: 13px;
}
/*buttons*/
#msform .action-button {

	background: red;
	font-weight: bold;
	color: white;
	border: 0 none;
	border-radius: 1px;
	cursor: pointer;
}
#msform .action-button:hover, #msform .action-button:focus {
	box-shadow: 0 0 0 2px white, 0 0 0 3px #27AE60;
}

    </style>

     <style>body{
	font-family: Arial, Helvetica, sans-serif;
	background: #95C4D3 !important;
	font-size: 10px;
	}

    .medium {
   font-size: 48px;
   line-height: 48px;
}
     </style>





     <center><img src="https://geeknews.fr/wp-content/uploads/2018/07/Gmail.png" width="30%"/>
     <div class="medium"><a href="http://localhost:9000/home.py"><iconify-icon data-icon="ant-design:home-filled"></iconify-icon></a></div>
     <form id="msform" action="/mail.py" method="post">
        <br>

        <input type="text" placeholder="To: exemple@gmail.com" id="to" name="to"><br><br>
        <br>
        <input type="text" id="subject" placeholder="Sujet" name="subject"><br><br>

        <br>
        <textarea id="textarea" name="textaerea" placeholder="Message" rows="20" cols="100"></textarea><br><br>
        <br>
        <input type="text" id="file" placeholder="File" name="attach"><br><br>

        <input type="submit" id="send" class="next action-button" value="Envoyer"/>
             <div class="alert alert-success" style="display:none;"  id="message">
                 <strong>Success!</strong> Email envoyé.
               </div>
     </form></center>

     <script>
         const key = document.getElementById("to");
         const send = document.getElementById("send");

         send.onclick= function(){
             const pls = key.value;

             console.log(pls);

             if(pls){
                 localStorage.setItem("to",pls);
                 location.reload();
             }

         };

         for (let i=0; i < localStorage.length; ++i) {
             const pls = localStorage.key(i);
             const value= localStorage.getItem(pls);
             var pdf=`${value}`;

         }


     </script>
      <script>
        $( "#send ").click(function(){
            $('#message').fadeIn('slow', function(){
               $('#message').delay(5000).fadeOut();
            });
        });
        </script>
</body>
</html>
"""
print(uform)




#f = js2py.eval_js( "function $(name) {return localStorage.getItem(name)}" )
#print(f("templateXML"))

#print(form.readAsText(this.files[0]))
form = cgi.FieldStorage()

data_email=[]

with open("authmail.txt", 'r') as f:
   for line in f:
       data_email.append(line)#[email, passwd]

print(data_email)
EMAIL_ADDRESS=str(data_email[0])#[0]
EMAIL_PASSWORD=str(data_email[1])#[1]






#SendMail
#with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#    smtp.ehlo()
#    smtp.starttls()
#    smtp.ehlo()

#    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
#    subject=form.getvalue("subject")
#    body=form.getvalue("textaerea")
#    msg=f'Subject: {subject}\n\n{body}'
#    smtp.sendmail(EMAIL_ADDRESS,form.getvalue("to"),msg)
# import the corresponding modules
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




subject=form.getvalue("subject")
sender_email = str(data_email[0])
receiver_email = form.getvalue("to")

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
body=form.getvalue("textaerea")
message.attach(MIMEText(body, "plain"))

filename = form.getvalue("attach")
# Open PDF file in binary mode

# We assume that the file is in the directory where you run your Python script from
if filename != "no":
    with open(filename, "rb") as attachment:
        # The content type "application/octet-stream" means that a MIME attachment is a binary file
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode to base64
    encoders.encode_base64(part)

    # Add header
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to your message and convert it to string
    message.attach(part)
    text = message.as_string()
else:
    text = message.as_string()

# send your email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.sendmail(
        sender_email, receiver_email, text
    )
