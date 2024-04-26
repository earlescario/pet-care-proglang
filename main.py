from tkinter import *
import cat_display
import dog_display

def main():
    window = Tk()
    window.title("PetWiki")
    icon = PhotoImage(file="images_cat/logo.png")
    window.iconphoto(True, icon)
    window.geometry("800x500")

    def view_animals():
        window.destroy()
        animals()

    def view_about():
        window.destroy()
        about()

    photo = PhotoImage(file="images_cat/logo.png")
    name = Label(window, text="Welcome to WikiPet", font=('Courier New', 30, 'bold'),padx=20, pady=20, image=photo, compound="top")
    name.pack()

    button_animals = Button(window, text="View Animals", command=view_animals, font=('Courier New', 12, 'bold'))
    button_animals.pack(pady=10)

    button_about = Button(window, text="About", command=view_about, font=('Courier New', 12, 'bold'))
    button_about.pack(pady=10)

    button_exit = Button(window, text="Exit", command=window.destroy,font=('Courier New', 12, 'bold'))
    button_exit.pack(pady=10)

    window.mainloop()


def animals():
    window = Tk()
    window.title("PetWiki")
    icon = PhotoImage(file="images_cat/logo.png")
    window.iconphoto(True, icon)
    window.geometry("800x500")

    name = Label(window, text="Choose your Animal" ,font=('Courier New', 30, 'bold'),padx=20, pady=20)
    name.pack()

    def view_cat():
        window.destroy()
        cat_display.cats_display()

    button_cat = Button(window, text="Cats", command=view_cat, font=('Courier New', 30, 'bold'))
    button_cat.place(x=200, y=200)

    def view_dog():
        window.destroy()
        dog_display.dogs_display()
    button_dog = Button(window, text="Dogs", command=view_dog, font=('Courier New', 30, 'bold'))
    button_dog.place(x=450, y=200)

    def back():
        window.destroy()
        main()

    button_back = Button(window, text="Back", command=back, font=('Courier New', 12,'bold'))
    button_back.place(x=380, y=460)

    window.mainloop()


# prints out the contents of the about.txt file
def about():
    window = Tk()
    window.geometry("800x500")
    window.title("PetWiki")
    icon = PhotoImage(file="images_cat/logo.png")
    window.iconphoto(True, icon)

    # reads the txt file
    with open('about.txt', 'r') as file:
        file = file.read()

    # opens the window
    name = Label(window, text="About WikiPet", font=('Courier New', 30, 'bold'),padx=20, pady=20)
    name.pack()
    text = Label(window, text=file, font=('Courier New', 11, 'bold'),padx=20, pady=5,
                        wraplength=600, anchor='w', justify="left")
    text.pack()

    def back():
        window.destroy()
        main()

    button_back = Button(window, text="Back", command=back, font=('Courier New', 12,'bold'))
    button_back.place(x=380, y=460)

    window.mainloop()


if __name__ == "__main__":
    
    main()