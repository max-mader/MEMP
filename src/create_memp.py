# create_memp.py

def extract_first_paragraph(llm_response):
    # Extract the first paragraph from the LLM response
    first_paragraph = llm_response.split('\n\n')[0]
    return first_paragraph

def create_memp(llm_response):
    # Extract the first paragraph from the LLM response
    first_paragraph = extract_first_paragraph(llm_response)

    # Formulate the Minimal Edit Meta-Prompt (MEMP)
    memp = f"Given the importance of {first_paragraph.lower()}, how can one leverage specific AI tool capabilities effectively?"

    return memp

def generate_bullet_points(llm_response):
    # Extract the first paragraph from the LLM response
    first_paragraph = extract_first_paragraph(llm_response)

    # Generate short bullet points for the MEMP
    bullet_points = [
        f"Incorporates the model's emphasis on {first_paragraph.lower()}.",
        "Highlights the need for understanding AI tool capabilities to enhance outcomes.",
        "Acts as a refined query that aligns with the model's perceived optimal approach."
    ]

    return bullet_points

# Example usage
llm_response = "To generate creative images using AI tools, it's crucial to provide detailed, vivid descriptions and specify the desired style or influence. Understanding the capabilities and limitations of the specific AI tool you're using is also important, as different tools may require different approaches for optimal results."

memp = create_memp(llm_response)
print(memp)

bullet_points = generate_bullet_points(llm_response)
for point in bullet_points:
    print(f"- {point}")