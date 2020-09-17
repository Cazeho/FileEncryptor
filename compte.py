import cgi
import os
import subprocess
import re
print("Content-type: text/html; charset=utf-8\n")
uform="""
<style>
#myDIV {
  width: 100%;
  padding: 50px 0;
  text-align: center;
  background-color: lightblue;
  margin-top: 20px;
}
</style>
<br>
<br>
<center><button onclick="myFunction()">Formulaire</button></center>
<div id="myDIV" style="display: none">
<center><form action="/compte.py" method="post">
    <br>
    <br>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="pseudo" placeholder="login"><br>
  <input type="submit" value="Enregistrer">
</form></center>
</div>

<center><p>
<script>
function myFunction() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

</script>



"""
print(uform)
with open('memory.txt', 'r+') as f:
    print(f.read())
#k=[]
#
form = cgi.FieldStorage()
lo=str(form.getvalue("pseudo"))
#print(k)
#print(k[0])
#print(len(k))

#############
print("""<br>"""+subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip())
uform2="""
</p></center>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js" ></script>
<center><button id="go">reload</button></center>
<script>
$('#go').click(function() {
    location.reload();
});
</script>
"""
print(uform2)




f = open("memory.txt", "a")
if lo!="None":
    k=[]
    with open("memory.txt" , 'r') as f:
        for line in f:
            k.append(line)
            #print(line+"""<br>""")
        #print(k)
    with open('memory.txt', 'r+') as f:
        file_source = f.read()
        file_source=re.sub(k[0], str(lo), file_source)
        f.seek(0)
        f.write(file_source)
        f.truncate()


#read file after changing
    #with open('memory.txt', 'r+') as f:
    #    print(f.read())
    #if len(k)==1:
    #     print("aaaaaaaaaaaaaaaaa")
    #else:

        #f.write(lo+ os.linesep)
    #    f.close()
    #-> 2 valeur interverti -> 1
