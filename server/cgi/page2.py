#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
fam = form.getvalue('family')

print """Content-Type: text/html

<!DOCTYPE html>
<html>
<form method="get" action="page1.py"> 
<div> Birthdate: <input type="date" name="birthdate" /> </div>
<div> Main Hobby: <input type="text" name="main hobby" /> </div>
<div> <input type="submit" value="Send"> </div>
</form>
Result:<br/>
Name: %s <br/>
Family: %s <br/>
</html>""" % (name, fam)
