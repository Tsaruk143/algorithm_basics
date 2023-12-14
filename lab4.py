import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Зчитуємо датасет з файлу
df = pd.read_csv('DS9.txt', delimiter='\s+', names=['x', 'y'])  # зчитуємо файл враховуючи деліметр для розбиття
df = df[df.index % 1000 == 0] # вибір кожної тисячної точки
# Ділимо датасет на зв'язані області
points = df[['x', 'y']].values
vor = Voronoi(points)

# Знаходимо центри ваги зв'язаних областей
centers = []
for region in vor.regions:
    if -1 not in region and len(region) > 0:
        y = [vor.vertices[i][1] for i in region]
        x = [vor.vertices[i][0] for i in region]
        center = [sum(x) / len(x), sum(y) / len(y)]
        centers.append(center)

# Будуємо діаграму Вороного за множиною центрів ваги
fig, ax = plt.subplots(figsize=(9.6, 5.4))
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='k', line_width=1, line_alpha=0.5)

# Відображаємо центри ваги кругами пдіаметру 5 пкс
for center in centers:
    circle = plt.Circle(center, 5, color='black', alpha=0.1)
    ax.add_artist(circle)

# Відображаємо точки вихідного датасету на побудованому малюнку чорним кольором з насиченістю 10%
ax.scatter(df['x'], df['y'], color='black', alpha=0.1)

# Встановлюємо колір фону для регіонів
ax.set_facecolor((1, 1, 1))

# Виводимо результати у файли будь-якого графічного формату (бажано jpeg)
plt.savefig('result.jpeg')
