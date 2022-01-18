#1 Escribe el código para imprimir una cadena literal que diga “Hola, mundo” 
print( "Hola, mundo" )
#2a  Almacena tu nombre en una variable y luego úsala para imprimir la cadena “¡Hola, {{tu nombre}}!” usando una coma en la función print
name ="Karen"
print( "¡Hola,", name"!" )
#2b Almacena tu nombre en una variable y luego úsala para imprimir la cadena “¡Hola, {{tu nombre}}!” usando un + en la función print
name ="Karen"
print( "¡Hola," + name + "!" )
#3a Almacena tu número favorito en una variable y luego úsala para imprimir la cadena “¡Hola, {{num}}!” usando una coma en la función print
name = 20
print( "¡Hola", 20, "!" )
#3b Almacena tu número favorito en una variable y luego úsala para imprimir la cadena “¡Hola, {{num}}!” usando un + en la función print
name = 20
print( "¡Hola" + str(42) + "!" ) # con un + -- ¡Esta debería darnos un error!
#4a Almacena dos de tus comidas favoritas en variables y luego úsalas para imprimir la cadena “Amo comer {{comida_uno}} y {{comida_dos}}.” con el método format 
favorito_comida1 = "ceviche"
favorito_comida2 = "pizza"
print( "Amo comer{} and {}.".format(favorito_comida1,favorito_comida2) )
#4b Almacena dos de tus comidas favoritas en variables y luego úsalas para imprimir la cadena “Amo comer {{comida_uno}} y {{comida_dos}}.” con cadenas “f”
favorito_comida1 = "ceviche"
favorito_comida2 = "pizza"
print( f"Amo comer {favorito_comida1} and {favorito_comida2}.") 
