from tkinter import *
import main
import cat_func

def cats_display():

    window = Tk()
    window.title("PetWiki")
    icon = PhotoImage(file="images_cat/logo.png")
    window.iconphoto(True, icon)
    window.geometry("930x520")

    def maincoom():
        window.destroy()
        cat_func.cat_funcs(1)
    
    def ragdolls():
        window.destroy()
        cat_func.cat_funcs(2)

    def persians():
        window.destroy()
        cat_func.cat_funcs(3)

    def americans():
        window.destroy()
        cat_func.cat_funcs(4)

    def sphynxs():
        window.destroy()
        cat_func.cat_funcs(5)

    def exotics():
        window.destroy()
        cat_func.cat_funcs(6)
    
    def aby():
        window.destroy()
        cat_func.cat_funcs(7)

    def scottishes():
        window.destroy()
        cat_func.cat_funcs(8)

    def bengals():
        window.destroy()
        cat_func.cat_funcs(9)

    def britishes():
        window.destroy()
        cat_func.cat_funcs(10)
    
    maincoon_photo = PhotoImage(file='icon/1.png')
    main_coon = Button(window, text="Main\nCoon", command=maincoom,font=('Courier New', 12, 'bold'), image=maincoon_photo, compound="top")
    main_coon.place(x=20,y=20)

    ragdoll_photo = PhotoImage(file='icon/2.png')
    ragdoll = Button(window, text="Ragdoll\nCat", command=ragdolls ,font=('Courier New', 12, 'bold'), image=ragdoll_photo, compound="top")
    ragdoll.place(x=200,y=20)

    persian_photo = PhotoImage(file='icon/3.png')
    persian = Button(window, text="Persian\nCat", command=persians ,font=('Courier New', 12, 'bold'), image=persian_photo, compound="top")
    persian.place(x=380,y=20)
    
    american_photo = PhotoImage(file='icon/4.png')
    american = Button(window, text="American\nShorthair", command=americans ,font=('Courier New', 12, 'bold'), image=american_photo, compound="top")
    american.place(x=560,y=20)

    Sphynx_photo = PhotoImage(file='icon/5.png')
    Sphynx = Button(window, text="Sphynx\nCat", command=sphynxs ,font=('Courier New', 12, 'bold'), image=Sphynx_photo, compound="top")
    Sphynx.place(x=740,y=20)

    Exotic_photo = PhotoImage(file='icon/6.png')
    Exotic = Button(window, text="Exotic\nShorthair", command=exotics ,font=('Courier New', 12, 'bold'), image=Exotic_photo, compound="top")
    Exotic.place(x=20,y=250)

    Abyssinian_photo = PhotoImage(file='icon/7.png')
    Abyssinian = Button(window, text="Abyssinian\nCat", command=aby ,font=('Courier New', 12, 'bold'), image=Abyssinian_photo, compound="top")
    Abyssinian.place(x=200,y=250)


    Scottish_photo = PhotoImage(file='icon/8.png')
    Scottish = Button(window, text="Scottish\nFold", command=scottishes ,font=('Courier New', 12, 'bold'), image=Scottish_photo, compound="top")
    Scottish.place(x=380,y=250)

    Bengal_photo = PhotoImage(file='icon/9.png')
    Bengal = Button(window, text="Bengal\nCat", command=bengals ,font=('Courier New', 12, 'bold'), image=Bengal_photo, compound="top")
    Bengal.place(x=560,y=250)

    British_photo = PhotoImage(file='icon/10.png')
    British = Button(window, text="British\nShorthair", command=britishes ,font=('Courier New', 12, 'bold'), image=British_photo, compound="top")
    British.place(x=740,y=250)

    def back():
        window.destroy()
        main.animals()

    button_back = Button(window, text="Back", command=back, font=('Courier New', 12,'bold'))
    button_back.place(x=450, y=470)

    window.mainloop()
