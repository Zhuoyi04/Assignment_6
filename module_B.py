import matplotlib.plot as plt

def draw_distribution_graph(male_scores, female_scores, subject):
  plt.hist([male_scores, female_scores], bins = 10, label = ['Male', 'Female'], alpha = 0.7, color = ['blue', 'pink'])
  plt.title(f"Score Distribution for {subject}")
  plt.xlabel("Scores")
  plt.ylabel("Frequency")
  plt.legend()
  plt.show()
