import streamlit as st
import pandas as pd

st.title("Language Translator")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("words.csv")
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return pd.DataFrame()

df = load_data()

# تأكد أن البيانات موجودة
if not df.empty:

    df['English'] = df['English'].astype(str).str.strip().str.lower()
    df['Arabic'] = df['Arabic'].astype(str).str.strip()

    option = st.radio(
        "Choose translation direction:",
        ("English → Arabic", "Arabic → English")
    )

    user_input = st.text_input("Enter a word:")

    if st.button("Translate"):

        if user_input.strip() == "":
            st.warning("Please enter a word")
        else:

            clean_input = user_input.strip().lower()

            if option == "English → Arabic":
                result = df[df['English'] == clean_input]

                if not result.empty:
                    st.success(result['Arabic'].values[0])
                else:
                    st.error("Word not found")

            else:
                clean_input = user_input.strip()
                result = df[df['Arabic'] == clean_input]

                if not result.empty:
                    st.success(result['English'].values[0])
                else:
                    st.error("Word not found")

else:
    st.error("Data not loaded. Check words.csv file.")

if st.button(" Refresh Data"):
    st.cache_data.clear()
    st.rerun()
