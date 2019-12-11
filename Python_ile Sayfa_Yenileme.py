import sys  
import urllib2

while True:
  about_page=urllib2.urlopen("http://localhost/about.php").read()
  if "KEY" in about_page:
     print(about_page)
     sys.exit(0) 

#Yüzlerce sayfa içinde KEY değerimizin hangi sayfada olduğunu bulmak için kullanabiliriz.