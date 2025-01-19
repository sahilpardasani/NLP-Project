import streamlit as st
st.set_page_config(page_title="NLP Web App", page_icon="💡",layout="centered",initial_sidebar_state="auto")
from textblob import TextBlob
import spacy
import neattext as nt
import matplotlib.pyplot as plt
import matplotlib
from Summarise import summarize_text
matplotlib.use("Agg")
from wordcloud import WordCloud
from deep_translator import GoogleTranslator

def main():
    """NLP web app with streamlit"""

    title_template = """
    <div style="background-color:blue; padding:5px;">
    <h1 style="color: cyan;">NLP Web App</h1>
    </div>
    """
    st.markdown(title_template, unsafe_allow_html=True)

    subtitle_template = """
    <div style="background-color:cyan; padding:8px;">
    <h2 style="color: blue;">Powered by Streamlit</h2>
    </div>
    """
    st.markdown(subtitle_template, unsafe_allow_html=True)

    st.sidebar.image("Blog-What-is-NLP.jpg",use_container_width=True)
    # Menu options
    activity = ["Text Analysis", "Translation", "Sentiment Analysis", "About"]
    choice = st.sidebar.selectbox("Menu", activity)

    # Handling the user choice
    if choice == "Text Analysis":
        st.subheader("Text Analysis")
        st.write("")
        raw_text=st.text_area("Write something","Enter a text in English...",height=300)

        if st.button("Analyse"):
            if not raw_text:  # This is the corrected condition
                st.warning("Enter a text...")
            else:
                blob = TextBlob(raw_text)
                st.info("Basic Function")

            col1, col2 = st.columns(2)

            with col1:
                with st.expander("Basic Info"):
                    st.write("Text Stats")
                    word_desc= nt.TextFrame(raw_text).word_stats()
                    result_desc= {"Length of Text": word_desc['Length of Text'],
                                  "Num of Vowels": word_desc['Num of Vowels'],
                                  "Num of Consonants":word_desc['Num of Consonants'],
                                  "Num of stopwords":word_desc['Num of Stopwords']}
                    st.write(result_desc)

                with st.expander("Stopwords"):
                    st.success("Stop Words List")
                    stop_w = nt.TextExtractor(raw_text).extract_shortwords()
                    st.error(stop_w)
            
            with col2:
                with st.expander("Processed Text"):
                    st.success ("Stopwords excluded Text")
                    processed_text=str(nt.TextFrame(raw_text).remove_stopwords())
                    st.write(processed_text)

                with st.expander("Plot wordcloud"):
                    st.success("Wordcloud")
                    wordcloud= WordCloud().generate(processed_text)
                    fig = plt.figure(1, figsize=(20,10))
                    plt.imshow(wordcloud, interpolation='bilinear')
                    plt.axis("off")
                    st.pyplot(fig)

            st.write("")
            st.write("")
            st.info("Advanced Features")

            col3, col4 = st.columns(2)

            with col3:
                with st.expander("Token&Lemmas"):
                    st.write("T&K")
            
            with col4:
                with st.expander("Summarise"):
                    st.success("summarise")
                    


    if choice == "Translation":
        st.subheader("Translation")
        st.write("")
        raw_text= st.text_area("Original text", "Write something to be translated...",height=200)
        if len(raw_text)<3:
            st.warning("Please provide a text with at least 3 characters.")
        else:
            target_lang=st.selectbox("Target Language",["German","Spanish","French","Italian","Hindi"])
            if target_lang == "German":
                target_lang ='de'
            elif target_lang == "Spanish":
                target_lang = 'es'
            elif target_lang == "French":
                target_lang = "fr"
            elif target_lang == "Italian":
                target_lang = "it"
            else:
                target_lang ='hi'

        if st.button("Translate"):
            translator= GoogleTranslator(source='auto', target=target_lang)
            translated_text = translator.translate(raw_text)
            st.write(translated_text)
    

    if choice == "Sentiment Analysis":
        st.subheader("Sentiment Analysis")
        st.write("")
        st.write("High polarity indicates positive sentiment. Low polarity indicates negative sentiment.")
        raw_text= st.text_area("Original text", "Enter a text here to be analysed...",height=200)
        if st.button("Evaluate"):
            if len(raw_text) == 0:
                st.warning("Enter a text...")
            else:
                blob= TextBlob(raw_text)
                st.info("Sentiment Analysis")
                st.write(blob.sentiment)
                st.write("")

    if choice == "About":
        st.subheader("About")
        st.write("")
        st.markdown("""
        # NLP Web App Made with Streamlit

        For more info:

        - [Streamlit](https://streamlit.io)
        """)

# Ensure the app only runs when executed directly
if __name__ == "__main__":
    main()
