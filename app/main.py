import streamlit as st
from neutralizeregex import neutralize_regex
from bias_hf import bias_score_hf

import re

PRONOUN_RULES = [
    (r"\b(he|He)\b", "X"),
    (r"\b(she|She)\b", "X"),
    (r"\b(him|Him)\b", "X"),
    (r"\b(her|Her)\b", "X"),
    (r"\b(his|His)\b", "X"),
    (r"\b(hers|Hers)\b", "X"),
]
GRAMMAR_FIXES = [
    (r"\b[Tt]hey was\b", "X were"),
]
def neutralize_regex(text:str)->str:
    out = text
    for pat, rep in PRONOUN_RULES:
        out = re.sub(pat, rep, out)
    for pat, rep in GRAMMAR_FIXES:
        out = re.sub(pat, rep, out)
    return out


st.set_page_config(page_title="Bias-Aware Neutralizer", layout="centered")
st.title("Bias-Aware Pronoun Neutralizer")

# Input text
txt = st.text_area("Enter your sentence:", "She is a doctor. He is a nurse.")

if st.button("Run Neutralizer"):
    # Neutralize.
    neutralized = neutralize_regex(txt)
    # Bias score (mock for now)
    score = bias_score_hf(txt)

    st.subheader("Results")
    st.write("**Neutralized Text:**")
    st.success(neutralized)

    st.write("**Bias Score (mock):**")
    st.metric(label="Bias Score", value=score)
    st.caption("⚠️ This is a mock bias score. Later, replace with Vertex AI perplexity..")
