import re
def evaluate_keyValue_01(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\{\s*(\w+:\s*\w+(\s*\w+)*)(,\s*\w+:\s*\w+(\s*\w+)*)*\s*\}", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
this is:
{Name: John, Age: 30, Occupation: Engineer}
{Name: John, Age: 30, Occupation: Engineer}
this is:
"""
final_score = evaluate_keyValue_01(text)
print(final_score)




import re
def evaluate_keyValue_02(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\{\s*(\w+\s*=\s*\w+(\s*\w+)*)(,\s*\w+\s*=\s*\w+(\s*\w+)*)*\s*\}", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
this is
{Name = John, Age = 30, Occupation = Engineer} {Name = John, Age = 30, Occupation = Engineer}
this is
"""
final_score = evaluate_keyValue_02(text)
print(final_score)


import re
def evaluate_keyValue_03(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\{\s*(\w+\s*\(\w+(\s*\w+)*\))(,\s*\w+\s*\(\w+(\s*\w+)*\))*\s*\}", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
this is:
{Name (John), Age (30), Occupation (Engineer)}
{Name (John), Age (30), Occupation (Engineer)}
"""
final_score = evaluate_keyValue_03(text)
print(final_score)


import re
def evaluate_keyValue_04(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split())  # 越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\{\s*(Key:\s*\w+\s*,\s*Value:\s*\w+(\s*\w+)*)(;\s*Key:\s*\w+\s*,\s*Value:\s*\w+(\s*\w+)*)*\s*\}", re.MULTILINE)
    score = calculate_score(text, pattern)  # 扣分
    return score

# Example usage
text = """
this is:
{Key: Name, Value: John; Key: Age, Value: 30; Key: Occupation, Value: Engineer}
{Key: Name, Value: John; Key: Age, Value: 30; Key: Occupation, Value: Engineer}

"""
final_score = evaluate_keyValue_04(text)
print(final_score)


import re
def evaluate_keyValue_05(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split())  # 越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\{\s*(\w+\s*->\s*\w+(\s*\w+)*)(,\s*\w+\s*->\s*\w+(\s*\w+)*)*\s*\}", re.MULTILINE)
    score = calculate_score(text, pattern)  # 扣分
    return score

# Example usage
text = """
this is:
{Name -> John, Age -> 30, Occupation -> Engineer} 
aaa 
"""
final_score = evaluate_keyValue_05(text)
print(final_score)
