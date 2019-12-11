import sys
import urllib2
 
sayfa=urllib2.urlopen("localhost/alıstırma.php?name=mustafa").read()
 

while True:
  ilk_split=sayfa.split("<pre>")                 #<pre> taginin içindeki captcha kodunu okuyabilmek için bunu kullandık.
  ikinci_split=ilk_split[1].split("</pre>")     #pre tagını bitirmek ve sadece içindeki kodu okumak için bunu kullandık.
  sayfa=urllib2.urlopen("localhost/alıstırma.php?name=mustafa&captcha="+ikinci_split[0]).read()  
#sadece captcha kodumuzu yazdırmaya yarar.


  if "FLAG" in sayfa;          #FLAG bulunana kadar döngü devam eder.
    print(sayfa)
    sys.exit(0)

#Bu yöntem ile istediğimiz kadar captcha kodunu bypass edebilir.Fakat "<pre>" tagında tanımlı olması lazım ve GET metodunu kullanması gereklidir.