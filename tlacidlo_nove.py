import tkinter as tk

okno = tk.Tk()
okno.title("Prvý program")

odist = tk.Button(okno, text="odísť",fg="red", command=quit)
odist.pack(side=tk.LEFT)

def faktorial():
    faktorial_okno = tk.Toplevel(okno)
    faktorial_okno.title("Faktorial")
    faktorial_okno.geometry("200x200")

    vytaj = tk.Label(faktorial_okno, text="Vypočítaj si faktoriál",font = "Helvetica 16 bold italic", fg="Blue")
    vytaj.place(relx=0.2, rely=0.0)



faktorial_tlacidlo = tk.Button(okno, text="vypočítať faktoriál", fg="green", command=faktorial)
faktorial_tlacidlo.pack(side=tk.LEFT)




okno.mainloop()