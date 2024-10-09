import sys;
# Beispiel fuer Listenverarbeitung
def move (y, x):
    #print("\033[%d;%dH" % (y, x));
    sys.stdout.write("\033[%d;%dH" % (y, x));

for i in range( 255,1055):
    #   move( i, i);
    print( str(i)+ ':' + chr(i));