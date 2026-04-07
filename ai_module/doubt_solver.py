from text_processing import extract_keywords

def solve_doubt(question):
    keywords = extract_keywords(question)

    if "python" in keywords:
        return "Python ek programming language hai jo AI aur web me use hoti hai."

    elif "database" in keywords:
        return "Database data store karne ke liye use hota hai."

    elif "ai" in keywords:
        return "AI ka matlab Artificial Intelligence hota hai."

    else:
        return "Sorry, mujhe samajh nahi aaya. Thoda clear pucho."
