import re
def evaluate_attributeGraph_01(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\(([\w\s,]+)\)")
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
Here is an outline of essential vitamins for human health:

1. Vitamin A
2. Vitamin B1 (Thiamine)
3. Vitamin B2 (Riboflavin)
4. Vitamin B3 (Niacin)
5. Vitamin B5 (Pantothenic Acid)
6. Vitamin B6 (Pyridoxine)
7. Vitamin B7 (Biotin)
8. Vitamin B9 (Folate or Folic Acid)
9. Vitamin B12 (Cobalamin)
10. Vitamin C (Ascorbic Acid)
11. Vitamin D
12. Vitamin E (Tocopherol)
13. Vitamin K (Phylloquinone)
14. Vitamin F (Essential Fatty Acids, including Omega-3 and Omega-6)
15. Vitamin P (Bioflavonoids, sometimes referred to as Vitamin C complex)

These vitamins play various important roles in the body, including maintaining overall health, supporting immune function, promoting skin health, aiding in energy metabolism, and more. A balanced diet with a variety of foods is essential to ensure you get an adequate intake of these vitamins for optimal health.
"""
final_score = evaluate_attributeGraph_01(text)
print(final_score)




import re
def evaluate_attributeGraph_02(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\{([\w\s,]+)\}")
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
this is the : 
{Make, Model, Year, Color, Engine Type}
this is the results.
"""
final_score = evaluate_attributeGraph_02(text)
print(final_score)


import re
def evaluate_attributeGraph_03(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\(([\w\s,]+)\)")
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
this is the : 
(Processor, RAM, Storage, Graphics Card)
this is the results.
"""
final_score = evaluate_attributeGraph_03(text)
print(final_score)


import re
def evaluate_attributeGraph_04(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split())  # 越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\(([\w\s-]+)\)")
    score = calculate_score(text, pattern)  # 扣分
    return score

# Example usage
text = """
this is the : 
(Floors-Elevators-Offices-Parking Space)
this is the results.
"""
final_score = evaluate_attributeGraph_04(text)
print(final_score)


import re
def evaluate_attributeGraph_05(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split())  # 越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\(([\w\s;]+)\)")
    score = calculate_score(text, pattern)  # 扣分
    return score

# Example usage
text = """
this is the : 
(Sugar; Salt; Vegetable Oil; Yeast)
this is the results.
"""
final_score = evaluate_attributeGraph_05(text)
print(final_score)
