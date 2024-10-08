import time, locale, requests;

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