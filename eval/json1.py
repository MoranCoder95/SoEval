import re
def evaluate_json(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0
    #
    # pattern = re.compile(r"\{\s*([\w\W]+?)\s*\}", re.MULTILINE)
    # Regular expression to match nested JSON structures
    pattern = re.compile(r'\{(?:[^{}]|{[^{}]*})*\}', re.DOTALL)

    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
Certainly! Here is the information about the Golden Gate Bridge in JSON format:

```json
{
  "Peaches": {
    "Main Nutrients": {
      "Vitamins": ["Vitamin C", "Vitamin A", "Vitamin E"],
      "Minerals": ["Potassium", "Magnesium", "Calcium"],
      "Others": ["Dietary Fiber", "Antioxidants"]
    },
    "Best Season for Consumption": {
      "Northern Hemisphere": "May to September",
      "Southern Hemisphere": "November to March"
    },
    "Economic Value": {
      "Global Production": "21.6 million metric tons (2021)",
      "Top Producers": ["China", "Italy", "United States"],
      "Uses": ["Fresh Consumption", "Canned Products", "Jams", "Beverages"]
    }
  }
}

```

You can use this JSON format to easily incorporate this information into your applications or databases.

"""
final_score = evaluate_json(text)
print(final_score)




