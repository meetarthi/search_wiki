import streamlit as st
import wikipedia
import spacy
import random
from IPython.display import display, HTML

def search():
    """
    Summarizes wiki content for the given search term.
    If the search term not valid, returns none
     
    """
    st.title('Wiki Search')
    search_text = st.text_input('Enter search word:')
    try:
        if search_text:
            results = wikipedia.summary(search_text, sentences=4) 
            return results
    except wikipedia.exceptions.DisambiguationError:
        return None

def POS(results):
    """
    Extracts individual word along with the parts of speech,
    by using spacy library
    
    """
    nlp = spacy.load('en_core_web_sm')
    result = nlp(results)
    words_with_pos = [(word.text, word.pos_) for word in result]
    return words_with_pos

def unique_pos(words_with_pos):
    """
    Finding unique parts of speech in the results
    
    """
    pos_list = set()
    for word, pos in words_with_pos:
        pos_list.add(pos)
    unique_pos_list = list(pos_list)
    return unique_pos_list

def generate_pastel_color():

    """
    Generating pastel colors to highlight the pos

    """
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
    """
    Generating Random pastel colors for each pos

    """
    pos_colors = {}
    for word, pos in words_with_pos:
        if pos not in pos_colors:
            pos_colors[pos] = generate_pastel_color()
    return pos_colors

def generate_unique_keys(unique_pos_list):
    """
    Unique keys for multi select options

    """
    keys = [f"box_{value}" for value in unique_pos_list]
    return keys

def Multi_pos_select(unique_pos_list, keys):
    """
    Multi-select option for choosing pos

    """
    options = st.multiselect(
        'What are your favorite colors',
        unique_pos_list,
        key=keys
    )
    return options

def highlight_pos(words_with_pos,pos_colors,multiple_pos_select):

    """
    Displays paragraph with selected pos corresponding words highlighted
    
    """
    highlighted_text = ''
    for word, pos in words_with_pos:
        if pos not in multiple_pos_select:
            highlighted_text += (word + " ") 

        elif pos in multiple_pos_select:
            color = pos_colors[pos]
            highlighted_text += '<span style="background-color:{}">{}</span> '.format(color, word)
    # highlighted_text = '-'.join(highlighted_text)
    display(HTML(highlighted_text))
    st.markdown(highlighted_text, unsafe_allow_html=True)

def main():
    results = search()
    if results:
        pos_colors = random_color_for_pos(POS(results))
        for pos, color in pos_colors.items():
            st.sidebar.markdown('<div style="display:flex; align-items: center;"><div style="background-color:{}; width:20px; height:20px; margin-right:10px; border-radius: 5px;"></div><div>{}</div></div>'.format(color, pos), unsafe_allow_html=True)
        unique_pos_list = unique_pos(POS(results))
        keys = generate_unique_keys(unique_pos_list)
        selected_pos = Multi_pos_select(unique_pos_list, keys)
        st.write(results)
        highlight_pos(POS(results), pos_colors, selected_pos)
        # st.write(results)
        # highlight_pos(POS(results),random_color_for_pos(POS(results)), Multi_pos_select(unique_pos(POS(results)),generate_unique_keys(unique_pos_list)))
        # print(unique_pos(POS(results)))
        # print(keys)


if __name__ == '__main__':
    main()

