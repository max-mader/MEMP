# evaluate_memp.py

def rate_verb_tense_consistency():
    # TODO: Implement rating logic for verb tense consistency
    pass

def rate_streamlining_sentence_structure():
    # TODO: Implement rating logic for streamlining sentence structure
    pass

def rate_removing_execution_details():
    # TODO: Implement rating logic for removing execution details
    pass

def evaluate_memp_v1():
    rating = 0

    rating += rate_verb_tense_consistency()
    rating += rate_streamlining_sentence_structure()
    rating += rate_removing_execution_details()

    return rating

def rate_sentence_separation_for_clarity():
    # TODO: Implement rating logic for sentence separation for clarity
    pass

def rate_consistency_in_imperative_tone():
    # TODO: Implement rating logic for consistency in imperative tone
    pass

def evaluate_memp_v2():
    rating = 0

    rating += rate_verb_tense_consistency()
    rating += rate_sentence_separation_for_clarity()
    rating += rate_consistency_in_imperative_tone()
    rating += rate_removing_execution_details()

    return rating

def choose_better_memp():
    rating_v1 = evaluate_memp_v1()
    rating_v2 = evaluate_memp_v2()

    if rating_v1 >= rating_v2:
        return "MEMP V1"
    else:
        return "MEMP V2"

# Main evaluation logic
if __name__ == "__main__":
    better_memp = choose_better_memp()
    print(f"The better MEMP is: {better_memp}")