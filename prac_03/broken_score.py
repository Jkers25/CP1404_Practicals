"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status
"""

# Note boundary conditions (50 should be a pass, not > 50)
# Note efficiency and nesting; use the fewest number of if/elif as possible


def main():
    score = float(input("Enter score: "))
    evaluation_message =evaluate_score(score)
    print(evaluation_message)


def evaluate_score(score):
    if score < 0 or score > 100:
        message = "Invalid score"
    elif score >= 90:
        message = "Excellent"
    elif score >= 50:
       message = "Passable"
    else:
        message = "Bad"
    return message
if __name__ == '__main__':
    main()


