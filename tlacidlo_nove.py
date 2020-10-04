import tkinter as tk
import time


okno = tk.Tk()
okno.title("Prvý program")
okno.geometry("300x200")

odist = tk.Button(okno, text="odísť", fg="red", command=quit)
odist.place(x=130, y=30)


# nove okno pre faktorial
def faktorial():
 
    faktorial_okno = tk.Toplevel(okno)
    faktorial_okno.title("Faktorial")
    faktorial_okno.geometry("310x200")

    vytaj = tk.Label(faktorial_okno, text="Vypočítaj si faktoriál",
                     font="Helvetica 14 bold italic", fg="Blue")
    vytaj.place(x=60, y=0)

    zadanie_cisel = tk.Label(
        faktorial_okno, text="Zadaj číslo:", font="Canvas 9", fg="green")
    zadanie_cisel.place(x=20, y=30)

    vstup = tk.Entry(faktorial_okno)
    vstup.place(x=100, y=30)


    def vypocet_faktorialu():
        vysledok = tk.Label(faktorial_okno, text=("      "*100), font="Canvas 9",)
        vysledok.place(x=100, y=100)

        
        
        n = int(vstup.get())
        fact = 1

        for i in range(1, n+1):
            fact = fact * i

        vysledok = tk.Label(faktorial_okno, text=(str(fact)), font="Canvas 9", fg="#97F23D")
        vysledok.place(x=100, y=100)

    spustac = tk.Button(faktorial_okno, text="Vypočítaj",command=vypocet_faktorialu)
    spustac.place(x=130, y=60)


faktorial_tlacidlo = tk.Button(
    okno, text="vypočítať faktoriál", fg="green", command=faktorial)
faktorial_tlacidlo.place(x=100,y=1)


okno.mainloop()
