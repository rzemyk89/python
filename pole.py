

print "Witamy w programie obliczajacym pole"
print "------------------------------------"
print

# Wydrukuj menu:
print "Wybierz figure:"
print "1 Prostokat"
print "2 Kolo"


figura = input("> ")

# Oblicz pole:
if figura == 1:
  wysokosc = input("Wpisz wysokosc: ")
  szerokosc = input("Wpisz szerokosc: ")
  pole = wysokosc*szerokosc
else:
  promien = input("Wpisz promien: ")
  pole = 3.14*(promien**2)
print "Pole wynosi", pole
