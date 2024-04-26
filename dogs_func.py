import dog_display
import dogs
from tkinter import *


# display the details of a dog
def dog_func(dog_no):
    # initialization of the window
    window = Tk()
    window.geometry("800x500")
    window.title("PetWiki")
    icon = PhotoImage(file="images_cat/logo.png")
    window.iconphoto(True, icon)

    # displays the name of the chosen breed
    name = Label(window, text=dogs.dog[dog_no - 1][0], font=('Courier New', 30, 'bold'), padx=20, pady=20)
    name.place(x=10, y=20)

    # displays the description of the chosen dog breed
    description_title = Label(window, text="Description:", font=('Courier New', 13, "bold"), padx=20,
                              wraplength=400, anchor="w", justify="left")
    description_title.place(x=10, y=90)
    description = Label(window, text=dogs.dog[dog_no - 1][1], font=('Courier New', 11), padx=20, pady=5,
                        wraplength=400, anchor="w", justify="left")
    description.place(x=10, y=110)

    # displays the image of the chosen dog breed
    photo_index = PhotoImage(file=f"images_dog/{dog_no}.png")
    photo = Label(window, image=photo_index, padx=20, pady=20)
    photo.place(x=470, y=30)

    # displays the pros of the chosen dog breed
    pros_title = Label(window, text="Pros:", font=('Courier New', 13, "bold"), padx=20,
                       wraplength=400, anchor="w", justify="left")
    pros_title.place(x=10, y=280)
    pros = Label(window, text=dogs.dog[dog_no - 1][2], font=('Courier New', 11), padx=20, pady=5,
                 wraplength=400, anchor="w", justify="left")
    pros.place(x=10, y=300)

    # displays the cons of the chosen dog breed
    cons_title = Label(window, text="Cons:", font=('Courier New', 13, "bold"), padx=20,
                       wraplength=400, anchor="w", justify="left")
    cons_title.place(x=10, y=370)
    cons = Label(window, text=dogs.dog[dog_no - 1][3], font=('Courier New', 11), padx=20, pady=5,
                 wraplength=400, anchor="w", justify="left")
    cons.place(x=10, y=390)

    # displays the maintenance level of the chosen dog breed
    maintenance_title = Label(window, text="Maintenance:", font=('Courier New', 13, "bold"), padx=20,
                              wraplength=400, anchor="w", justify="left")
    maintenance_title.place(x=470, y=370)
    maintenance = Label(window, text=dogs.dog[dog_no - 1][4], font=('Courier New', 11), padx=20, pady=5,
                        wraplength=400, anchor="w", justify="left")
    maintenance.place(x=470, y=390)

    def back():
        window.destroy()
        dog_display.dogs_display()

    button_back = Button(window, text="Back", command=back, font=('Courier New', 12,'bold'))
    button_back.place(x=380, y=460)

    window.mainloop()

