import matplotlib.pyplot as mpl

date = [1984, 1986, 1988, 1989]
ratings = [89, 96, 93, 98]

mpl.figure(figsize=(8, 6))

bar = mpl.bar(date, ratings)
mpl.bar_label(bar, labels=[r for r in ratings], 
              label_type='center',
              rotation=10, fontsize=10, padding=3)

mpl.bar_label(bar, labels=['Nausicaa of the Valley of the Wind',
                           'Castle in the Sky',
                           'My Neighbor Totoro',
                           "Kiki's Delivery Service"], 
              rotation=70, fontsize=10, padding=3)


mpl.title("Hayao Miyazaki Movie Ratings", pad=75)
mpl.xlabel("Year")
mpl.ylabel("Ratings (%)")
mpl.show()