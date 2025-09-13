import streamlit as st
import numpy as np
from google import genai
import json

st.markdown('# AI Powered Matrix Solver')
st.markdown('*Convert your matrices into RREF with ease*')
client = genai.Client(
    api_key=(st.secrets['GOOGLE_API_KEY'])
)

matrix_input_coff = st.text_area(label= 'Enter Coffecients', placeholder="Enter matrix (rows separated by newline, values by space): 1 2 3\n4 5 6\n7 8 9", )
matrix_X = np.array([list(map(float, row.split())) for row in matrix_input_coff.splitlines()])
matrix_input_y = st.text_area("Enter matrix (rows separated by newline, values by space):", "1 2 3\n4 5 6\n7 8 9")
matrix_Y = np.array([list(map(float, row.split())) for row in matrix_input_y.splitlines()])
if st.button('Generate Matrix'):
    st.write(matrix_X, matrix_Y)
    sys_prompt = {
                    
                    'ROLE': ['You are tutor of Linear Algebra and Geometry',
                             'Your task is to solve the matrix and convert it into Reduced Echilon Form and calculate final values of variables'],
                    'INSTRUCTIONS': [
                        'Show all the calculations step-by-step by writing down whole matrix in each step',
                    ],
                    'VARIABLES': [f'{matrix_X} is the Matrix of coefficient',
                                  f'{matrix_Y} is the Matrix of constants'],
                    'ALGORITHM': [
                        'The leading 1 in first row is at placed at first, second for second row, and so on',
                        'All the digits below the leading 1 always 0',
                        'You can interchange rows',
                        'You can perform any elemantry row operations'
                    ],
                    'OUTPUT': ['The Solved Matrix',
                               'Calculated Values for each variable']
                           
                }
    answer = client.models.generate_content(
        model='gemini-2.5-flash',
        contents= json.dumps(sys_prompt, indent=2)
    ).text

    st.markdown(answer)
