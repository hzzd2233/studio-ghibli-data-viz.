import matplotlib.pyplot as mpl

date = [1984, 1986, 1988, 1989]
ratings = [89, 96, 93, 98]

x = 80

mpl.plot(date, ratings, marker='o')

mpl.title("Hayao Miyazaki Movie Ratings")

mpl.xlabel("Year")

mpl.ylabel("Ratings (%)")

mpl.xticks([d for d in date])

mpl.yticks([x + (i + 1) * 5 for i in range(len(ratings))])

mpl.text(1984, 88, '89', fontsize=10, rotation=15, 
         bbox=dict(facecolor='gray', alpha=0.1))
mpl.text(1986, 95, '96', fontsize=10, rotation=15, 
         bbox=dict(facecolor='gray', alpha=0.1))
mpl.text(1988, 92, '93', fontsize=10, rotation=15, 
         bbox=dict(facecolor='gray', alpha=0.1))
mpl.text(1989, 98.5, '98', fontsize=10, rotation=15, 
         bbox=dict(facecolor='gray', alpha=0.1))


mpl.text(1984, 90, 'Nausicaa of the Valley of the Wind',
          fontsize=10, rotation=75,)

mpl.text(1986, 96.5, 'Castle in the Sky', fontsize=10, 
         rotation=50)

mpl.text(1987.9, 93.5, 'My Neighbor Totoro', fontsize=10, rotation=70)

mpl.text(1989, 93.7, "Kiki's Delivery Service", fontsize=10, rotation=275)

mpl.show()

 