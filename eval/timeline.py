import re
def evaluate_timeline_01(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0


    pattern = re.compile(r"\{\d{4}: .+?;?\d{4}: .+?\}", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
this is:
{1918: Armistice signed, ending WWI;1919: Treaty of Versailles signed}
qqqqq
"""
final_score = evaluate_timeline_01(text)
print(final_score)

