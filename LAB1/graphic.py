import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('maxdegree.csv')

sns.pairplot(x_vars=["index"], y_vars=["dim_CC_maxs"], data=df, hue="key",plot_kws=dict(s=50), markers="+",height=10)

plt.savefig("relazione/figures/figure_maxdegree")

plt.hlines(4856,0,6474,colors='r')
plt.vlines(1295,0,6474,colors='r')

plt.savefig("relazione/figures/figure_maxdegree_line")


df=pd.read_csv('random.csv')


sns.pairplot(x_vars=["index"], y_vars=["dim_CC_maxs"], data=df, hue="key",plot_kws=dict(s=50), markers="+",height=10)

plt.savefig("relazione/figures/figure_random")

plt.hlines(4856,0,6474,colors='r')
plt.vlines(1295,0,6474,colors='r')

plt.savefig("relazione/figures/figure_random_line")
