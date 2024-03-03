import re
def evaluate_text_01(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\[[^\]]+\](?:\s*\w+\s*=\s*.+)+", re.DOTALL)

    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
Certainly! The Himalayas are a prominent mountain range in Asia, known for their majestic peaks and significant impact on the region's climate. Here's the information in INI format:

```ini
[Himalayas]
Location = Asia (spanning five countries: India, Nepal, Bhutan, China, and Pakistan)
Length = Approximately 2,500 kilometers (1,550 miles)
Climatic Influence = 
    1. Acts as a barrier for cold winds from Central Asia, moderating temperatures in the Indian subcontinent.
    2. Responsible for creating the monsoon patterns in South Asia.
    3. Influences rainfall patterns by blocking moisture-laden winds and causing heavy precipitation on the windward side.
```

This format presents the key characteristics of the Himalayas in a structured and easily readable manner.


"""
final_score = evaluate_text_01(text)
print(final_score)

