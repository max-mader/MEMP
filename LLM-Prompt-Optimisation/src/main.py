from extract_meta import extract_meta
from create_memp import create_memp
from evaluate_memp import evaluate_memp

def main():
    # Extract meta from LLM response
    meta = extract_meta("LLM_Response.txt")

    # Create Minimal Edit Meta-Prompt
    memp = create_memp(meta)

    # Evaluate MEMPs
    ratings = evaluate_memp(memp)

    # Print the ratings for each MEMP
    print("MEMP V1:")
    print("Verb Tense Consistency and Imperative Mood: Rating -", ratings["v1"]["verb_tense"])
    print("Streamlining Sentence Structure: Rating -", ratings["v1"]["sentence_structure"])
    print("Removing Execution Details: Rating -", ratings["v1"]["execution_details"])

    print("\nMEMP V2:")
    print("Verb Tense Consistency and Imperative Mood: Rating -", ratings["v2"]["verb_tense"])
    print("Sentence Separation for Clarity: Rating -", ratings["v2"]["sentence_separation"])
    print("Consistency in Imperative Tone Across Tasks: Rating -", ratings["v2"]["imperative_tone"])
    print("Removing Execution Details: Rating -", ratings["v2"]["execution_details"])

if __name__ == "__main__":
    main()