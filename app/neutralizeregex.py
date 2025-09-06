# src/neutralize.py..
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
