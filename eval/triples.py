import re
def evaluate_triple_01(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\(([^,]+),\s*([^,]+),\s*([^)]+)\)", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
this is 
(Harry Potter, Author, J.K. Rowling) 
(Harry Potter, Author, J.K. Rowling)
aaa
"""
final_score = evaluate_triple_01(text)
print(final_score)




import re
def evaluate_triple_02(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\{([^,]+),\s*([^,]+),\s*([^}]+)\}", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
ffff
{Eiffel Tower, Location, Paris, France} aaa 
{Apple iPhone, Category, Smartphone}
this
"""
final_score = evaluate_triple_02(text)
print(final_score)





import re
def evaluate_triple_03(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\[([^,]+),\s*([^,]+),\s*([^]]+)\]", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
[Mona Lisa, Artist, Leonardo da Vinci] [Periodic Table, Inventor, Dmitri Mendeleev]
"""
final_score = evaluate_triple_03(text)
print(final_score)




import re
def evaluate_triple_04(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split())  # 越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\(([^-]+)-\s*([^-]+)-\s*([^)]+)\)", re.MULTILINE)
    score = calculate_score(text, pattern)  # 扣分
    return score

# Example usage
text = """
(Earth-Third Planet- Solar System)
(Beethoven- Composer- Symphony No.9)
"""
final_score = evaluate_triple_04(text)
print(final_score)

