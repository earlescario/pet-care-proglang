from tkinter import *
import main
import dogs_func

def dogs_display():

    window = Tk()
    window.title("PetWiki")
    icon = PhotoImage(file="images_cat/logo.png")
    window.iconphoto(True, icon)
    window.geometry("930x520")

    def dog1():
        window.destroy()
        dogs_func.dog_func(1)
    
    def dog2():
        window.destroy()
        dogs_func.dog_func(2)

    def dog3():
        window.destroy()
        dogs_func.dog_func(3)

    def dog4():
        window.destroy()
        dogs_func.dog_func(4)

    def dog5():
        window.destroy()
        dogs_func.dog_func(5)

    def dog6():
        window.destroy()
        dogs_func.dog_func(6)
    
    def dog7():
        window.destroy()
        dogs_func.dog_func(7)

    def dog8():
        window.destroy()
        dogs_func.dog_func(8)

    def dog9():
        window.destroy()
        dogs_func.dog_func(9)

    def dog10():
        window.destroy()
        dogs_func.dog_func(10)
    
    dog_photo1 = PhotoImage(file='icon/11.png')
    dogw1 = Button(window, text="Labrador\nRetriever", command=dog1,font=('Courier New', 12, 'bold'), image=dog_photo1, compound="top")
    dogw1.place(x=20,y=20)

    dog_photo2 = PhotoImage(file='icon/12.png')
    dogw2 = Button(window, text="German\nShepherd", command=dog2 ,font=('Courier New', 12, 'bold'), image=dog_photo2, compound="top")
    dogw2.place(x=200,y=20)

    dog_photo3 = PhotoImage(file='icon/13.png')
    dogw3 = Button(window, text="Golden\nRetriever", command=dog3 ,font=('Courier New', 12, 'bold'), image=dog_photo3, compound="top")
    dogw3.place(x=380,y=20)
    
    dog_photo4 = PhotoImage(file='icon/14.png')
    dogw4 = Button(window, text="English\nBulldog", command=dog4 ,font=('Courier New', 12, 'bold'), image=dog_photo4, compound="top")
    dogw4.place(x=560,y=20)

    dog_photo5 = PhotoImage(file='icon/15.png')
    dogw5 = Button(window, text="French\nBulldog", command=dog5 ,font=('Courier New', 12, 'bold'), image=dog_photo5, compound="top")
    dogw5.place(x=740,y=20)

    dog_photo6 = PhotoImage(file='icon/16.png')
    dogw6 = Button(window, text="Toy\nPoodle", command=dog6 ,font=('Courier New', 12, 'bold'), image=dog_photo6, compound="top")
    dogw6.place(x=20,y=250)

    dog_photo7 = PhotoImage(file='icon/17.png')
    dogw7 = Button(window, text="Beagle\nDog", command=dog7 ,font=('Courier New', 12, 'bold'), image=dog_photo7, compound="top")
    dogw7.place(x=200,y=250)


    dog_photo8 = PhotoImage(file='icon/18.png')
    dogw8 = Button(window, text="Rottweiler\nDog", command=dog8 ,font=('Courier New', 12, 'bold'), image=dog_photo8, compound="top")
    dogw8.place(x=380,y=250)

    dog_photo9 = PhotoImage(file='icon/19.png')
    dogw9 = Button(window, text="Dachshund\nDog", command=dog9 ,font=('Courier New', 12, 'bold'), image=dog_photo9, compound="top")
    dogw9.place(x=560,y=250)

    dog_photo10 = PhotoImage(file='icon/20.png')
    dogw10 = Button(window, text="Yorkshire\nTerrier", command=dog10 ,font=('Courier New', 12, 'bold'), image=dog_photo10, compound="top")
    dogw10.place(x=740,y=250)

    def back():
        window.destroy()
        main.animals()

    button_back = Button(window, text="Back", command=back, font=('Courier New', 12,'bold'))
    button_back.place(x=450, y=470)

    window.mainloop()