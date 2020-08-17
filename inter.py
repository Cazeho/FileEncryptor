import cgi
import win32com.client
from os import path
import os
from pathlib import Path
from zipfile import ZipFile
import shutil
from yattag import Doc
print("Content-type: text/html; charset=utf-8\n")

#//img.alicdn.com/tps/TB1d.u8MXXXXXXuXFXXXXXXXXXX-1900-790.jpg


path = '/Users/Romain/AppData/Local/Programs/Python/Python37/FileEncryptor/upload'

files=os.listdir(path)

#https://cdn5.vectorstock.com/i/1000x1000/00/64/abstract-technology-background-web-developer-vector-20170064.jpg

#https://wallpaperaccess.com/full/672238.jpg

uform="""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">


     <style>html{
	font-family: Arial, Helvetica, sans-serif;
    background-image: url("https://wallpaperaccess.com/full/672238.jpg");
    background-size: 100%;


    background-repeat:no-repeat;
    background-attachment: fixed;
    font-size: 10px;


	}



    .aside {
  background-color: #DDDDDD;
  border-radius: 25px;
  width: 400px;
  padding: 0px;
  color: #000000;
  text-align: center;
  font-size: 14px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);


}
/* rectange opage */
.bg-header {
  background-color: ##f1f1f1; /* Fallback color */
  /*background-color: rgba(0,0,0, 0.4); /* Black w/opacity/see-through */
  box-shadow: inset 0 0 0 200px rgba(255,255,255,0.2);
  color: white;
  font-weight: bold;
  /*border: 3px solid #f1f1f1;*/
  position: absolute;
  top: 0%;
  left: 50%;
  height:   400px;
  transform: translate(-50%, -50%);
  z-index: 2;
  width: 100%;
  /*padding: 20px;*/
   filter: blur(10ppx);
  -webkit-filter: blur(10ppx);

}

     </style>
<div class="bg-header"></div>

<!-- FileEncryptor logo -->
     <style>
@import url(https://fonts.googleapis.com/css?family=Mr+Dafoe);
@import url(https://fonts.googleapis.com/css?family=Titillium+Web:900);
@import url(https://fonts.googleapis.com/css?family=Righteous);
@import url(https://fonts.googleapis.com/css?family=Candal);

@import url(https://fonts.googleapis.com/css?family=Permanent+Marker);

@import url(https://fonts.googleapis.com/css?family=Monoton);
.vectro {
  position: relative;
  -webkit-text-fill-color: transparent;
  -webkit-text-stroke: 0.1px #f1f1f1;
  font-family: 'Righteous', cursive;
  font-size: 160px;
  margin: 150px 0 50px 0;
}

.vectro:after {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  /*-webkit-animation:vectro_effect 0.067s infinite;*/

}



.windows .vectro {
  -webkit-text-stroke: 4px #f1f1f1;
}

.vectro-body {
  -webkit-background-clip: text;
  background-image: -webkit-linear-gradient(#C3BFB4 0%, #FDFCFA 50%, #E8E7E5 51%, #757172 52%, #E8E9DB 100%);
  -webkit-filter: drop-shadow(2px 2px 15px #3F59F4);
}

.vectro-red {
  color: #F10C20;
  -webkit-text-fill-color: #F10C20;
  -webkit-text-stroke: 0;
  -webkit-filter: drop-shadow(2px 2px 15px #F10C20);
  font-style: italic;
  padding-right: 20px;
}

.windows .vectro-red {
  padding-right: 30px;
}

.vectro-green {
  color: #6BFF2B;
  -webkit-text-fill-color: #6BFF2B;
  -webkit-filter: drop-shadow(2px 2px 15px #6BFF2B);
  -webkit-text-stroke: 0;
  font-style: italic;
  padding-right: 20px;
  margin-left: -20px;
}

.windows .vectro-green {
  padding-right: 30px;
  margin-left: -30px;
}

.vectro-blue {
  color: #3F59F4;
  -webkit-text-fill-color: #3F59F4;
  -webkit-filter: drop-shadow(2px 2px 15px #3F59F4);
  -webkit-text-stroke: 0;
  font-style: italic;
  padding-right: 20px;
  margin-left: -20px;
}

.windows .vectro-blue {
  padding-right: 30px;
  margin-left: -30px;
}
</style>

<!-- logo qui bouge -->
<style>
@keyframes square-animation {
	 0% {
		 left: 0;
		 top: 0;
	}
	 10.5% {
		 left: 0;
		 top: 0;
	}
	 12.5% {
		 left: 32px;
		 top: 0;
	}
	 23% {
		 left: 32px;
		 top: 0;
	}
	 25% {
		 left: 64px;
		 top: 0;
	}
	 35.5% {
		 left: 64px;
		 top: 0;
	}
	 37.5% {
		 left: 64px;
		 top: 32px;
	}
	 48% {
		 left: 64px;
		 top: 32px;
	}
	 50% {
		 left: 32px;
		 top: 32px;
	}
	 60.5% {
		 left: 32px;
		 top: 32px;
	}
	 62.5% {
		 left: 32px;
		 top: 64px;
	}
	 73% {
		 left: 32px;
		 top: 64px;
	}
	 75% {
		 left: 0;
		 top: 64px;
	}
	 85.5% {
		 left: 0;
		 top: 64px;
	}
	 87.5% {
		 left: 0;
		 top: 32px;
	}
	 98% {
		 left: 0;
		 top: 32px;
	}
	 100% {
		 left: 0;
		 top: 0;
	}
}
 @keyframes hue-rotate {
	 0% {
		 filter: hue-rotate(0deg);
	}
	 100% {
		 filter: hue-rotate(360deg);
	}
}

 .loading {
	 position: relative;
	 width: 35px;
	 height: 0px;
	 transform: rotate(45deg);
	 animation: hue-rotate 10s linear infinite both;
}
 .loading__square {
	 position: absolute;
	 top: 0;
	 left: 0;
	 width: 28px;
	 height: 28px;
	 margin: 2px;
	 border-radius: 2px;
	 background: #07a;
	 background-image: linear-gradient(45deg, #fa0 40%, #0c9 60%);
	 background-image: -moz-linear-gradient(#fa0, #fa0);
	 background-size: cover;
	 background-position: center;
	 background-attachment: fixed;
	 animation: square-animation 10s ease-in-out infinite both;
}
 .loading__square:nth-of-type(0) {
	 animation-delay: 0s;
}
 .loading__square:nth-of-type(1) {
	 animation-delay: -1.4285714286s;
}
 .loading__square:nth-of-type(2) {
	 animation-delay: -2.8571428571s;
}
 .loading__square:nth-of-type(3) {
	 animation-delay: -4.2857142857s;
}
 .loading__square:nth-of-type(4) {
	 animation-delay: -5.7142857143s;
}
 .loading__square:nth-of-type(5) {
	 animation-delay: -7.1428571429s;
}
 .loading__square:nth-of-type(6) {
	 animation-delay: -8.5714285714s;
}
 .loading__square:nth-of-type(7) {
	 animation-delay: -10s;
}



</style>


      <center><br><br><br><br><br><br><br><br>
      <div class="loading">

          <div class="loading__square"></div>
          <div class="loading__square"></div>
          <div class="loading__square"></div>
          <div class="loading__square"></div>
          <div class="loading__square"></div>
          <div class="loading__square"></div>
          <div class="loading__square"></div>
      </div>



        <!-- gestion de fichier -> Upload -->
      <p class="vectro"><span class="vectro-body">FileEncryptor</span><span class="vectro-red">I</span><span class="vectro-green">I</span><span class="vectro-blue">I</span></p><br><br><div class="col-3 col-s-12">
    <div class="aside">
      <br>
      <a href="index.py">to next</a>
      <form action="/inter.py" method="post">

      <input type="file" id="myFile" name="filename" multiple>
      <button id="ok" class="parametre" onclick="myFunction()">GO</button>
      <label for="n"><h3>Select Path of current file</h3></label><br>
      <input type="text" id="p" name="p"><br><br>
      <input type="submit" id="save" value="save">
      </form>
    </div></center>

     <style>


     .btn {
       background-color: red;
       border: none;
       color: white;
       padding: 12px 30px;
       cursor: pointer;
       font-size: 20px;
     }

     /* Darker background on mouse-over */
     .btn:hover {
       background-color: grey;
     }
     </style>

     <!-- E/D + download + misc fonct -->

     <center><br><br><br><div class="aside"><form action="/inter.py" method="post">
        <br>
        <label for="n"><h3>1</h3></label><br>
        <input type="text" id="to" name="to"><br><br>
        <label for="n"><h3>2</h3></label><br>
        <input type="text" id="subject" name="subject"><br><br>

        <input type="submit" id="encrypt" value="encrypt">
        <input type="submit" id="decrypt" value="decrypt">
     </form>
     <button class="btn"><i class="fa fa-download"></i><i class="cf cf-orbs"></i><a href="/pack/dir.zip" download>Download</a></button></center></div>
     <script>
         const key = document.getElementById("p");
         const send = document.getElementById("save");
         const fi= document.getElementById("myFile");


         send.onclick= function(){
             const pls = key.value;
             const pls2= fi.files[0].name;

             console.log(pls);
             console.log(pls2);

             //if(pls && pls2){
                if(pls!=""){
                 localStorage.setItem("path",pls);
                 }
                 localStorage.setItem("file",pls2);
                 //alert(pls2)
                 location.reload();
             //}

         };
         var ft=[];
         for (let i=0; i < localStorage.length; ++i) {
             const pls = localStorage.key(i);
             const pls2 = localStorage.key(i+1);
             //alert(pls)
             //alert(i);
             const value= localStorage.getItem(pls);
             var pdf=`${value}`;
             //var pdf2=`${value2}`;
             ft.push(value);
             //alert(value);


         }
         console.log(ft);


     </script>
     <script>
     function myFunction() {
  var x = document.getElementById("myFile").value;
  //document.getElementById("demo").innerHTML = x;
}
     </script>

     <p id="demo"></p>


"""
print(uform)




#f = js2py.eval_js( "function $(name) {return localStorage.getItem(name)}" )
#print(f("templateXML"))

#print(form.readAsText(this.files[0]))


#dash file
form = cgi.FieldStorage()
print(form.getvalue("filename"))
print("====================")

#Affichage tableau des dossiers: Upload
print("""<center><div class="aside"><h3><p>File: Upload</p></h3><table>""")
for fi in files:
    print("""<tr><td>"""+fi+"""</td></tr>""")
print("""</table></div></center><style>
table {
  width:100%;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 15px;
  text-align: left;
}
#t01 tr:nth-child(even) {
  background-color: #eee;
}
#t01 tr:nth-child(odd) {
 background-color: #fff;
}
#t01 th {
  background-color: black;
  color: white;
}
</style>""")




a="aaaa"
print("""<p id="demo2">

<script>

  document.getElementById("demo2").innerHTML = " """+str(a)+""" ";

</script>""")
print(form.getvalue("to"))





data_folder = Path("/Users/Romain/AppData/Local/Programs/Python/Python37/FileEncryptor")

file_to_open = data_folder / "privkey.pem"
###############go download
with ZipFile('dir.zip', 'w') as zipObj2:
   # Add multiple files to the zip
   zipObj2.write('privkey.pem')

original = r'/Users/Romain/AppData/Local/Programs/Python/Python37/FileEncryptor/dir.zip'
target = r'/Users/Romain/AppData/Local/Programs/Python/Python37/FileEncryptor/pack/'

shutil.move(original,target)

f = open(file_to_open)

print(f.read())




data_para=[]
data_type=[]
data_name=[]


js="""
    function load_slide(clicked_id) {
        // console.log(clicked_id);
        document.getElementById('slides').scrollTo(0,(document.getElementsByClassName('slide').namedItem(clicked_id).offsetTop)-50);
    }


    """
#ajax/jquery
jq="""
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js" ></script>
    <script>
    //alert(pdf);



    $(".parametre").click(function() { //class: shape
        $(this).text('OK');  //ecrire dans un élément jquery
        $.ajax({
            url : '/asso.py', //adresse du fichier
            type : 'GET', // Le type de la requête HTTP.
            data : {
                xml_value: ft[0],
                mk_value: ft[1]
            },
            dataType: "html",
            success: function (){
                console.log('ajax: ok, fichier: new_xml');
            },
            error: function(){
                console.log('ajax: pas ok.');
            },
        });
    });
    </script>
    """


print(jq)





##############################
