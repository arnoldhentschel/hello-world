import time, locale;
name = input( 'Geben Sie bitte Ihren Namen ein: ');
print( 'Hallo %s! ', name);
# locale.setlocale( locale.LC_ALL, 'de_DE'); #linux, macos
# locale.setlocale( locale.LC_ALL, 'de_DE'); #windows
thetime = time.strftime( 'heute ist %A, der %d.%B.');
print( thetime)

