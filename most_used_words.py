import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import urllib.request
import plotly.io as pio

def read_url(url):
    page = urllib.request.urlopen(url)
    plain_html = page.read()
    return plain_html

def data_cleaning(plain_html):
    soup = BeautifulSoup(plain_html, 'html.parser')
    soup_text = soup.get_text(strip=True)
    ready_text = soup_text.lower()
    return ready_text

def gen_tokens(ready_text):
    tokens = []
    for t in ready_text.split():
        tokens.append(t)
    return tokens

def cleanse_tokens(tokens):
    stop_words = stopwords.words('english')
    clean_tokens = tokens[:]
    for token in tokens:
        if token in stop_words:
            clean_tokens.remove(token)
    return clean_tokens

def freq_dict(clean_tokens):
    freq = nltk.FreqDist(clean_tokens)
    high_freq = dict()
    for key, val in freq.items():
        if (val > 10):
            high_freq[key] = val
    return high_freq


def show_fig(high_freq):
    #Note: to pass keys and values of high_freq dictionary, I had to convert them to list when passing them
    fig = dict({
        "data": [{"type": "bar",
                  "x": list(high_freq.keys()),
                  "y": list(high_freq.values())}],
        "layout": {"title": {"text": "Most frequently used words in the page"}, "xaxis": {"categoryorder":"total descending"}}
    })
    pio.show(fig)

def main():
    url = 'https://en.wikipedia.org/wiki/Natural_language_processing'
    plain_html =  read_url(url)
    ready_text = data_cleaning(plain_html)
    tokens = gen_tokens(ready_text)
    clean_tokens = cleanse_tokens(tokens)
    high_freq = freq_dict(clean_tokens)
    show_fig(high_freq)




if __name__ == '__main__':
    main()
