import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re
import matplotlib
from collections import Counter

matplotlib.rcParams['font.family'] = 'Arial'


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = ' '.join(text.split())
    return text


def count_words(text):
    processed_text = preprocess_text(text)
    words = processed_text.split()
    stopwords = set(STOPWORDS)
    filtered_words = [word for word in words if word not in stopwords]
    word_counts = Counter(filtered_words)
    return word_counts


def display_word_counts(word_counts, top_n=10):
    print("\n=== Word Counts ===")
    print(f"{'Word':<20} {'Count':<10}")
    print("-" * 30)

    for word, count in word_counts.most_common(top_n):
        print(f"{word:<20} {count:<10}")

    print(f"\nTotal unique words: {len(word_counts)}")
    print(f"Total words (excluding common words): {sum(word_counts.values())}")


def create_word_cloud(
    input_text,
    cloud_width=1200,
    cloud_height=800,
    bg_color='white',
    font_path=None,
    mask_path=None,
    contour_width=0,
    contour_color='black'
):
    processed_text = preprocess_text(input_text)

    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        colors = [
            '#1f77b4', '#ff7f0e', '#2ca02c',
            '#d62728', '#9467bd', '#8c564b', '#e377c2'
        ]
        return np.random.choice(colors)

    cloud_config = {
        'width': cloud_width,
        'height': cloud_height,
        'background_color': bg_color,
        'max_words': 200,
        'stopwords': STOPWORDS,
        'min_font_size': 10,
        'max_font_size': 150,
        'relative_scaling': 0.5,
        'collocations': False,
        'color_func': color_func,
        'prefer_horizontal': 0.9,
        'font_path': font_path,
        'mask': None,
        'contour_width': contour_width,
        'contour_color': contour_color,
        'scale': 3
    }

    wordcloud = WordCloud(**cloud_config).generate(processed_text)

    return wordcloud


def display_word_cloud(word_cloud, figure_width=15, figure_height=10):
    plt.figure(figsize=(figure_width, figure_height), dpi=300)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()


def main():
    print("=== Word Cloud Generator ===\n")
    try:
        with open('data.txt', 'r', encoding='utf-8') as file:
            text_to_process = file.read().strip()

    except FileNotFoundError:
        print("Error: 'data.txt' not found in this folder.")
        return

    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if not text_to_process:
        print("'data.txt' is empty.")
        return

    print("Counting words...")
    word_counts = count_words(text_to_process)

    display_word_counts(word_counts, top_n=10)

    print("\nCreating word cloud...")

    my_wordcloud = create_word_cloud(
        text_to_process,
        font_path=None,
        mask_path=None,
        bg_color='white'
    )

    print("Displaying word cloud...")

    display_word_cloud(my_wordcloud)

    print("\nDone!")


if __name__ == "__main__":
    main()