import tkinter

main_window = tkinter.Tk()

def tombol_ditekan():
    label2 = tkinter.Label(main_window, text="tombol ditekan")
    label2.pack()

label = tkinter.Label(main_window, text="Hello world \n ini adalah GUI sederhana \n menggunakan python")
tombol = tkinter.Button(main_window, text="Tombol", command_=_tombol_ditekan)
label.pack()
tombol.pack()
main_window.mainloop()