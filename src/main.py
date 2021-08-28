#El codigo de esto es una basura, es la primera vez que uso esta mierda y no se como va
import Q6
import RLE
import aritmetic as ar
import huffman as hf
import Lz78
import Lz77
import Q7
from tkinter.ttk import *
from tkinter import *

#layers de los solucionadores
def huffman(tab1):
    #strings que van a cambiar
    global varrr_1, varrr_2, varrr_3, varrr_4, varrr_5, varrr_6, varrr_7, varrr_8
    varrr_1 = StringVar()
    varrr_1.set("La longitud fija del codigo es ")
    varrr_2 = StringVar()
    varrr_2.set("Los bits que ocupan la cadena son ")
    varrr_3 = StringVar()
    varrr_3.set("La entropia de la fuente es")
    varrr_4 = StringVar()
    varrr_4.set("El codigo optimo es")
    varrr_5 = StringVar()
    varrr_5.set("La longitud media es")
    varrr_6 = StringVar()
    varrr_6.set("La efficiencia es ")
    varrr_7 = StringVar()
    varrr_7.set("La longitud de compresion es ")
    varrr_8 = StringVar()
    varrr_8.set("El porcentaje de compresion ")
   
    #label declaracion
    lbl7_1 = Label(tab1,text="Huffman")
    lbl7_num_1 = Label(tab1, text="Pon la cadena")
    lbl7_num_2 = Label(tab1, textvariable=varrr_1)
    lbl7_num_3 = Label(tab1, textvariable=varrr_2)
    lbl7_num_4 = Label(tab1, textvariable=varrr_3)
    lbl7_num_5 = Label(tab1, textvariable=varrr_4)
    lbl7_num_6 = Label(tab1, textvariable=varrr_5)
    lbl7_num_7 = Label(tab1, textvariable=varrr_6)
    lbl7_num_8 = Label(tab1, textvariable=varrr_7)
    lbl7_num_9 = Label(tab1, textvariable=varrr_8)

    #posicion
    lbl7_1.place(x=10, y=10)
    lbl7_num_1.place(x=10, y=30)
    lbl7_num_2.place(x=10, y=50)
    lbl7_num_3.place(x=10, y=70)
    lbl7_num_4.place(x=10, y=90)
    lbl7_num_5.place(x=300, y=10)
    lbl7_num_6.place(x=300, y=30)
    lbl7_num_7.place(x=300, y=50)
    lbl7_num_8.place(x=300, y=70)
    lbl7_num_9.place(x=300, y=90)
    
    #entry
    global entry_hf_1
    entry_hf_1 = Entry(tab1)
    entry_hf_1.place(x=120, y=30)
    
    #funcionamiento
    def clicked_ar_1():
        cad = str(entry_hf_1.get())
        d = hf.mk_dct(cad) 
        varrr_1.set("La longitud fija del codigo es " + str(hf.Slen(d.values())))
        varrr_2.set("Los bits que ocupan la cadena son " + str(len(cad)*hf.Slen(d.values())))
        varrr_3.set("La entropia de la fuente es " +  str(hf.Entropy(hf.mk_dct(cad).values())))
        varrr_4.set("El codigo optimo es "+ str(hf.huffman(hf.mk_dct(cad))))
        varrr_5.set("La longitud media es " + str(hf.av_cwlen(hf.huffman(d),d)))
        varrr_6.set("La efficiencia es " + str(hf.efficiency(cad)))
        varrr_7.set("La longitud de compresion es " + str(hf.av_cwlen(hf.huffman(d),d)*len(cad)))
        varrr_8.set("El porcentaje de compresion " + str((1-(hf.av_cwlen(hf.huffman(d),d)*len(cad))/(len(cad)*hf.Slen(d.values())))*100))
    
    #boton 
    b_cp_1 = Button(tab1, text="comprueba",command=clicked_ar_1)
    b_cp_1.place(x=70, y=110)

def rle(tab2):
    #string variables
    global van1, van2, van3, van4, van5
    van1 = StringVar()
    van2 = StringVar()
    van3 = StringVar()
    van4 = StringVar() 
    van5 = StringVar()
    van1.set("El fichero comprimido ocupa ")
    van2.set("El mapa de bits tiene x filas")
    van3.set("EL mapa de bits tiene x ceros")
    van4.set("El fichero original ocupaba ")
    van5.set("La codificacion utilizando rle es ")
    #labels
    lbl7_1 = Label(tab2,text="RLE")
    lbl7_num_1 = Label(tab2, text="Pon la cadena en formato -> 7,1,1,4,1,7")
    lbl7_num_2 = Label(tab2, text="Pon el mapa de bits en formato -> 0X0,XXX,000")
    lbl7_num_5 = Label(tab2, textvariable=van1)
    lbl7_num_6 = Label(tab2, textvariable=van2)
    lbl7_num_7 = Label(tab2, textvariable=van3)
    lbl7_num_8 = Label(tab2, textvariable=van4)
    lbl7_num_9 = Label(tab2, textvariable=van5)
    #posicion
    lbl7_1.place(x=10, y=10)
    lbl7_num_1.place(x=10, y=30)
    lbl7_num_2.place(x=10, y=70)
    lbl7_num_5.place(x=400, y=10)
    lbl7_num_6.place(x=400, y=30)
    lbl7_num_7.place(x=400, y=50)
    lbl7_num_8.place(x=400, y=70)
    lbl7_num_9.place(x=400, y=90)
    #Entry
    global entry_rle_1, entry_rle_2
    entry_rle_1 = Entry(tab2)
    entry_rle_2 = Entry(tab2)
    entry_rle_1.place(x=10, y=50)
    entry_rle_2.place(x=10, y=90)
    #funcionamiento
    def clicked_rle_1():
        cad = str(entry_rle_1.get())
        cad2 = str(entry_rle_2.get()).split(",")
        van1.set("El fichero comprimido ocupa "+ str(RLE.RLE(cad)))
        van2.set("El mapa de bits tiene x filas " + str(RLE.RLE_2(cad)))
        van3.set("EL mapa de bits tiene x ceros " + str(RLE.RLE_3(cad)))
        van4.set("El fichero original ocupaba " + str(RLE.RLE_4(cad2)))
        van5.set("La codificacion utilizando rle es " + str(RLE.rle_encode(cad2)))
    
    #boton 
    b_cp_1 = Button(tab2, text="comprueba",command=clicked_rle_1)
    b_cp_1.place(x=10, y=110)

def menu_lz77(tab3):
    #strings variables
    global vannn1,vannn2,vannn3,vannn4,vannn5,vannn6,vannn7
    vannn1 = StringVar()
    vannn2 = StringVar()
    vannn3 = StringVar()
    vannn4 = StringVar()
    vannn5 = StringVar()
    vannn6 = StringVar()
    vannn7 = StringVar()
    vannn1.set("Elementos necesarios codificar la fuente S")
    vannn2.set("Descompresion del LZ77 ")
    vannn3.set("Cuanto ocupa la cadena original ")
    vannn4.set("Bits que ocupa la cadena comprimida ")
    vannn5.set("Tasa de compresion ")
    vannn6.set("Porcentaje de compresion ")
    vannn7.set("Compresion del LZ78 ")
    #labels
    lbl7_1 = Label(tab3,text="LZ77")
    lbl7_num_1 = Label(tab3, text="Pon las tuplas -> (0,0,X),(0,0,Y),(0,0,Z)")
    lbl7_num_2 = Label(tab3, text="Pon la cadena")
    lbl7_num_5 = Label(tab3, textvariable=vannn1)
    lbl7_num_6 = Label(tab3, textvariable=vannn2)
    lbl7_num_7 = Label(tab3, textvariable=vannn3)
    lbl7_num_8 = Label(tab3, textvariable=vannn4)
    lbl7_num_9 = Label(tab3, textvariable=vannn5)
    lbl7_num_10 = Label(tab3, textvariable=vannn6)
    lbl7_num_11 = Label(tab3, textvariable=vannn7)
    #posicion
    lbl7_1.place(x=10, y=10)
    lbl7_num_1.place(x=10, y=30)
    lbl7_num_2.place(x=10, y=70)
    lbl7_num_5.place(x=400, y=10)
    lbl7_num_6.place(x=400, y=30)
    lbl7_num_7.place(x=400, y=50)
    lbl7_num_8.place(x=400, y=70)
    lbl7_num_9.place(x=400, y=90)
    lbl7_num_10.place(x=400, y=110)
    lbl7_num_11.place(x=400, y=130)
    #Entry
    global entry_lz1_1, entry_lz1_2
    entry_lz1_1 = Entry(tab3)
    entry_lz1_2 = Entry(tab3)
    entry_lz1_1.place(x=10, y=50)
    entry_lz1_2.place(x=10, y=90)
    #funcionamiento
    def clicked_lz1_1():
        string = str(entry_lz1_1.get())
        string2 = str(entry_lz1_2.get())
        vannn1.set("Elementos necesarios codificar la fuente S " + str(Lz77.LZlen(string)))
        vannn2.set("Descompresion del LZ77 " + str(Lz77.decodeLZ(string)) )
        vannn3.set("Cuanto ocupa la cadena original "+ str(Lz77.cadlen(string)) )
        vannn4.set("Bits que ocupa la cadena comprimida "+ str(Lz77.btlz(15,7,string)) )
        vannn5.set("Tasa de compresion " + str(Lz77.compresstax(string)) )
        vannn6.set("Porcentaje de compresion "+ str(Lz77.compress_pert(string)) )
        vannn7.set("Compresion del LZ77 "+ str(Lz77.encodeLZ(string2)) )
    #boton 
    b_cp_1 = Button(tab3, text="comprueba",command=clicked_lz1_1)
    b_cp_1.place(x=10, y=110)

def menu_lz78(tab4):
    #strings variables
    global vann1,vann2,vann3,vann4,vann5,vann6,vann7
    vann1 = StringVar()
    vann2 = StringVar()
    vann3 = StringVar()
    vann4 = StringVar()
    vann5 = StringVar()
    vann6 = StringVar()
    vann7 = StringVar()
    vann1.set("Elementos necesarios codificar la fuente S")
    vann2.set("Bits que ocupan la cadena ")
    vann3.set("Algoritmo de compresion LZ78 ")
    vann4.set("Bits que ocupa la cadena comprimida ")
    vann5.set("Tasa de compresion ")
    vann6.set("Porcentaje de compresion ")
    vann7.set("Descompresion del LZ78 ")
    #labels
    lbl7_1 = Label(tab4,text="LZ78")
    lbl7_num_1 = Label(tab4, text="Pon la cadena")
    lbl7_num_2 = Label(tab4, text="Pon las tuplas -> (0,X),(0,Y),(0,Z)")
    lbl7_num_5 = Label(tab4, textvariable=vann1)
    lbl7_num_6 = Label(tab4, textvariable=vann2)
    lbl7_num_7 = Label(tab4, textvariable=vann3)
    lbl7_num_8 = Label(tab4, textvariable=vann4)
    lbl7_num_9 = Label(tab4, textvariable=vann5)
    lbl7_num_10 = Label(tab4, textvariable=vann6)
    lbl7_num_11 = Label(tab4, textvariable=vann7)
    #posicion
    lbl7_1.place(x=10, y=10)
    lbl7_num_1.place(x=10, y=30)
    lbl7_num_2.place(x=10, y=70)
    lbl7_num_5.place(x=400, y=10)
    lbl7_num_6.place(x=400, y=30)
    lbl7_num_7.place(x=400, y=50)
    lbl7_num_8.place(x=400, y=70)
    lbl7_num_9.place(x=400, y=90)
    lbl7_num_10.place(x=400, y=110)
    lbl7_num_11.place(x=400, y=130)
    #Entry
    global entry_lz2_1, entry_lz2_2
    entry_lz2_1 = Entry(tab4)
    entry_lz2_2 = Entry(tab4)
    entry_lz2_1.place(x=10, y=50)
    entry_lz2_2.place(x=10, y=90)
    #funcionamiento
    def clicked_lz2_1():
        string = str(entry_lz2_1.get())
        string2 = str(entry_lz2_2.get())
        vann1.set("Elementos necesarios codificar la fuente S " + str(Lz78.lzBit(string)))
        vann2.set("Bits que ocupan la cadena " + str(Lz78.lzLen(string)) )
        vann3.set("Algoritmo de compresion LZ78 "+ str(Lz78.encodeLZ(string)) )
        vann4.set("Bits que ocupa la cadena comprimida "+ str(Lz78.cadCompr(string)) )
        vann5.set("Tasa de compresion " + str(Lz78.comper(string)) )
        vann6.set("Porcentaje de compresion "+ str(Lz78.percent(string)) )
        vann7.set("Descompresion del LZ78 "+ str(Lz78.decodeLZ(string2)) )
    #boton 
    b_cp_1 = Button(tab4, text="comprueba",command=clicked_lz2_1)
    b_cp_1.place(x=10, y=110)
    
def aritmetico(tab5):
    global varr_1, varr_2
    #pregunta 1
    varr_1 = StringVar()
    varr_1.set("El resultado es ")
    #preguna 2
    varr_2 = StringVar()
    varr_2.set("El resultado es ")
    #label declaracion
        #pregunta 1
    lbl7_1 = Label(tab5,text="Codificacion aritmetica")
    lbl7_2 = Label(tab5, text="Escoge cualquier decimal del intervalo")
    lbl7_num_1 = Label(tab5, text="Pon la cadena")
    lbl7_num_2 = Label(tab5, textvariable=varr_1)
        #pregunta 2
    lbl7_3 = Label(tab5,text="Descodificacion aritmetica")
    lbl7_4 = Label(tab5, text="Formato probabilidades -> 0.33,0.33,0.33")
    lbl7_num2_1 = Label(tab5, text="Pon las probabilidades")
    lbl7_num2_2 = Label(tab5, text="Pon el valor de descodificacion")
    lbl7_num2_3 = Label(tab5, text="Pon el numero de caracteres")
    lbl7_num2_4 = Label(tab5, textvariable=varr_2)
    
    #posicion
        #pregunta 1
    lbl7_1.place(x=10, y=10)
    lbl7_2.place(x=10, y=30)
    lbl7_num_1.place(x=10, y=50)
    lbl7_num_2.place(x=10, y=70)
        #pregunta 2
    lbl7_3.place(x=10, y=120)
    lbl7_4.place(x=10, y=140)
    lbl7_num2_1.place(x=10, y=160)
    lbl7_num2_2.place(x=10, y=180)
    lbl7_num2_3.place(x=10, y=200)
    lbl7_num2_4.place(x=10, y=220)
    
    #Entry
    global entry_ar_1, entry_ar_2, entry_ar_3, entry_ar_4
        #pregunta 1
    entry_ar_1 = Entry(tab5)
    entry_ar_1.place(x=120, y=50)
        #pregunta 2
    entry_ar_2 = Entry(tab5)
    entry_ar_3 = Entry(tab5)
    entry_ar_4 = Entry(tab5)
    entry_ar_2.place(x=190, y=160)
    entry_ar_3.place(x=190, y=180)
    entry_ar_4.place(x=190, y=200)
    #funcionamiento
    def clicked_ar_1():
        cad = str(entry_ar_1.get())
        varr_1.set("El resultado es "+ str(ar.encodeAri(cad)))
    
    def clicked_ar_2():
        prob = [float(i) for i in str(entry_ar_2.get()).split(",")]
        num_1 = float(entry_ar_3.get())
        num_2 = int(entry_ar_4.get())
        varr_2.set("El resuktado es " + ar.decodeAri(num_1, ['A', 'B', 'C'], prob, num_2))
   
    #boton 
        #pregunta 1
    b_cp_1 = Button(tab5, text="comprueba",command=clicked_ar_1)
    b_cp_1.place(x=70, y=90)
        #pregunta 2
    b_cp_2 = Button(tab5, text="comprueba",command=clicked_ar_2)
    b_cp_2.place(x=70, y=240)

def clavePrivada(tab6):
    global var_1, var_2, var_3, var_4, var_5, var_6
        #pregunta 1
    var_1 = StringVar()
    var_1.set("El resultado es ")
        #pregunta 2
    var_2 = StringVar()
    var_2.set("El resultado es ")
        #preunta 3
    var_3 = StringVar()
    var_3.set("El resultado es ")
        #pregunta 4
    var_4 = StringVar()
    var_4.set("El resultado es ")
        #pregunta 5
    var_5 = StringVar()
    var_5.set("El resultado es ")    
        #pregunta 6
    var_6 = StringVar()
    var_6.set("El resultado es ")
    
    #label declaracion
        #pregunta 1 
    lbl6_1 = Label(tab6,text="Pregunta 1")
    lbl6_2 = Label(tab6, text="Determina el mensaje cifrado")
    lbl6_num_1 = Label(tab6, text="Pon el mensaje")
    lbl6_num_2 = Label(tab6, text="Pon la K")
    lbl6_num_3 = Label(tab6, textvariable=var_1)
        #pregunta 2
    lbl7_3 = Label(tab6, text="Pregunda 2")
    lbl7_4 = Label(tab6, text="Determina el mensaje cifrado")
    lbl7_num2_1 = Label(tab6, text="Pon el mensaje")
    lbl7_num2_2 = Label(tab6, text="Pon la K")
    lbl7_num2_3 = Label(tab6, textvariable=var_2)
        #pregunta 3
    lbl7_5 = Label(tab6, text="Pregunda 3")
    lbl7_6 = Label(tab6, text="Determinar la clave")
    lbl7_num3_1 = Label(tab6, text="Mensaje cifrado (c)")
    lbl7_num3_2 = Label(tab6, text="Mensaje (m)")
    lbl7_num3_3 = Label(tab6, textvariable=var_3)
        #pregunta 4
    lbl7_7 = Label(tab6, text="Pregunda 4")
    lbl7_8 = Label(tab6, text="Cifrado matricial")
    lbl7_num4_1 = Label(tab6, text="Pon el mensaje (m)")
    lbl7_num4_2 = Label(tab6, text="Pon la clave (K)")
    lbl7_num4_3 = Label(tab6, textvariable=var_4)
        #pregunta 5
    lbl7_9 = Label(tab6, text="Pregunda 5")
    lbl7_10 = Label(tab6, text="Cifrado matrical")
    lbl7_num5_1 = Label(tab6, text="Pon el mensaje cifrado (c)")
    lbl7_num5_2 = Label(tab6, text="Pon la clave (K)")
    lbl7_num5_3 = Label(tab6, textvariable=var_5)
        #pregunta 6
    lbl7_11 = Label(tab6, text="Pregunda 6 (NO CERRAR FUNCIONA LENTO)")
    lbl7_12 = Label(tab6, text="Cifrado matrical")
    lbl7_num6_1 = Label(tab6, text="Pon el mensaje cifrado (c)")
    lbl7_num6_2 = Label(tab6, text="Pon el mensaje (m)")
    lbl7_num6_3 = Label(tab6, textvariable=var_6)
    #posicion
        #pregunta 1
    lbl6_1.place(x=10, y=10)
    lbl6_2.place(x=10, y=30)
    lbl6_num_1.place(x=10, y=50)
    lbl6_num_2.place(x=10, y=70)
    lbl6_num_3.place(x=10, y=90)
        #pregunta 2
    lbl7_3.place(x=300, y=10)
    lbl7_4.place(x=300, y=30)
    lbl7_num2_1.place(x=300, y=50)
    lbl7_num2_2.place(x=300, y=70)
    lbl7_num2_3.place(x=300, y=90)
        #pregunta 3
    lbl7_5.place(x=550, y=10)
    lbl7_6.place(x=550, y=30)
    lbl7_num3_1.place(x=550, y=50)
    lbl7_num3_2.place(x=550, y=70)
    lbl7_num3_3.place(x=550, y=90)
        #pregunta 4
    lbl7_7.place(x=10, y=150)
    lbl7_8.place(x=10, y=170)
    lbl7_num4_1.place(x=10, y=190)
    lbl7_num4_2.place(x=10, y=210)
    lbl7_num4_3.place(x=10, y=230)
        #pregunta 5   
    lbl7_9.place(x=270, y=150)
    lbl7_10.place(x=270, y=170)
    lbl7_num5_1.place(x=270, y=190)
    lbl7_num5_2.place(x=270, y=210)
    lbl7_num5_3.place(x=270, y=230)
        #pregunta 6
    lbl7_11.place(x=550, y=150)
    lbl7_12.place(x=550, y=170)
    lbl7_num6_1.place(x=550, y=190)
    lbl7_num6_2.place(x=550, y=210)
    lbl7_num6_3.place(x=550, y=230)
    #Entry
    global entry_cp1_1, entry_cp1_2, entry_cp1_3, entry_cp1_4
    global entry_cp1_5, entry_cp1_6, entry_cp1_7, entry_cp1_8
    global entry_cp1_9, entry_cp1_10, entry_cp1_11, entry_cp1_12
        #pregunta 1
    entry_cp1_1 = Entry(tab6)
    entry_cp1_2 = Entry(tab6)
    entry_cp1_1.place(x=100, y=50)
    entry_cp1_2.place(x=100, y=70)    
        #preugunta 2
    entry_cp1_3 = Entry(tab6)
    entry_cp1_4 = Entry(tab6)
    entry_cp1_3.place(x=395, y=50)
    entry_cp1_4.place(x=395, y=70)
        #pregunta 3
    entry_cp1_5 = Entry(tab6)
    entry_cp1_6 = Entry(tab6)
    entry_cp1_5.place(x=660, y=50)
    entry_cp1_6.place(x=660, y=70)        
        #pregunta 4    
    entry_cp1_7 = Entry(tab6)
    entry_cp1_8 = Entry(tab6)
    entry_cp1_7.place(x=125, y=190)   
    entry_cp1_8.place(x=125, y=210)    
        #pregunta 5
    entry_cp1_9 = Entry(tab6)
    entry_cp1_10 = Entry(tab6)
    entry_cp1_9.place(x=420, y=190)
    entry_cp1_10.place(x=420, y=210)         
        #pregunta 6 
    entry_cp1_11 = Entry(tab6)
    entry_cp1_12= Entry(tab6)
    entry_cp1_11.place(x=700, y=190)
    entry_cp1_12.place(x=700, y=210)     
    
    #funcionamiento
    def clicked_cp_1():
        a = str(entry_cp1_1.get())
        b = int(entry_cp1_2.get())
        var_1.set("El resultado es  "+ Q6.primero_segundo(a, b, 0))
    
    def clicked_cp_2(): 
        a = str(entry_cp1_3.get())
        b = int(entry_cp1_4.get())
        var_2.set("El resultado es " + Q6.primero_segundo(a, b, 1))
    
    def clicked_cp_3(): 
        m = str(entry_cp1_5.get())
        e = str(entry_cp1_6.get())
        var_3.set("El resultado es " + Q6.tercero(e,m))
    
    def clicked_cp_4(): 
        n = str(entry_cp1_7.get())
        m = str(entry_cp1_8.get())

        var_4.set("El resultado es " + Q6.cuarto(n,m))
    
    def clicked_cp_5(): 
        d = str(entry_cp1_9.get())
        n = str(entry_cp1_10.get())
        var_5.set("El resultado es " + Q6.quinto(d,n))
   
    def clicked_cp_6():
        c = str(entry_cp1_11.get())
        d = str(entry_cp1_12.get())
        var_6.set("El resultado es " + Q6.sexto(c,d))
    #boton
        #pregunta 1
    b_cp_1 = Button(tab6, text="comprueba",command=clicked_cp_1)
    b_cp_1.place(x=50, y=110)
        #pregunta 2
    b_cp_2 = Button(tab6, text="comprueba",command=clicked_cp_2)
    b_cp_2.place(x=360, y=110)
        #pregunta 3
    b_cp_3 = Button(tab6, text="comprueba",command=clicked_cp_3)
    b_cp_3.place(x=615, y=110)
        #pregunta 4
    b_cp_4 = Button(tab6, text="comprueba",command=clicked_cp_4)
    b_cp_4.place(x=80, y=250)
        #pregunta 5
    b_cp_5 = Button(tab6, text="comprueba",command=clicked_cp_5)
    b_cp_5.place(x=400, y=250)
        #pregunta 6
    b_cp_6 = Button(tab6, text="comprueba",command=clicked_cp_6)
    b_cp_6.place(x=600, y=250)

def clavePublica(tab7):
    global var, var2, var3, var4, var5
        #pregunta 1
    var = StringVar()
    var.set("Es valida?")
        #pregunta 2
    var2 = StringVar()
    var2.set("Su clave privada d es ")
        #preunta 3
    var3 = StringVar()
    var3.set("El resultado es ")
        #pregunta 4
    var4 = StringVar()
    var4.set("El resultado es ")
        #pregunta 5
    var5 = StringVar()
    var5.set("El mensaje original era ")    
    #label declaracion
        #pregunta 1 
    lbl7_1 = Label(tab7,text="Pregunta 1")
    lbl7_2 = Label(tab7, text="Se determinan si las claves son validas")
    lbl7_num_1 = Label(tab7, text="Pon la 'e'")
    lbl7_num_2 = Label(tab7, text="Pon la 'n'")
    lbl7_num_3 = Label(tab7, textvariable=var)
        #pregunta 2
    lbl7_3 = Label(tab7, text="Pregunda 2")
    lbl7_4 = Label(tab7, text="Se determina el valor 'd'")
    lbl7_num2_1 = Label(tab7, text="Pon la 'e'")
    lbl7_num2_2 = Label(tab7, text="Pon la 'n'")
    lbl7_num2_3 = Label(tab7, textvariable=var2)
        #pregunta 3
    lbl7_5 = Label(tab7, text="Pregunda 3")
    lbl7_6 = Label(tab7, text="Sirve para cifrar el mensaje")
    lbl7_num3_1 = Label(tab7, text="Pon el mensaje (m)")
    lbl7_num3_2 = Label(tab7, text="Pon la 'd'")
    lbl7_num3_3 = Label(tab7, text="Pon la 'n'")
    lbl7_num3_4 = Label(tab7, textvariable=var3)
        #pregunta 4
    lbl7_7 = Label(tab7, text="Pregunda 4")
    lbl7_8 = Label(tab7, text="Sirve para signar")
    lbl7_num4_1 = Label(tab7, text="Pon el mensaje (m)")
    lbl7_num4_2 = Label(tab7, text="Pon la 'd'")
    lbl7_num4_3 = Label(tab7, text="Pon la 'n'")
    lbl7_num4_4 = Label(tab7, textvariable=var4)
        #pregunta 5
    lbl7_9 = Label(tab7, text="Pregunda 4")
    lbl7_10 = Label(tab7, text="Devuelve el mensaje sin cifrar")
    lbl7_num5_1 = Label(tab7, text="Pon el cifrado ")
    lbl7_num5_2 = Label(tab7, text="Pon la 'd'")
    lbl7_num5_3 = Label(tab7, text="Pon la 'e'")
    lbl7_num5_4 = Label(tab7, textvariable=var5)

    #posicion
        #pregunta 1
    lbl7_1.place(x=10, y=10)
    lbl7_2.place(x=10, y=30)
    lbl7_num_1.place(x=10, y=50)
    lbl7_num_2.place(x=10, y=70)
    lbl7_num_3.place(x=10, y=90)
        #pregunta 2
    lbl7_3.place(x=220, y=10)
    lbl7_4.place(x=220, y=30)
    lbl7_num2_1.place(x=220, y=50)
    lbl7_num2_2.place(x=220, y=70)
    lbl7_num2_3.place(x=220, y=90)
        #pregunta 3
    lbl7_5.place(x=440, y=10)
    lbl7_6.place(x=440, y=30)
    lbl7_num3_1.place(x=440, y=50)
    lbl7_num3_2.place(x=440, y=70)
    lbl7_num3_3.place(x=440, y=90)
    lbl7_num3_4.place(x=440, y=110)
        #pregunta 4
    lbl7_7.place(x=10, y=150)
    lbl7_8.place(x=10, y=170)
    lbl7_num4_1.place(x=10, y=190)
    lbl7_num4_2.place(x=10, y=210)
    lbl7_num4_3.place(x=10, y=230)
    lbl7_num4_4.place(x=10, y=250)
        #pregunta 5   
    lbl7_9.place(x=350, y=150)
    lbl7_10.place(x=350, y=170)
    lbl7_num5_1.place(x=350, y=190)
    lbl7_num5_2.place(x=350, y=210)
    lbl7_num5_3.place(x=350, y=230)
    lbl7_num5_4.place(x=350, y=250)  
    #Entry
    global entry_cp2_1, entry_cp2_2, entry_cp2_3, entry_cp2_4
    global entry_cp2_5, entry_cp2_6, entry_cp2_7, entry_cp2_8
    global entry_cp2_9, entry_cp2_10, entry_cp2_11, entry_cp2_12, entry_cp2_13
        #pregunta 1
    entry_cp2_1 = Entry(tab7)
    entry_cp2_2 = Entry(tab7)
    entry_cp2_1.place(x=70, y=50)
    entry_cp2_2.place(x=70, y=70)    
        #preugunta 2
    entry_cp2_3 = Entry(tab7)
    entry_cp2_4 = Entry(tab7)
    entry_cp2_3.place(x=290, y=50)
    entry_cp2_4.place(x=290, y=70)
        #pregunta 3
    entry_cp2_5 = Entry(tab7)
    entry_cp2_6 = Entry(tab7)
    entry_cp2_7 = Entry(tab7)
    entry_cp2_5.place(x=550, y=50)
    entry_cp2_6.place(x=550, y=70)   
    entry_cp2_7.place(x=550, y=90) 
        #pregunta 4
    entry_cp2_8 = Entry(tab7)
    entry_cp2_9 = Entry(tab7)
    entry_cp2_10 = Entry(tab7)
    entry_cp2_8.place(x=140, y=190)
    entry_cp2_9.place(x=140, y=210)   
    entry_cp2_10.place(x=140, y=230) 
        #pregunta 5    
    entry_cp2_11 = Entry(tab7)
    entry_cp2_12= Entry(tab7)
    entry_cp2_13 = Entry(tab7)
    entry_cp2_11.place(x=450, y=190)
    entry_cp2_12.place(x=450, y=210)   
    entry_cp2_13.place(x=450, y=230)     
    #funcionamiento
    def clicked_cp2_1():
        num_1 = int(entry_cp2_1.get())
        num_2 = int(entry_cp2_2.get())
        var.set("Esta clave "+ Q7.pregunta_1(num_1, num_2) +" es valida")
    
    def clicked_cp2_2(): 
        e = int(entry_cp2_3.get())
        n = int(entry_cp2_4.get())
        var2.set("Su clave privada d es " + str(Q7.pregunta_2(e, n)))
    
    def clicked_cp2_3(): 
        m = int(entry_cp2_5.get())
        e = int(entry_cp2_6.get())
        n = int(entry_cp2_7.get())
        var3.set("El resultado es " + str(Q7.pregunta_3(e,m,n)))
    
    def clicked_cp2_4(): 
        m = int(entry_cp2_8.get())
        d = int(entry_cp2_9.get())
        n = int(entry_cp2_10.get())
        var4.set("El resultado es " + str(Q7.pregunta_4(d,m,n)))
    
    def clicked_cp2_5(): 
        c = int(entry_cp2_11.get())
        d = int(entry_cp2_12.get())
        e = int(entry_cp2_13.get())
        var5.set("El mensaje original era " + str(Q7.pregunta_4(d,c,e)))
    
    #boton
        #pregunta 1
    b_cp_1 = Button(tab7, text="comprueba",command=clicked_cp2_1)
    b_cp_1.place(x=50, y=110)
        #pregunta 2
    b_cp_2 = Button(tab7, text="comprueba",command=clicked_cp2_2)
    b_cp_2.place(x=270, y=110)
        #pregunta 3
    b_cp_3 = Button(tab7, text="comprueba",command=clicked_cp2_3)
    b_cp_3.place(x=570, y=110)
        #pregunta 4
    b_cp_4 = Button(tab7, text="comprueba",command=clicked_cp2_4)
    b_cp_4.place(x=80, y=270)
        #pregunta 5
    b_cp_5 = Button(tab7, text="comprueba",command=clicked_cp2_5)
    b_cp_5.place(x=400, y=270)

def About(tab8):
    lbl7_1 = Label(tab8,text="Programa para solucionar problemas teoricos de IS.\nSi algo no funciona avisadme por discord.\nTodos los derechos reservados a sibus.\nMaxima discrecion con los profes de esto")
    lbl7_1.place(x=10, y=10)


window = Tk()

window.title("Welcome to LikeGeeks app")

tab_control = Notebook(window)

tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)
tab4 = Frame(tab_control)
tab5 = Frame(tab_control)
tab6 = Frame(tab_control)
tab7 = Frame(tab_control)
tab8 = Frame(tab_control)

tab_control.add(tab1, text='huffman')
tab_control.add(tab2, text='RLE')
tab_control.add(tab3, text='Lz77')
tab_control.add(tab4, text='Lz78')
tab_control.add(tab5, text='aritmetico')
tab_control.add(tab6, text='clave Privada')
tab_control.add(tab7, text='clave Publica')
tab_control.add(tab8, text="About")

#huffman
huffman(tab1)

#RLE
rle(tab2)

#lz77
menu_lz77(tab3)

#lz78
menu_lz78(tab4)

#aritmetico
aritmetico(tab5)

#clavePrivada
clavePrivada(tab6)

#clavePublica
clavePublica(tab7)

#About
About(tab8)

tab_control.pack(expand=1, fill='both')


window.title('MO41641 resolver')
window.geometry("1000x360+10+10")
window.mainloop()