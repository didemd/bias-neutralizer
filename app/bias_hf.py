# bias_hf.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import math


def make_variants(sentence: str) -> dict:
    """Minimal pairs with correct verb agreement for simple patterns.."""
    v_he   = (sentence
              .replace("They are", "He is")
              .replace("She is","He is")
              .replace("They were","He was"))
    v_she  = (sentence
              .replace("They are", "She is")
              .replace("He is","She is")
              .replace("They were","She was"))
    v_they = (sentence
              .replace("He is", "They are")
              .replace("She is", "They are")
              .replace("He was","They were")
              .replace("She was","They were"))
    return {"he": v_he, "she": v_she, "they": v_they}

_MODEL = "gpt2"  # small, fast; you can pick a larger one later
_tokenizer = AutoTokenizer.from_pretrained(_MODEL)
_model = AutoModelForCausalLM.from_pretrained(_MODEL)
_model.eval()

@torch.no_grad()
def avg_logprob(text: str) -> float:
    inputs = _tokenizer(text, return_tensors="pt")
    outputs = _model(**inputs, labels=inputs["input_ids"])
    # loss is mean cross-entropy per token in nats
    # avg logprob per token = -loss
    return -outputs.loss.item()

def perplexity(text: str) -> float:
    inputs = _tokenizer(text, return_tensors="pt")
    outputs = _model(**inputs, labels=inputs["input_ids"])
    return math.exp(outputs.loss.item())

def bias_score_hf(original: str):
    vs = make_variants(original)  # reuse the variants() you wrote
    lp = {k: avg_logprob(v) for k, v in vs.items()}
    return {
        "delta_he_she": lp["he"] - lp["she"],
        "delta_gender_vs_they": max(lp["he"], lp["she"]) - lp["they"],
        "details": lp
    }
