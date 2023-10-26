from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import re
import time
import random

st.set_page_config(layout="wide")
first_time = True

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if 'first' not in st.session_state:
    st.session_state.first = True


st.image("logo_1956.png")

st.title("""
Welcome to CanonPDF!
""")

text = st.text_input("Enter PDF URL", value="https://arxiv.org/pdf/2106.13292.pdf")

def click_button():
    st.session_state.clicked = True

button = st.button("Upload!", on_click=click_button)
    

if st.session_state.clicked:
    if st.session_state.first:
        with st.spinner(text="In progress..."):
            time.sleep(random.randint(3, 5))
        st.write("Uploaded!")
        st.session_state.first = False

    st.divider()

    if st.button("Scientific review"):
        with st.spinner(text="In progress..."):
            time.sleep(random.randint(1, 3))
        st.code("""This paper proposes a semi-supervised meta-learning framework with disentanglement for 
                domain-generalized medical image segmentation, achieving state-of-the-art generalization performance 
                by modeling domain shifts and utilizing unlabeled data.

    The problem the paper addresses is the decrease in inference performance on unseen datasets in medical image 
                segmentation due to domain shifts caused by variations in patient populations, scanners, and scan 
                acquisition settings.

    The paper addresses the problem by proposing a semi-supervised meta-learning framework that explicitly 
                disentangles representations related to domain shifts and utilizes unlabeled data for better 
                simulation of domain shifts. This approach improves generalization performance by learning complete 
                and sufficient representations through reconstruction.

    The key experiment involves evaluating the proposed framework on two public benchmarks for medical image 
                segmentation.

    The key findings of the experiment show that the proposed method achieves state-of-the-art generalization 
                performance on the benchmarks, outperforming other approaches.

    The paper concludes that the proposed semi-supervised meta-learning framework with disentanglement effectively 
                addresses the challenge of domain-generalized medical image segmentation and improves generalization 
                performance.

    Future work could focus on exploring additional techniques for disentanglement and further improving the 
                scalability and efficiency of the proposed framework.""", language=None)





    if st.button("Literature review and related work"):
        with st.spinner(text="In progress..."):
            time.sleep(random.randint(1, 3))
        st.code("""This paper addresses the problem of decreased performance in medical image segmentation when 
                faced with domain shifts, proposing a semi-supervised meta-learning framework with disentanglement 
                that utilizes unlabeled data and achieves state-of-the-art generalization performance. 

    The previous methods mentioned in the paper include direct augmentation of source domain data, feature space 
                regularization, alignment of source domain features or output distributions, and learning 
                domain-invariant features with gradient-based meta-learning. These methods have limitations in 
                scalability, efficiency, and accurately approximating true domain shifts in medical image segmentation. 

    Related work to this paper includes research on domain generalization, gradient-based meta-learning methods, 
                disentangled representation learning, unsupervised learning, and domain-invariant feature 
                representation. Techniques such as cross-site MRI harmonization and domain adaptation are also 
                mentioned as related work in handling domain shifts in medical imaging. """, language=None)





    if st.button("Lay summary"):
        with st.spinner(text="In progress..."):
            time.sleep(random.randint(1, 3))
        
        st.code("""This paper is about improving the performance of computer models in analyzing medical images. 
                It introduces a new method that helps the models to better understand and handle differences in 
                images from different sources, like different hospitals or scanners. By using this method, the 
                models can give more accurate results and be more useful in medical diagnosis and treatment. 

    The major problems this paper tries to solve are the decrease in performance of computer models when 
                analyzing medical images from different sources, and the difficulty of creating enough labeled 
                data for training these models. The paper proposes a solution that addresses these problems by
                 modeling the differences between sources and using unlabeled data to improve the models' performance. 

    The key findings of the paper show that the proposed method achieves state-of-the-art generalization 
                performance on benchmark datasets for medical image segmentation. It outperforms existing methods and 
                demonstrates the effectiveness of modeling domain shifts and utilizing unlabeled data. This means that
                 the models can accurately analyze medical images from different sources, even when they haven't been 
                specifically trained on those sources. """, language=None)




    if st.button("Extracting table and figures into LaTex text"):
        with st.spinner(text="In progress..."):
            time.sleep(random.randint(1, 3))
        st.code("""\\begin{table}[h] 
    \centering 
    \caption{Dice (%) results and the standard deviations on M&Ms dataset. For "SDNet+Aug." and our method, the training data contain all the unlabeled data and 2% or 5% of labeled data from source domains. The other models are trained by 2% or 5% labeled data only. Bold numbers denote the best performance.} 
    \label{tab} 
    \\begin{tabular}{cccccc} 
    \hline 
    \\textbf{Source} & \\textbf{Target} & \\textbf{nnUNet} & \\textbf{SDNet+Aug.} & \\textbf{LDDG} & \\textbf{SAML} & \\textbf{Ours} \ \hline 
    2% & 2% & 59.47±±12 & 56.31±±13 & 66.01±±12 & 56.16±±14 & 56.32±±15 \ 
    & 5% & 72.72±±10 & 68.21±±11 & 75.70±±8.7 & 77.54±±10 & 68.56±±10 \ 
    & & 69.94±±9.8 & 75.14±±8.4 & 63.16±±5.4 & 64.57±±8.5 & 72.85±±4.3 \ 
    5% & 2% & 66.22±±6.3 & 67.11±±10 & 72.40±±12 & 69.49±±8.3 & 76.35±±7.9 \ 
    & 5% & 80.30±±9.1 & 73.40±±9.8 & 77.43±±8.3 & 82.51±±6.6 & 75.66±±8.5 \ 
    & & 78.64±±5.8 & 83.77±±5.1 & 71.29±±3.6 & 74.88±±4.6 & 79.75±±4.4 \ \hline 
    \end{tabular} 
    \end{table} """, language=None)
        


    if st.button("Extracting table and figures into Word format content"):
        with st.spinner(text="In progress..."):
            time.sleep(random.randint(1, 3))
        st.code("""Table 1. Dice (%) results and the standard deviations on M&Ms dataset. For "SDNet+Aug." and our method, the training data contain all the unlabeled data and 2% or 5% of labeled data from source domains. The other models are trained by 2% or 5% labeled data only. Bold numbers denote the best performance. 

    Source Target nnUNet SDNet+Aug. LDDG SAML Ours 
    2% 2% 59.47±12 56.31±13 66.01±12 56.16±14 56.32±15 
    5% 72.72±10 68.21±11 75.70±8.7 77.54±10 68.56±10 
    69.94±9.8 75.14±8.4 63.16±5.4 64.57±8.5 72.85±4.3 
    5% 2% 66.22±6.3 67.11±10 72.40±12 69.49±8.3 76.35±7.9 
    5% 80.30±9.1 73.40±9.8 77.43±8.3 82.51±6.6 75.66±8.5 
    78.64±5.8 83.77±5.1 71.29±3.6 74.88±4.6 79.75±4.4 """, language=None)