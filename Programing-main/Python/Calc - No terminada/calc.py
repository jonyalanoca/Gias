from tkinter import *
root=Tk()
# root.iconbitmap("calc.ico")
root.title("Calculadora 1.0")
root.resizable(False,False)
root.config(bg="#6D6290")
#varible en pantalla

var_pantalla=StringVar()
var_operacion=StringVar()
var_aux=StringVar()
separar=BooleanVar(value=False)
puesto=IntVar(value=1)
valor=StringVar()

prueba=StringVar()
def pasar(n):
    if separar.get()==True:
        var_pantalla.set("")
        separar.set(False)
    valor.set(n)
    if n=="." and "." in var_pantalla.get():
        valor.set("")
    elif n=="." and var_pantalla.get()=="":
        valor.set("0.")
    if n=="0" and var_pantalla.get()=="":
        valor.set("")
    var_pantalla.set(var_pantalla.get() + valor.get())
def igual():
    if var_operacion.get()=="suma":
            var_pantalla.set(int(var_aux.get()) + int(var_pantalla.get()))
            var_aux.set(var_pantalla.get())
            var_operacion.set("")
            puesto.set(1)
    if var_operacion.get()=="resta":
            var_pantalla.set(int(var_aux.get()) - int(var_pantalla.get()))
            var_aux.set(var_pantalla.get())
            var_operacion.set("")
            puesto.set(1)
    if var_operacion.get()=="por":
            var_pantalla.set(int(var_aux.get()) * int(var_pantalla.get()))
            var_aux.set(var_pantalla.get())
            var_operacion.set("")
            puesto.set(1)
    if var_operacion.get()=="div":
            var_pantalla.set(int(var_aux.get()) / int(var_pantalla.get()))
            var_aux.set(var_pantalla.get())
            var_operacion.set("")
            puesto.set(1)
def funcion(m):
    if var_pantalla.get()!="":
        separar.set(True)
        if puesto.get()==1:
            var_operacion.set(m)
            var_aux.set(var_pantalla.get())
            
            puesto.set(2)
        elif puesto.get()==2:
            if var_operacion.get()=="suma":
                var_pantalla.set(int(var_aux.get()) + int(var_pantalla.get()))
                var_aux.set(var_pantalla.get())
                var_operacion.set("suma")
                
            elif var_operacion.get()=="resta":
                var_pantalla.set(int(var_aux.get()) - int(var_pantalla.get()))
                var_aux.set(var_pantalla.get())
                var_operacion.set("resta")
            elif var_operacion.get()=="por":
                var_pantalla.set(int(var_aux.get()) * int(var_pantalla.get()))
                var_aux.set(var_pantalla.get())
                var_operacion.set("por")
                
            elif var_operacion.get()=="div":
                var_pantalla.set(int(var_aux.get()) / int(var_pantalla.get()))
                
                prueba.set(int(var_pantalla.get()))
                var_aux.set(var_pantalla.get())
                var_operacion.set("div")
        var_operacion.set(m)
#----Frame---numeros
framepantalla=Frame(root,bg="#6D6290")
framepantalla.grid(row="0",column="0", pady=10)

framenums=Frame(root,bg="#6D6290")
framenums.grid(row="1", column="0", padx=10, pady=10)
#---Botones de los números
btn_num1=Button(framenums, text="1", justify="center" , width="4", height="2" ,bg="white", command=lambda:pasar("1"))
btn_num1.grid(row="2", column="0", padx=2, pady=2)

btn_num2=Button(framenums, text="2", justify="center" , width="4", height="2" ,bg="white", command=lambda:pasar("2"))
btn_num2.grid(row="2", column="1", padx=2, pady=2)

btn_num3=Button(framenums, text="3", justify="center" , width="4", height="2" ,bg="white",command=lambda:pasar("3"))
btn_num3.grid(row="2", column="2", padx=2, pady=2)

btn_num4=Button(framenums, text="4", justify="center" , width="4", height="2" ,bg="white",command=lambda:pasar("4"))
btn_num4.grid(row="1", column="0", padx=2, pady=2)

btn_num5=Button(framenums, text="5", justify="center" , width="4", height="2" ,bg="white",command=lambda:pasar("5"))
btn_num5.grid(row="1", column="1", padx=2, pady=2)

btn_num6=Button(framenums, text="6", justify="center" , width="4", height="2" ,bg="white",command=lambda:pasar("6"))
btn_num6.grid(row="1", column="2", padx=2, pady=2)

btn_num7=Button(framenums, text="7", justify="center" , width="4", height="2" ,bg="white",command=lambda:pasar("7"))
btn_num7.grid(row="0", column="0", padx=2, pady=2)

btn_num8=Button(framenums, text="8", justify="center" , width="4", height="2" ,bg="white",command=lambda:pasar("8"))
btn_num8.grid(row="0", column="1", padx=2, pady=2)

btn_num9=Button(framenums, text="9", justify="center" , width="4", height="2" ,bg="white",command=lambda:pasar("9"))
btn_num9.grid(row="0", column="2", padx=2, pady=2)

btn_num0=Button(framenums, text="0", justify="center" , width="4", height="2" ,bg="white",command=lambda:pasar("0"))
btn_num0.grid(row="3", column="0", padx=2, pady=2)
#----Botones extras
btn_punto=Button(framenums, text=".", justify="center" , width="4", height="2" ,bg="white",command=lambda:pasar("."))
btn_punto.grid(row="3", column="1", padx=2, pady=2)

btn_igual=Button(framenums, text="=", justify="center" , width="4", height="2" ,bg="red", command=lambda:igual())
btn_igual.grid(row="3", column="2", padx=2, pady=2)
#--Botones de operaciones 

btn_sumar=Button(framenums, text="+", justify="center" , width="4", height="2", bg="#AFAAC1",command=lambda:funcion("suma"))
btn_sumar.grid(row="3", column="3", padx=2, pady=2)

btn_restar=Button(framenums, text="-", justify="center" , width="4", height="2",bg="#AFAAC1",command=lambda:funcion("resta"))
btn_restar.grid(row="2", column="3", padx=2, pady=2)

btn_mult=Button(framenums, text="x", justify="center" , width="4", height="2",bg="#AFAAC1",command=lambda:funcion("por"))
btn_mult.grid(row="1", column="3", padx=2, pady=2)

btn_dividir=Button(framenums, text="/", justify="center" , width="4", height="2",bg="#AFAAC1",command=lambda:funcion("div"))
btn_dividir.grid(row="0", column="3", padx=2, pady=2)
#caja de pantalla+
box_pantalla=Entry(framepantalla, width="26", justify="right",  textvariable=var_pantalla, state=DISABLED)

box_pantalla.grid(row="0",pady=7, ipady=15)

nose=Entry(framepantalla, bg="blue",textvariable=prueba)
nose.grid(row="1")

otro=Button(framepantalla,text="hola", command=lambda:root.destroy())
otro.grid(row=2,sticky="w")
root.mainloop()