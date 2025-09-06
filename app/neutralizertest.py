from app.neutralizeregex import neutralize_regex


sentences = [
    "She gave him her notes. He was grateful.",
    "His car is bigger than hers.",
    "They was happy yesterday.",
    "He is a doctor. She is a nurse."
    "She said, He will come later.",
]

for s in sentences:
    print("Input:      ", s)
    print("Neutralized:", neutralize_regex(s))
    print("-" * 50)