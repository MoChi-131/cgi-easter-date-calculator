#!/usr/bin/env python3

import cgitb, cgi
import datetime


cgitb.enable()
form = cgi.FieldStorage() 
year = int(form.getvalue('theNumber'))
format = form.getvalue("format")

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title> Python script to output the square of a number </title>  </head>')
print('<link rel="stylesheet" type="text/css" href="../stylesheet.css">')
print('<body>')

def Easter(y):
    a = y % 19   
    b = y // 100   
    c = y % 100   
    d = b // 4   
    e = b % 4   
    g = (8 * b + 13) // 25   
    h = (19 * a + b - d - g + 15) % 30   
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    #return (f"{p}/{n}/{y}")
    return [p, n, y]

def numerical(date):
    return (f"{date[0]}/{date[1]}/{date[2]}")

def verbose(date):
    y = datetime.datetime(date[2], date[1], date[0])
    month = y.strftime("%B")
    if date[0]%10 ==1 and date[0]!=11:
        word = "st"
    elif date[0]%10 ==2 and date[0]!=12:
        word = "nd"
    elif date[0]%10 ==3 and date[0]!=13:
        word = "rd"
    else:
        word = "th"
    sup = "<sup>"
    sup_end = "</sup>"
    return (f"{date[0]}{sup}{word}{sup_end} {month} {date[2]}")

def both(date):
    z = "OR"
    return (f"{numerical(date)} {z} {verbose(date)}")

x = Easter(year)

if format == "numerical":
    result = str(numerical(x))
elif format == "verbose":
    result = str(verbose(x))
else:
    result = str(both(x))

print('<p>')
print("The Easter date of %s =<u>  <u/>" %(year), result)
print('</p>')
print('</body>')
print('</html>')
