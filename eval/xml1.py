import re

def evaluate_xml(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    # Updated pattern to match XML-like tags
    # pattern = re.compile(r"<\s*([\w\W]+?)\s*>", re.MULTILINE)
    pattern = re.compile(r"<\s*([\w\W]+?)\s*>([\w\W]+?)<\s*/\s*\1\s*>", re.MULTILINE)

    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
Certainly! Here's the information about the Great Wall of China in XML format:

```xml
<GreatWallOfChina>
  <Length>21,196.18 miles (34,000 kilometers)</Length>
  <Location>Across northern China</Location>
  <HistoricalSignificance>
    The Great Wall of China is a monumental fortification and UNESCO World Heritage Site. It was built over centuries, with various sections constructed by different Chinese dynasties, starting as early as the 7th century BC and continuing into the 17th century AD.

    - It served as a defensive barrier to protect China from invasions by nomadic tribes from the north.
    - It played a significant role in the history of China, symbolizing the country's determination to protect its territory and culture.
    - It is one of the most iconic and recognizable man-made structures in the world.
  </HistoricalSignificance>
</GreatWallOfChina>
```

Please note that the length mentioned here is an approximate figure and can vary depending on the source. The Great Wall of China is not a continuous wall but consists of multiple sections built during different historical periods.
"""
final_score = evaluate_xml(text)
final_score
