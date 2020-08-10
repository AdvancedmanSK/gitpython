import tkinter as tk

okno = tk.Tk()
okno.title("Prvý program")

odist = tk.Button(okno, text="odísť",fg="red", command=quit)
odist.place(relx=0.0, rely=0.0)


#nove okno pre faktorial
def faktorial():
    faktorial_okno = tk.Toplevel(okno)
    faktorial_okno.title("Faktorial")
    faktorial_okno.geometry("310x200")

    vytaj = tk.Label(faktorial_okno, text="Vypočítaj si faktoriál",font = "Helvetica 14 bold italic", fg="Blue")
    vytaj.place(relx=0.2, rely=0.0)

    zadanie_cisel = tk.Label(faktorial_okno, text="Zadaj číslo:", font="Canvas 9", fg="green")
    zadanie_cisel.place(relx=0.1, rely=0.15)


    vstup = tk.Entry(faktorial_okno)
    vstup.place(relx=0.32, rely=0.15)



faktorial_tlacidlo = tk.Button(okno, text="vypočítať faktoriál", fg="green", command=faktorial)
faktorial_tlacidlo.place(relx=0.3, rely=0.0)




okno.mainloop()