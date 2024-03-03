import re
def evaluate_heading_01(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"^(# .+)$\n(.*\n)*?(## .+(\n|$))+$", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
# "The Last Oasis"
## "Desolation and Hope"
      """
final_score = evaluate_heading_01(text)
print(final_score)



import re
def evaluate_heading_02(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"<h1>.+?</h1>\s*(<h2>.+?</h2>\s*)+", re.DOTALL)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
Certainly! Here is a two-level outline for a piece on urban development:

<h1>Urban Development: Creating Sustainable Cities</h1>
<h2>I. Introduction to Urban Development</h2>
1.1 Definition and Importance
1.2 Historical Context
1.3 Purpose of the Article

<h2>II. Key Challenges in Urban Development</h2>
2.1 Population Growth and Urbanization
2.2 Infrastructure and Transportation
2.3 Environmental Sustainability
2.4 Social Equity and Inclusion

<h1>Approaches to Sustainable Urban Development</h1>
<h2>III. Planning and Design Strategies</h2>
3.1 Smart Growth and Compact Development
3.2 Mixed-Use Zoning
3.3 Transit-Oriented Development
3.4 Green and Open Spaces

<h2>IV. Sustainable Infrastructure</h2>
4.1 Energy-Efficient Buildings
4.2 Renewable Energy Integration
4.3 Water and Waste Management
4.4 Innovative Transportation Solutions

<h2>V. Community Engagement and Social Inclusion</h2>
5.1 Affordable Housing Initiatives
5.2 Public Participation in Planning
5.3 Inclusive Urban Design
5.4 Cultural Preservation

<h1>Conclusion: Shaping the Future of Our Cities</h1>
<h2>VI. The Path Forward</h2>
6.1 Policy Recommendations
6.2 Collaborative Efforts
6.3 Vision for Sustainable Urban Futures

This outline provides a structured framework to discuss the various aspects of urban development, from its challenges to the strategies and approaches that can lead to more sustainable and inclusive cities.
"""
final_score = evaluate_heading_02(text)
print(final_score)



import re
def evaluate_heading_03(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"^\s*\d+\.\s+.+(\n\s*\d+\.\d+\s+.+)*", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
Sure, here's a two-level outline for a review on classical music:

1. Overview of Classical Music
1.1 Historical Significance
1.2 Key Characteristics
1.3 Importance in Music History

2. Major Composers and Their Contributions
   2.1 Ludwig van Beethoven
       2.1.1 Early Life and Background
       2.1.2 Notable Compositions
       2.1.3 Influence on Classical Music
   2.2 Wolfgang Amadeus Mozart
       2.2.1 Life and Musical Education
       2.2.2 Iconic Works
       2.2.3 Legacy in Classical Music
   2.3 Johann Sebastian Bach
       2.3.1 Biography and Musical Journey
       2.3.2 Masterpieces
       2.3.3 Lasting Impact on Classical Music

3. Classical Music Forms and Styles
   3.1 Symphony
       3.1.1 Development and Evolution
       3.1.2 Notable Symphonies
   3.2 Concerto
       3.2.1 Origins and Purpose
       3.2.2 Renowned Concertos
   3.3 Opera
       3.3.1 Emergence and Transformation
       3.3.2 Opera Masterpieces

4. Influence on Modern Music
   4.1 Romantic Era
       4.1.1 Transition from Classical to Romantic
       4.1.2 Composers Influenced by Classical Music
   4.2 Contemporary Music
       4.2.1 Incorporation of Classical Elements
       4.2.2 Notable Modern Compositions

5. Impact on Society and Culture
   5.1 Cultural Significance
       5.1.1 Role in Cultural Traditions
       5.1.2 Classical Music in Film and Media
   5.2 Educational Importance
       5.2.1 Classical Music in Schools
       5.2.2 Fostering Musical Appreciation

6. Conclusion
   6.1 Enduring Legacy
   6.2 Personal Reflections on Classical Music
   6.3 Encouragement for Further Exploration
"""
final_score = evaluate_heading_03(text)
print(final_score)
