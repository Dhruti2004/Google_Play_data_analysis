# scripts/analysis.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_category_distribution(df, output_path=None):
    """Plots and optionally saves the distribution of app categories."""
    plt.figure(figsize=(12, 6))
    category_counts = df['Category'].value_counts().head(15)  # Top 15 categories
    sns.barplot(x=category_counts.values, y=category_counts.index, palette='viridis')
    plt.title('Top App Categories on Google Play Store')
    plt.xlabel('Number of Apps')
    plt.ylabel('Category')
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
        print(f"Saved: {output_path}")
    plt.show()

def plot_rating_distribution(df, output_path=None):
    """Plots the rating distribution."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Rating'].dropna(), bins=20, kde=True)
    plt.title('App Rating Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
        print(f"Saved: {output_path}")
    plt.show()

def plot_reviews_vs_rating(df, output_path=None):
    """Scatter plot of Reviews vs Rating."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Reviews', y='Rating', alpha=0.5)
    plt.xscale('log')
    plt.title('Reviews vs. Rating')
    plt.xlabel('Number of Reviews (log scale)')
    plt.ylabel('Rating')
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
        print(f"Saved: {output_path}")
    plt.show()
