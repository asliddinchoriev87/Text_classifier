import streamlit as st
import plotly.express as px
import pandas as pd
import pickle  # If your model is saved as a pickle file

import plotly.express as px
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Load our pre-trained model (replace 'text_classify_model.pkl' with your actual model file)
def load_model():
    with open('text_classify_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Sample function to predict category (adapt this based on your model)
def classify_news(news_text, model):
    prediction = model.predict([news_text])  # Ensure your model accepts a list of texts
    return prediction[0]  # Return the predicted category

# Main Streamlit app
def main():
    st.title("News Classification App")
    st.write("Enter the news text below and the AI model will classify it into one of the 5 categories.")

    # Text input for news
    news_text = st.text_area("Enter the news text")

    if st.button("Classify"):
        if news_text.strip() != "":
            # Load the model
            model = load_model()

            # Get prediction
            predicted_category = classify_news(news_text, model)

            # Display the result
            st.success(f"The news is classified under: {predicted_category}")
            
            # Example bar chart for visualization (dummy data)
            category_count = {'Category A': 10, 'Category B': 5, 'Category C': 15, 'Category D': 7, 'Category E': 8}
            df = pd.DataFrame(category_count.items(), columns=['Category', 'Count'])
            fig = px.bar(df, x='Category', y='Count', title='Sample News Category Distribution')
            st.plotly_chart(fig)
        else:
            st.error("Please enter some news text.")

if __name__ == "__main__":
    main()
