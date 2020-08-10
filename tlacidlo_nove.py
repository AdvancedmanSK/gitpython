import tkinter as tk

okno = tk.Tk()
okno.title("Prvý program")

odist = tk.Button(okno, text="odísť",fg="red", command=quit)
odist.place(x=0, y=0)


#nove okno pre faktorial
def faktorial():
    faktorial_okno = tk.Toplevel(okno)
    faktorial_okno.title("Faktorial")
    faktorial_okno.geometry("310x200")

    vytaj = tk.Label(faktorial_okno, text="Vypočítaj si faktoriál",font = "Helvetica 14 bold italic", fg="Blue")
    vytaj.place(x=60, y=0)

    zadanie_cisel = tk.Label(faktorial_okno, text="Zadaj číslo:", font="Canvas 9", fg="green")
    zadanie_cisel.place(x=20, y=30)

    global vstup
    vstup = tk.Entry(faktorial_okno)
    vstup.place(x=100, y=30)


    def vypocet_faktorialu():
        n = int(vstup.get())
        fact = 1
    
        for i in range(1,n+1): 
            fact = fact * i 
        print(fact)

    spustac = tk.Button(faktorial_okno, text="Vypočítaj", command=vypocet_faktorialu)
    spustac.place(x=130, y=60)





faktorial_tlacidlo = tk.Button(okno, text="vypočítať faktoriál", fg="green", command=faktorial)
faktorial_tlacidlo.place(x=40, y=0)




okno.mainloop()