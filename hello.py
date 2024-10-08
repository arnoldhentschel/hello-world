import time, locale, requests;
from datetime import datetime;
mach01 = False;

if (mach01):
    deinname = input( 'Geben Sie bitte Ihren Namen ein: ');
    print( 'Hallo %s! ' %deinname);
    # locale.setlocale( locale.LC_ALL, 'de_DE'); #linux, macos
    # locale.setlocale( locale.LC_ALL, 'de_DE'); #windows
    thetime = time.strftime( 'heute ist %A, der %d.%B.');
    print( thetime)

    response = requests.get( 'https://httpbin.org/get?q=123');
    print( response.json());

s = "ich bin lang";
print( "Die Zeichenkette <" + s + ">")
print( "s[4:7]");
print( s[4:7]);
print( "s[4:]");
print( s[4:]);
print( "s[:3]");
print( s[:3]);
print( "s[-4:]");
print( s[-4:]);
print( "s[-4:-2]");
print( s[-4:-2]);
print( "s[::2]");
print( s[::2]);
print( "s[::-1]");
print( s[::-1]);
print( "s[:7][::-1]");
print( s[:7][::-1]);
print( "s.partition(\"bin\")");
print( s.partition("bin"));
print( "s.split(\"bin\")");
print( s.split("bin"));
n = datetime.now();
print( n);
print( n.strftime("%d.%m.%Y %H:%M.%s"));

#!/usr/bin/env python3
# Beispielprogramm measure.py
import time, math
start = time.process_time()

# sinnlos Zeit totschlagen
for i in range(1, 1000000):  
  x=math.sin(i)

end = time.process_time()    
print(end - start, 'Sekunden')
