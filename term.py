import cgi
import re

print("Content-type: text/html; charset=utf-8\n")


a="aaaaaaaaaa"
uform="""

<!DOCTYPE html>
<html>
<head>
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="https://unpkg.com/jquery.terminal/js/jquery.terminal.min.js"></script>
<link rel="stylesheet" href="https://unpkg.com/jquery.terminal/css/jquery.terminal.min.css"/>
</head>

<body>
</body>
</html>
<script>
$('body').terminal({

    logs: function() {

        """
print(uform)
with open("console.log" , 'r') as f:
    for line in f:
        print("""this.echo( """+ """'"""+line+""");""" )

uform2= """
    },

    help: function(){
        this.echo('0- la commande - la description de la commande');
        this.echo('1- logs - Affiche l ensemble des logs de UI');
        this.echo('2- log argv("Est une date") - Affiche les logs a partir de la date renseigne');
        this.echo('3- quit - Quitte le terminal et revient sur le Dashboard');
        this.echo('4- clear - Reset le terminal');
    },

    log: function(self){

        """
print(uform2)
print("""this.echo(self);""")
with open("console.log" , 'r') as f:
   for line in f:
       match= re.search(r'(\d+-\d+-\d+)',line)
       #print(date)
       #print(match.group(0))
       if match.group(0) == """self""":
           print("""this.echo( """+ """'"""+line+""");""")

uform3= """ console.log(self);
    },

    quit: function(){

        window.open('http://localhost:9000/home.py');
        window.close();


    }

}, {
    greetings: 'Console de Log:'
});
</script>
"""
print(uform3)
