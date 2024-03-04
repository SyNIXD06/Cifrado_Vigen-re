En el cifrado Vigenère, cada letra del texto se cifra usando un cifrado César diferente, el cual es determinado por
una letra correspondiente en la clave. Si la clave es más corta que el texto, la clave se repite hasta que tenga la
misma longitud que el texto. Por ejemplo, si la clave es "ABC", la primera letra del texto se cifraría con un
desplazamiento de 1 (por la 'A'), la segunda con un desplazamiento de 2 (por la 'B'), la tercera con un
desplazamiento de 3 (por la 'C'), y luego se repite el patrón para las letras subsiguientes.
El cifrado Vigenère se consideró irrompible durante muchos años debido a su uso de múltiples alfabetos de cifrado.
Sin embargo, a finales del siglo XIX, el criptógrafo británico Charles Babbage descubrió una forma de romperlo al
analizar las frecuencias de las letras y encontrar repeticiones, un método conocido como análisis de frecuencia.
Un aspecto importante del cifrado Vigenère es que el número de posibles claves aumenta exponencialmente con la
longitud de la clave. Por ejemplo, una clave de una sola letra solo tiene 26 posibles claves (correspondientes a las
26 letras del alfabeto). Sin embargo, una clave de dos letras tiene 676 posibles claves (26x26), una de tres letras
tiene 17,576 (26x26x26), y así sucesivamente.
