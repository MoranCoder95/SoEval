import re
def evaluate_flowchart_01(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\{[^\}]*\→[^\}]*\}", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
this is:
   {Start → Analyze → Design → Implement → Test → Deploy}
aaaa
"""
final_score = evaluate_flowchart_01(text)
print(final_score)


import re
def evaluate_flowchart_02(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0


    pattern = re.compile(r"\{[^\}]*\->[^\}]*\}", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
this is 
   {Init -> Plan -> Execute -> Review -> Complete}
"""
final_score = evaluate_flowchart_02(text)
print(final_score)


import re
def evaluate_flowchart_03(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0


    pattern = re.compile(r"\{[^\}]*\=>[^\}]*\}", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
this is 
   {Begin => Assess => Develop => Test => Release}     {Begin => Assess => Develop => Test => Release}
aaa
"""
final_score = evaluate_flowchart_03(text)
print(final_score)




import re
def evaluate_flowchart_04(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0


    pattern = re.compile(r"\{Step\s+\d+:[^\}]*\->[^\}]*\}", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
Sure, here's a simplified single-line flowchart detailing the process of making a movie:

{Step 1: Scriptwriting -> Step 2: Pre-production -> Step 3: Casting -> Step 4: Financing -> Step 5: Location Scouting -> Step 6: Hiring Crew -> Step 7: Production -> Step 8: Post-production -> Step 9: Editing -> Step 10: Sound Design -> Step 11: Visual Effects -> Step 12: Music Composition -> Step 13: Marketing -> Step 14: Distribution -> Step 15: Release -> Step 16: Promotion}
"""
final_score = evaluate_flowchart_04(text)
print(final_score)


