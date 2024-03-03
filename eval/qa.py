import re
def evaluate_qa_01(text, alpha=0.5):

    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"Q:\s*.+\n\s*A:\s*.+")
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
Q: What is photosynthesis?
A: Photosynthesis is the process by which green plants, algae, and some bacteria convert light energy into chemical energy in the form of glucose (a sugar) while releasing oxygen as a byproduct.

Q: Where does photosynthesis take place?
A: Photosynthesis primarily takes place in the chloroplasts of plant cells, specifically in the chlorophyll-containing structures called thylakoids.

Q: What are the main reactants needed for photosynthesis?
A: The main reactants required for photosynthesis are carbon dioxide (CO2) from the atmosphere, water (H2O) absorbed through the plant's roots, and sunlight.

Q: What is the role of sunlight in photosynthesis?
A: Sunlight provides the energy necessary to drive the photosynthesis process. Specifically, it powers the conversion of carbon dioxide and water into glucose by facilitating a series of chemical reactions.

Q: What is chlorophyll, and what is its role in photosynthesis?
A: Chlorophyll is a green pigment found in chloroplasts. Its primary role is to absorb light energy, mainly in the blue and red parts of the electromagnetic spectrum, and use it to convert carbon dioxide and water into glucose and oxygen through a series of chemical reactions.

Q: Can you explain the two stages of photosynthesis?
A: Sure. Photosynthesis consists of two main stages:
   1. Light-dependent reactions: These occur in the thylakoid membranes and require sunlight. During these reactions, light energy is used to split water molecules into oxygen and protons while producing ATP (adenosine triphosphate) and NADPH (nicotinamide adenine dinucleotide phosphate), which are energy-rich molecules used in the next stage.
   2. Calvin cycle (light-independent reactions): This stage takes place in the stroma of chloroplasts and does not require direct sunlight. Here, ATP and NADPH generated in the previous stage are used to convert carbon dioxide into glucose through a series of chemical reactions.

Q: What happens to the oxygen produced during photosynthesis?
A: The oxygen produced as a byproduct of photosynthesis is released into the atmosphere, providing oxygen for respiration in animals and other organisms that require it for survival.

Q: How is glucose used by the plant?
A: Glucose produced during photosynthesis serves as an energy source for the plant. It can be used immediately for energy or stored as starch for later use. Additionally, glucose can be converted into other essential molecules, such as cellulose for cell wall formation and various organic compounds for plant growth and development.

Q: What is the overall equation for photosynthesis?
A: The overall equation for photosynthesis is:
   6 CO2 + 6 H2O + light energy → C6H12O6 (glucose) + 6 O2
   This equation represents the conversion of carbon dioxide and water into glucose and oxygen in the presence of sunlight.

Q: Why is photosynthesis crucial for life on Earth?
A: Photosynthesis is crucial because it is the primary process that provides oxygen for the atmosphere and serves as the foundation of the food chain. It produces glucose, which serves as an energy source for plants and, subsequently, for animals and humans that consume plants directly or indirectly. Without photosynthesis, life as we know it would not be sustainable.
"""
final_score = evaluate_qa_01(text)
print(final_score)



import re
def evaluate_qa_02(text, alpha=0.5):

    def calculate_score(text, pattern):
        non_structured_text = pattern.sub("", text)
        E = len(non_structured_text.split()) #越小越好
        T = len(text.split())
        return E / T if T != 0 else 1.0

    pattern = re.compile(r"Question:\s*.+\n\s*Answer:\s*.+")
    score = calculate_score(text, pattern) #扣分
    return score

# Example usage
text = """
Question: What are some effective strategies for overcoming procrastination?
Answer: There are several strategies that can help you overcome procrastination:

Question: Can you provide an example of a time management technique that can help combat procrastination?
Answer: One effective time management technique is the Pomodoro Technique. It involves working on a task for 25 minutes, then taking a 5-minute break. This can help break a large task into smaller, more manageable chunks and reduce the temptation to procrastinate.

Question: How can setting specific goals help in overcoming procrastination?
Answer: Setting specific, measurable, and achievable goals can provide you with a clear sense of direction and purpose. When you have a clear goal in mind, it becomes easier to stay focused and motivated, making it less likely for procrastination to creep in.
"""
final_score = evaluate_qa_02(text)
print(final_score)
