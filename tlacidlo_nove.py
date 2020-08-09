import tkinter as tk

okno = tk.Tk()

odist = tk.Button(okno, text="odísť",fg="red", command=quit)
odist.pack(side=tk.LEFT)

def faktorial():
    faktorial_okno = tk.Toplevel(okno)
    faktorial_okno.title("Faktorial")
    faktorial_okno.geometry("200x200")

faktorial_tlacidlo = tk.Button(okno, text="vypočítať faktoriál", fg="green", command=faktorial)
faktorial_tlacidlo.pack(side=tk.LEFT)




okno.mainloop()