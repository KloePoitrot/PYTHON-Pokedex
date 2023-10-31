import tkinter as tk
from PIL import Image, ImageTk
# import pickle

pokedex = tk.Tk()
pokedex.geometry("1095x540")
pokedex.resizable(0, 0)
pokedex.title("Pokedex")
pokedex.configure(bg="#bf1520", borderwidth=10, relief="groove")

#
# Pokedex class
# 
#
class Pokemon():
    def __init__(self, name, type1, type2, category, movepool, evo, entry, img):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.category = category
        self.movepool = movepool
        self.evo = evo
        self.entry = entry
        self.img = img

# list
impidimp = Pokemon("Impidimp", "Dark", "Fairy", "The Wily pokemon", "Dark Pulse, Fake Out, Bite, Flatter, Fake Tears", "Morgrem", "Through its nose, it sucks in the emanations produced by people and Pokémon when they feel annoyed. It thrives off this negative energy.", "./images/Grimalin-EB.png")
morgrem = Pokemon("Morgrem", "Dark", "Fairy", "The Devious pokemon", "Fake Out, False Surrender, Sucker Punch, Foul Play", "Grimmsnarl", "When it gets down on all fours as if to beg for forgiveness, it's trying to lure opponents in so that it can stab them with its spear-like hair.", "./images/Fourbelin-EB.png")
grimmsnarl = Pokemon("Grimmsnarl", "Dark", "Fairy", "The Bulk Up pokemon", "False Surrender, Sucker Punch, Foul Play, Hammer Arm, Spirit Break", "Final stage", "With the hair wrapped around its body helping to enhance its muscles, this Pokémon can overwhelm even Machamp.", "./images/Angoliath-EB.png")
budew = Pokemon("Budew", "Grass", "Poison", "The Bud pokemon", "Absorb, Growth, Stun Spore, Worry Seed", "Roselia", "Over the winter, it closes its bud and endures the cold. In spring, the bud opens and releases pollen. When it feels the sun's warm touch, it opens its bud to release pollen. It lives alongside clear pools.", "./images/364px-Rozbouton-DP.png")
roselia = Pokemon("Roselia", "Grass", "Poison", "The Thorn pokemon", "Poison Sting, Absorb, Mega Drain, Mgical Leaf, Toxic Spikes", "Roserade", "A Roselia that drinks nutritionally rich springwater blooms with lovely flowers. The fragrance of its flowers has the effect of making its foes careless.", "./images/Roselia-RS.png")
roserade = Pokemon("Roserade", "Grass", "Poison", "The Bouquet pokemon", "Grassy Terrain, Poison Sting, Venom Drench, Giga Drain, Synthesis", "Final stage", "Hidden within the bouquet on each hand are thorned whips loaded with virulent poison. Roserade moves gracefully as it corners its prey and mercilessly lashes them with its whips.", "./images/Roserade-DP.png")

listpokemon = [impidimp, morgrem, grimmsnarl, budew, roselia, roserade]




#
# Submit button fuction
# 
#
def submit():
    newpoke = Pokemon(addname.get(), addtype1.get(), addtype2.get(), addcategory.get(), addmove.get(), addevo.get(), addentry.get("1.0",tk.END), addimg.get())
    newpokename = addname.get()

    pokedexentry.insert(tk.END, newpokename)
    listpokemon.append(newpoke)

    addname.delete(0, tk.END)
    addtype1.delete(0, tk.END)
    addtype2.delete(0, tk.END)
    addcategory.delete(0, tk.END)
    addmove.delete(0, tk.END)
    addevo.delete(0, tk.END)
    addentry.delete(1.0, tk.END)
    addimg.delete(0, tk.END)






#
# display entry
# 
#
def display():
    pd = int(pokedexentry.curselection()[0])
    
    pokename.config(text=listpokemon[pd].name)
    poketype.config(text=listpokemon[pd].type1 + "/" + listpokemon[pd].type2)
    pokecateory.config(text=listpokemon[pd].category)
    pokemove.config(text=listpokemon[pd].movepool)
    pokeevo.config(text=listpokemon[pd].evo)
    pokeentry.config(text=listpokemon[pd].entry)
    pokeimg.config(file=listpokemon[pd].img)





#
# Visual
# ---- box placement
#

# List
pokedexentrytitle = tk.Label(pokedex, text="Pokedex", font="arial, 12", bg="#870918", fg="#fff")
pokedexentrytitle.place(x=20, y=20)

pokedexentry = tk.Listbox(pokedex, width=20, height=23)
pokedexentry.place(x=20, y=45)

pokedexentry.insert(0, "Impidimp")
pokedexentry.insert(1, "Morgrem")
pokedexentry.insert(2, "Grimmsnarl")
pokedexentry.insert(3, "Budew")
pokedexentry.insert(4, "Roselia")
pokedexentry.insert(5, "Roserade")

check = tk.Button(pokedex, text="Select", command=display)
check.place(x=102, y=20)








# Box informations
pokedexinfo = tk.Frame(pokedex, bg="#fff", width=330, height=450)
pokedexinfowidth = 330
pokedexinfo.place(x=160, y=45)

pokedexinfotitle = tk.Label(pokedex, text="Informations", font="arial, 12", bg="#870918", fg="#fff")
pokedexinfotitle.place(x=170, y=20)



# Box information content
pokename = tk.Label(pokedexinfo, text="Name", font="arial, 30", bg="#fff")
pokename.place(x=10, y=10)


poketype = tk.Label(pokedexinfo, text="Type 1/Type 2", font="arial, 15", bg="#fff")
poketype.place(x=10, y=55)


pokecateory = tk.Label(pokedexinfo, text="The ?? pokemon", font="arial, 10", bg="#fff")
pokecateory.place(x=10, y=83)


pokemovetitle = tk.Label(pokedexinfo, text="Movepool", font="arial, 15", bg="#fff")
pokemovetitle.place(x=10, y=140)
pokemove = tk.Label(pokedexinfo, font="arial, 10", wraplength=pokedexinfowidth - 20, bg="#fff")
pokemove.place(x=10, y=167)


pokeevotitle = tk.Label(pokedexinfo, text="Evolution", font="arial, 15", bg="#fff")
pokeevotitle.place(x=10, y=230)
pokeevo = tk.Label(pokedexinfo, font="arial, 10", wraplength=pokedexinfowidth - 20, bg="#fff")
pokeevo.place(x=10, y=257)


pokeentrytitle = tk.Label(pokedexinfo, text="Pokedex Entry", font="arial, 15", bg="#fff")
pokeentrytitle.place(x=10, y=310)
pokeentry = tk.Label(pokedexinfo, font="arial, 10", wraplength=pokedexinfowidth - 20, bg="#fff")
pokeentry.place(x=10, y=337)






# Illustration
pokeimg = tk.PhotoImage(file="./images/unknown.png")
pokeimgdisplay = tk.Canvas(pokedex, bg="#870918", width=370, height=475)
pokeimglab = tk.Label(pokeimgdisplay, image=pokeimg, bg="#870918", height=475, width=370)
pokeimglab.place(x=0, y=0)
pokeimgdisplay.place(x=505, y=20)





# Form
addnametitle = tk.Label(pokedex, text="Add Name", font="arial, 11", bg="#870918", fg="#fff")
addnametitle.place(x=890,y=20)
addname = tk.Entry(pokedex, width=27)
addname.place(x=890,y=42)

addtypetitle = tk.Label(pokedex, text="Add Type", font="arial, 11", bg="#870918", fg="#fff")
addtypetitle.place(x=890, y=65)
addtype1 = tk.Entry(pokedex, width=27)
addtype1.place(x=890,y=88)
addtype2 = tk.Entry(pokedex, width=27)
addtype2.place(x=890,y=108)

addcategorytitle = tk.Label(pokedex, text="Add Category", font="arial, 11", bg="#870918", fg="#fff")
addcategorytitle.place(x=890,y=132)
addcategory = tk.Entry(pokedex, width=27)
addcategory.place(x=890,y=154)

addmovetitle = tk.Label(pokedex, text="Add Movepool", font="arial, 11", bg="#870918", fg="#fff")
addmovetitle.place(x=890,y=177)
addmove = tk.Entry(pokedex, width=27)
addmove.place(x=890,y=198)

addevotitle = tk.Label(pokedex, text="Add Evolution", font="arial, 11", bg="#870918", fg="#fff")
addevotitle.place(x=890,y=222)
addevo = tk.Entry(pokedex, width=27)
addevo.place(x=890,y=244)

addentrytitle = tk.Label(pokedex, text="Add Pokedex Entry", font="arial, 11", bg="#870918", fg="#fff")
addentrytitle.place(x=890,y=268)
addentry = tk.Text(pokedex, width=23, height=6, font="arial, 10")
addentry.place(x=890,y=290)

addimgtitle = tk.Label(pokedex, text="Add Image", font="arial, 11", bg="#870918", fg="#fff")
addimgtitle.place(x=890,y=395)
addimg = tk.Entry(pokedex, width=27)
addimg.place(x=890,y=415)

submitbg = tk.PhotoImage(file="./images/45634.png", width=160, height=45)
submitentry = tk.Button(pokedex, image=submitbg, command=submit)
submitentry.place(x=890, y=450)

#
# 
# Mainloop
#
#
pokedex.mainloop()