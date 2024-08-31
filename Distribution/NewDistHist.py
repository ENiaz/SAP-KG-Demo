


import pandas as pd
import matplotlib.pyplot as plt

def plot_distribution(df, output_name, plot_color):
    rdf2vec_df = df[df['Methods'] == 'RDF2Vec']
    counts = rdf2vec_df['values'].value_counts().sort_index()

    plt.bar(counts.index, counts.values, color=plot_color)
    plt.ylabel('Number of properties', fontsize=16)
    plt.xlabel('Number of relationships among properties', fontsize=16)
    # plt.title(f'Distribution of {output_name}')
    plt.savefig(f'Wikidata-{output_name}.pdf', dpi=100)  # Save plot with unique filename
    plt.show()
    plt.clf()

# List of CSV files, output names, and colors
files = [
    {'filename': 'PersonDistributionSynonym.csv', 'output_name': 'Person', 'color': 'mediumorchid'},
    {'filename': 'MusicDistributionSynonym.csv', 'output_name': 'Music', 'color': 'palevioletred'},
    {'filename': 'HistoryDistributionSynonym.csv', 'output_name': 'History', 'color': 'lightskyblue'},
    {'filename': 'FilmDistributionSynonym.csv', 'output_name': 'Film', 'color': 'purple'},
    {'filename': 'SportDistributionSynonym.csv', 'output_name': 'Sport', 'color': 'turquoise'},
    {'filename': 'DrugDistributionSynonym.csv', 'output_name': 'Drug', 'color': 'khaki'}
]

# Loop through files, plot, and save
for file_info in files:
    df = pd.read_csv(file_info['filename'], header=None, names=['Methods', 'values', 'predicate'])
    plot_distribution(df, file_info['output_name'], file_info['color'])
