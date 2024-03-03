import re
def evaluate_table(text, alpha=0.5):
    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"(\|\s*[^|\r\n]+\s*)+\|", re.MULTILINE)
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """

Here is a comparison of three major airlines, Delta, Emirates, and Lufthansa, based on their hub, average fleet age, and passenger capacity:

| Airline   | Hub                  | Average Fleet Age | Passenger Capacity |
|-----------|----------------------|--------------------|---------------------|
| Delta     | Hartsfield-Jackson   | 15.1 years         | Varies by aircraft  |
|           | Atlanta International|                    |                     |
| Emirates  | Dubai International  | 6.6 years          | Varies by aircraft  |
| Lufthansa | Frankfurt Airport    | 10.3 years         | Varies by aircraft  |

- **Delta Airlines** operates primarily out of Hartsfield-Jackson Atlanta International Airport in Atlanta, Georgia, USA. Their average fleet age is 15.1 years, and their passenger capacity varies depending on the type of aircraft they operate, including narrow-body and wide-body planes.

- **Emirates** is based at Dubai International Airport in Dubai, United Arab Emirates. They have a relatively young fleet, with an average fleet age of 6.6 years. Emirates also operates a range of aircraft, from small to large, so passenger capacity varies accordingly.

- **Lufthansa** is based at Frankfurt Airport in Frankfurt, Germany. Their average fleet age is 10.3 years, and like the other two airlines, Lufthansa has a diverse fleet that includes various types of aircraft with varying passenger capacities.

Please note that the passenger capacity for each airline can vary greatly depending on the specific aircraft they use for different routes and configurations. Therefore, the capacity is not listed in the table as it can change from flight to flight.

"""
final_score = evaluate_table(text)
print(final_score)





