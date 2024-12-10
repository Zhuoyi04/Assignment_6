import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

def draw_distribution_graph(scores, male_count, female_count, subject):
    sorted_data = sorted(zip(scores, male_count, female_count), key=lambda x: x[0])
    scores, male_count, female_count = zip(*sorted_data)
    
    x = np.arange(len(scores))
    
    plt.plot(x, male_count, label='Male', color='blue', marker='o', linestyle='-')
    plt.plot(x, female_count, label='Female', color='pink', marker='o', linestyle='-')

    plt.xticks(x, scores, rotation=90, fontsize=5)

    plt.title(f"Score Distribution for {subject}")
    plt.xlabel("Scores")
    plt.ylabel("Number of Students")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()
