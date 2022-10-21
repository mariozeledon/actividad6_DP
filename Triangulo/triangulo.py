import tkinter
import math

ventana = tkinter.Tk()
ventana.geometry("400x500")

fuenteTitulo = ("Arial Black",24)
fuenteElemento = ("Arial",18)
resultado = 0.0

def hipoteusa():
    resultado = math.sqrt(float(txt_num1.get())**2+float(txt_num2.get())**2)
    lbl_resultado["text"] = resultado

def area():
    resultado = (float(txt_num1.get())*float(txt_num2.get()))/2
    lbl_resultado["text"] = resultado

lbl_titulo = tkinter.Label(ventana, text="Triángulo", font = fuenteTitulo)
lbl_titulo.pack(fill = tkinter.X)

lbl_num1 = tkinter.Label(ventana, text="Ingrese el cateto a", font = fuenteElemento)
lbl_num1.pack(fill = tkinter.X, pady =3)

txt_num1 = tkinter.Entry(ventana, font = fuenteElemento)
txt_num1.pack(fill = tkinter.X, pady=3)

lbl_num2 = tkinter.Label(ventana, text="Ingrese el cateto b", font = fuenteElemento)
lbl_num2.pack(fill = tkinter.X, pady =3)

txt_num2 = tkinter.Entry(ventana, font = fuenteElemento)
txt_num2.pack(fill = tkinter.X, pady=3)

btn_hipo = tkinter.Button(ventana, text="Hipotenusa", font=fuenteElemento, bg="green", command=hipoteusa)
btn_hipo.pack(fill = tkinter.X, pady=3)

btn_area = tkinter.Button(ventana, text="Area", font=fuenteElemento, bg="yellow", command=area)
btn_area.pack(fill = tkinter.X, pady=3)

lbl_resultado = tkinter.Label(ventana, text="Resultado", font=fuenteElemento)
lbl_resultado.pack(fill = tkinter.X, pady=2)

ventana.mainloop()