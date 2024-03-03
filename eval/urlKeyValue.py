import re
def evaluate_urlKeyValue(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"\?\s*([\w=&]+)", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
To organize the information you provided in the form of a URL with key-value pairs, you can do it like this:

```
https://example.com/book_info?Book=TheHobbit&Publisher=Tolkien
```

Replace "example.com" with the actual domain where you want to use this URL."""
final_score = evaluate_urlKeyValue(text)
print(final_score)

