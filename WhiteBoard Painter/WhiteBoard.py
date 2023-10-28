from tkinter import *

app = Tk()
app.title("Resim Çizim Uygulaması")
app.geometry("1050x570+150+150")
app.configure(bg="#f2f3f5")
app.resizable(False, False)

icon_img = PhotoImage(file="logo.png")
app.iconphoto(False, icon_img)

canvas = Canvas(app, bg="#ffffff", width=100, height=393)
canvas.place(x=18, y=28)

# Seçilen rengi saklamak için bir değişken oluşturun
secilen_renk = "black"

def renk_goster(renk):
    global secilen_renk
    secilen_renk = renk

def tuvali_temizle():
    draw_canvas.delete("all")

def renk_paletini_goster():
    renk_listesi = ["black", "red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "cyan", "white", "violet", "indigo", "lime", "magenta", "turquoise", "gold", "sienna", "tan"]
    dikdortgen_yukseklik = 20
    sutun_sayisi = 2
    satir_sayisi = len(renk_listesi) // sutun_sayisi

    for i, renk in enumerate(renk_listesi):
        x1 = (i % sutun_sayisi) * (100 // sutun_sayisi)
        y1 = (i // sutun_sayisi) * dikdortgen_yukseklik
        x2 = x1 + (100 // sutun_sayisi)
        y2 = y1 + dikdortgen_yukseklik
        id = canvas.create_rectangle(x1, y1, x2, y2, fill=renk)
        canvas.tag_bind(id, '<Button-1>', lambda x, c=renk: renk_goster(c))

renk_paletini_goster()

# Çizim tuvaline çerçeve ekleyin
draw_canvas = Canvas(app, width=900, height=512, background="white", cursor="hand2", bd=2, relief="ridge")
draw_canvas.place(x=110, y=20)

cizim = False
son_x = 0
son_y = 0

def cizime_basla(event):
    global cizim, son_x, son_y
    cizim = True
    son_x = event.x
    son_y = event.y
    draw_canvas.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill=secilen_renk)

def ciz(event):
    global cizim, son_x, son_y
    if cizim:
        cizgi_kalinligi = cizgi_kalinligi_degiskeni.get()
        draw_canvas.create_line(son_x, son_y, event.x, event.y, fill=secilen_renk, width=cizgi_kalinligi)
    son_x = event.x
    son_y = event.y

def cizimi_bitir(event):
    global cizim
    cizim = False

draw_canvas.bind("<Button-1>", cizime_basla)
draw_canvas.bind("<B1-Motion>", ciz)
draw_canvas.bind("<ButtonRelease-1>", cizimi_bitir)

cizgi_kalinligi_degiskeni = IntVar()
cizgi_kalinligi_degiskeni.set(2)
cizgi_kalinligi_menu = OptionMenu(app, cizgi_kalinligi_degiskeni, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
cizgi_kalinligi_menu.place(x=40, y=470)

temizle_dugme = Button(app, text="Temizle", command=tuvali_temizle)
temizle_dugme.place(x=20, y=500)

app.mainloop()
