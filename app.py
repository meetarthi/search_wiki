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
    words_with_pos = [(word.text, word.pos_) for word in result]
    return words_with_pos

def generate_pastel_color():
    # Generate random RGB components
    r = random.randint(128, 255)
    g = random.randint(128, 255)
    b = random.randint(128, 255)
    # Adjust intensity to achieve pastel effect
    r = (r + 255) // 2
    g = (g + 255) // 2
    b = (b + 255) // 2

    # Format the color code
    color_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return color_code

def random_color_for_pos(words_with_pos):
    pos_colors = {}
    for word, pos in words_with_pos:
        if pos not in pos_colors:
            pos_colors[pos] = generate_pastel_color()
    return pos_colors

def highlight_pos(words_with_pos,pos_colors):
    highlighted_text = ''
    for word, pos in words_with_pos:
        color = pos_colors[pos]
        highlighted_text += '<span style="background-color:{}">{}</span> '.format(color, word)
    display(HTML(highlighted_text))
    st.markdown(highlighted_text, unsafe_allow_html=True)

def main():
    results = search()
    if results:
        pos_colors = random_color_for_pos(POS(results))
        for pos, color in pos_colors.items():
            st.sidebar.markdown('<div style="display:flex; align-items: center;"><div style="background-color:{}; width:20px; height:20px; margin-right:10px; border-radius: 5px;"></div><div>{}</div></div>'.format(color, pos), unsafe_allow_html=True)
        highlight_pos(POS(results),random_color_for_pos(POS(results)))
        print(pos_colors.items())  

if __name__ == '__main__':
    main()
