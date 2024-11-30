import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

def draw_distribution_graph(scores, male_count, female_count, subject):
  sorted_data = sorted(zip(scores, male_count, female_count), key=lambda x: x[0])
  scores, male_count, female_count = zip(*sorted_data)
  
  x = np.arange(len(scores))
  bar_width = 0.4

  plt.bar(x - bar_width / 2, male_count, bar_width, label='Male', color='blue')
  plt.bar(x + bar_width / 2, female_count, bar_width, label='Female', color='pink')

  plt.xticks(x, scores, rotation = 90, fontsize = 5)

  plt.title(f"Score Distribution for {subject}")
  plt.xlabel("Scores")
  plt.ylabel("Number of Students")
  plt.legend()
  plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
  plt.tight_layout()

  plt.show()
