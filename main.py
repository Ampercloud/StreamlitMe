# This is a simple Streamlit script.
import streamlit as st
import pandas as pd
import plotly.express as px


def main():
    st.markdown('# Avocado Prices dashboard')

    # # Set the app title
    # st.title('xG Match Result Prediction App')
    # # Add a text box to the app
    # text = st.text(
    #     'Using known xG figures for a match, enter them into the boxes below.\n'
    #     'First prediction is made from an XGBoost Regressor trained on a dataset from\n'
    #     'understat.\n'
    #     'Second prediction uses a ZIF Poisson model with a theta of 0.08 to account\n'
    #     'for the 0-0.'
    # )
    #
    # # Add input fields for home and away xG
    # home_xg = st.number_input('Home xG', min_value=0.0, max_value=6.0, step=0.06, format="%.6f")
    # away_xg = st.number_input('Away xG', min_value=0.0, max_value=6.0, step=0.06, format="%.6f")
    # # Add a button to trigger the prediction
    # if st.button('Predict'):
    #     if home_xg == 0.0 or away_xg == 0.0:
    #         st.error('Please enter an xG value for both teams.')
    #     else:
    #         # Preprocess the input data
    #         input_data = preprocess_data(home_xg, away_xg)
    #         # Make the prediction
    #         prediction = xgb_model.predict(input_data)[0]
    #         # Normalize the prediction
    #         prediction_normalized = prediction / sum(prediction)
    #         st.success("The predicted match outcomes are:\nHome team: {:.4f}\nDraw: {:.4f}\nAway team: {:.4f}".format(
    #             prediction_normalized[0], prediction_normalized[1], prediction_normalized[2]))
    #         st.success("The summed match outcomes are: {:.4f}".format(sum(prediction_normalized)))
    #
    #     # Make the Poisson model prediction
    #     poisson_prediction = zero_inflated_poisson_model(home_xg, away_xg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
