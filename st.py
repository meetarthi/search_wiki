import streamlit as st
import wikipedia
import spacy
import random
from IPython.display import display, HTML

def search():
    st.title('Wiki Search')
    search_text = st.text_input('Enter search word:')
    try:
        if search_text:
            results = wikipedia.summary(search_text, sentences=4) 
            return results
    except wikipedia.exceptions.DisambiguationError:
        return None

def POS(results):
    nlp = spacy.load('en_core_web_sm')
    result = nlp(results)
    words_with_pos = [(word.text, word.pos_) for word in nlp(result)]
    return words_with_pos

def random_color_for_pos(words_with_pos):
    pos_colors = {}
    for word, pos in words_with_pos:
            if pos not in pos_colors:
                pos_colors[pos] = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return pos_colors

def highlight_pos(words_with_pos,pos_colors):
    highlighted_text = ''
    for word, pos in words_with_pos:
        color = pos_colors[pos]
        highlighted_text += '<span style="background-color:{}">{} {}</span> '.format(color, word, pos)
    display(HTML(highlighted_text))
    st.markdown(highlighted_text, unsafe_allow_html=True)

def main():
       results = search()
       if results:
        highlight_pos(POS(results),random_color_for_pos(POS(results)))

if __name__ == '__main__':
    main()


