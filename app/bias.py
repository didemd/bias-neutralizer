import random

text="He is a doctor. She is a teacher. They were there."


def mock_bias_score(text: str) -> float:
    """
    Mock bias logic:
    - If sentence has 'he is a doctor' → pretend bias is high (0.8).
    - If sentence has 'she is a doctor' → pretend bias is lower (0.3).
    - Otherwise → random number between 0.4 and 0.6 (neutral)
    """
    text = text.lower()
    if "he is a doctor" in text:
        return 0.8
    elif "she is a doctor" in text:
        return 0.3
    else:
        return round(random.uniform(0.4, 0.6), 2)

if __name__ == "__main__": 
    print(mock_bias_score("He is a doctor")) 
    print(mock_bias_score("she is a doctor")) 
    print(mock_bias_score("They are engineers"))

