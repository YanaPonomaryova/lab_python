import matplotlib.pyplot as plt

labels = ['Zhivchiki', 'SumDu', 'Smilivtsi', 'Bozhevilni Genii' , 'Prosto Tut za Groshi', 'Monstri', 'Ofisni Geroi', 'Komanda A' , 'Ruinivnyky', 'Vyshchenky']
x = [60, 45, 55, 50, 70, 30, 65, 40, 75, 80]

plt.pie(x, labels=labels, shadow=True)

plt.show()