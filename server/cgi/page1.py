#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()
bday = form.getvalue('birthdate')
hobby = form.getvalue('main hobby')

print """Content-Type: text/html

<!DOCTYPE html>
<html>
<form method="get" action="page2.py"> 
<div> Name: <input type="text" name="name" /> </div>
<div> Family: <input type="text" name="family" /> </div>
<div> <input type="submit" value="Send"> </div>
</form>
Result:<br/>
Birthdate: %s <br/>
Main Hobby: %s <br/>
</html>""" % (bday, hobby)
