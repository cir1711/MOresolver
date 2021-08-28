# MOresolver

Se trata de un programa para resolver problemas de universidad sobre criptografía y compresión de datos. Es una versión muy verde aún falta revisar y mejorar algunas cosas. Funciona en casi su totalidad, las funciones de encode de los LZ pueden equivocarse con una probabilidad del 40%.

## Instalación

El programa usa tres librerías como son numpy, sympy y tkinter. Para instalarlas en caso de no tenerlas utiliza el comando pip, **si no te funciona usa el pip3**.

```console
pip install tk
pip install numpy
pip install sympy
```
## Metodo de uso

Es simple rellenas la información con el formato que pidan, en algunos casos se explica un poco el formato (ejemplo para lz77 `(0,0,A),(0,0,B),(2,1,C)`). Igualmente explicaré brevemente los que más problemas pueden dar. Para utilizarlo usa un ide cualquiera o escribe en la consola el comando `python main.py` asegurate de estar en la **carpeta \src**. En Linux la interfaz se mueve y puede que no se vea bien, en macOS no lo he comprobado.

### RLE
El formato de las entradas son los siguientes:
- Para la primera entrada es donde va la cadena de números el formato requerido es este: `9,7,1,1,0,3,2,2,2,0,2,1,4,2,0,5,3,1,3,4,2,8,1,5,2,1,1,0,7,2`
- Para el mapa de bits se utiliza este formato: `0000000X0,XXX00XX00,XX0XXXX00,XXXXX000X,000XXXX00,00000000X,00000XX0X,XXXXXXX00`

### LZ77 y LZ78
El encode funciona regulero, en alguna revisión se intentará que funcione para el 100% de los casos. El formato del lz78 es igual que el del 77 pero con duplas.

### Clave simétrica
Las claves para ciertas de las preguntas tienen que tener sentido si no el programa fallara debido a las dimensiones y para la pregunta 6 el programa parece que se congela, no es el caso. Simplemente esperad un tiempo y saldrá el resultado.

## Programa

El programa está hecho para practicar una asignatura así que es probable que algunas cosas nunca se solucionen, igualmente estoy pensando añadir códigos correctores que también era parte del temario así como arreglar los encodes de los LZ. Por tanto tenemos que:

| Funcional         | Con Errores   |
| -------------     |:-------------:|
| Huffman           | LZ77          |
| RLE               | LZ78          |
| Aritmetico        |Clave simetrica|
| Clave simetrica   |               |
| Clave Privada     |               |

### To do list
- [x] Algoritmos de compresion basicos
- [x] Algoritmos basicos de criptografia simetrica y publica (metodo de cesar, (e,n),...)
- [ ] Arreglar lz77 y lz78
- [ ] Meter algoritmos de correccion de errores