import re
def evaluate_list_01(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"^- .+", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
- Apple
- Samsung
- Huawei
"""
final_score = evaluate_list_01(text)
print(final_score)




import re
def evaluate_list_02(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"^\* .+", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
* Apple
* Samsung
* Huawei
"""
final_score = evaluate_list_02(text)
print(final_score)


import re
def evaluate_list_03(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"^\d+\.\s.+", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
As of my last knowledge update in January 2022, I can provide you with a list of some of the most visited countries in the world. Please note that tourism rankings can change over time, and the most current data may be different. Here is a list of popular tourist destinations in no particular order:

1. France
2. Spain
3. United States
4. China
5. Italy
6. Turkey
7. Mexico
8. Germany
9. Thailand
10. United Kingdom
11. Malaysia
12. Saudi Arabia
13. India
14. Japan
15. South Korea

Keep in mind that this list is not exhaustive, and there are many other countries that attract a significant number of tourists. Additionally, tourism statistics can change from year to year, so I recommend checking a reliable source like the United Nations World Tourism Organization (UNWTO) or a similar organization for the most up-to-date information on the most visited countries in the world.
"""
final_score = evaluate_list_03(text)
print(final_score)


import re
def evaluate_list_04(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split())  # 越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"^\+ .+", re.MULTILINE)
    score = calculate_score(text, pattern)  # 扣分
    return score

# Example usage
text = """
+ Apple
+ Samsung
+ Huawei
"""
final_score = evaluate_list_04(text)
print(final_score)


import re
def evaluate_list_05(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split())  # 越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"^\([a-z]\)\s.+", re.MULTILINE)
    score = calculate_score(text, pattern)  # 扣分
    return score

# Example usage
text = """

(a) Apple
(b) Samsung
(c) Huawei

"""
final_score = evaluate_list_05(text)
print(final_score)
