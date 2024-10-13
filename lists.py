import sys;
# Beispiel fuer Listenverarbeitung
#   Konstatnen fuer Unicode-Zeichen, lrou = links rechts, oben unten

def drawFrame():
    lr = chr(0x2500);
    LR = chr( 0x2501);
    ou = chr( 0x2502);
    OU = chr( 0x2503);
    ru = chr( 0x250c);
    RU = chr( 0x250f);
    lU = chr( 0x2510);
    LU = chr( 0x2513);
    ro = chr( 0x2514);
    RO = chr( 0x2517);
    lo = chr( 0x2518);
    LO = chr( 0x251b);
    rou = chr( 0x251c);
    rOU = chr( 0x2520);
    ROU = chr( 0x2523);
    lou = chr( 0x2524);
    lOU = chr( 0x2528);
    LOU = chr( 0x252b);
    lru = chr( 0x252c);
    LRu = chr( 0x252f);
    LRU = chr( 0x2533);
    lro = chr( 0x2534);
    LRo = chr( 0x2537);
    LRO = chr( 0x253b);
    lrou = chr( 0x253c);
    LRou = chr( 0x253f);
    lrOU = chr( 0x2542);
    LROU = chr( 0x254b);
    lineTop = RU + LR + LRu + LR + LRu + LR + LRU + LR + LRu + LR + LRu + LR + LRU + LR + LRu + LR + LRu + LR + LU;
    lineBot = RO + LR + LRo + LR + LRo + LR + LRO + LR + LRo + LR + LRo + LR + LRO + LR + LRo + LR + LRo + LR + LO;
    lineSep = rOU + lr + lrou + lr + lrou + lr + lrOU  + lr + lrou + lr + lrou + lr + lrOU  + lr + lrou + lr + lrou + lr + lOU;
    lineSEP = ROU + LR + LRou + LR + LRou + LR + LROU  + LR + LRou + LR + LRou + LR + LROU  + LR + LRou + LR + LRou + LR + LOU;
    lineTxt = OU + " " + ou + " " + ou + " " + OU + " " + ou + " " + ou + " " + OU + " " + ou + " " + ou + " " + OU;
    print( lineTop);
    print( lineTxt);
    print( lineSep);
    print( lineTxt);
    print( lineSep);
    print( lineTxt);
    print( lineSEP);
    print( lineTxt);
    print( lineSep);
    print( lineTxt);
    print( lineSep);
    print( lineTxt);
    print( lineSEP);
    print( lineTxt);
    print( lineSep);
    print( lineTxt);
    print( lineSep);
    print( lineTxt);
    print( lineBot);

def move (y, x):
    #print("\033[%d;%dH" % (y, x));
    sys.stdout.write("\033[%d;%dH" % (y, x));

#for i in range( 0x2500,0x257f):
#   #   move( i, i);
#    print( str(i)+ ':' + chr(i));

drawFrame();