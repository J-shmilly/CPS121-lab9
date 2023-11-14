from findTemperatureLive import findTemperatureLive
from sentence import sentence

def createHomePage(emailuser):
    firstname, lastname = emailuser.split(".")
    filename = firstname[0].upper() + firstname[1:]
    filename = emailuser + '.html'
    file = open(filename, 'w')
    temperature = findTemperatureLive()
    sent = sentence()
    htmlCode = f'''<!DOCTYPE html>
<html>
<head>
<title>{firstname[0].upper() + firstname[1:]}'s Home Page</title>
</head>
<body>
<h1>Welcome to {firstname[0].upper() + firstname[1:]}'s Home Page</h1>
<p>
Hi! I am {firstname[0].upper() + firstname[1:]}. This is my home page!
Here is my picture.
</p>
<img src="{emailuser}.jpg" alt="Picture of {firstname}" />
<p> Today's Weather is {temperature} degrees F!</p>
<p> The random sentence of today is: {sent} </p>
</body>
</html>'''
    file.write(htmlCode)
    file.close()



if __name__ == "__main__":
    createHomePage("josh.miller")