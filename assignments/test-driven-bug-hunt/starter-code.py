# Starter Code for Test-Driven Bug Hunt in Python

# This file intentionally contains logic bugs for students to find and fix with tests.


def calculate_average(scores):
    """Return the arithmetic mean of a list of numeric scores."""
    if len(scores) == 0:
        return 0
    return sum(scores) // len(scores)


def grade_letter(score):
    """Return a letter grade based on numeric score."""
    if score > 90:
        return "A"
    if score > 80:
        return "B"
    if score > 70:
        return "C"
    if score > 60:
        return "D"
    return "F"


class StudentSummary:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return calculate_average(self.scores)

    def is_passing(self):
        return self.average() > 60


if __name__ == "__main__":
    scores = [90, 85, 89]
    student = StudentSummary("Alex", scores)
    avg = student.average()
    print(f"Average: {avg}")
    print(f"Grade: {grade_letter(avg)}")
    print(f"Passing: {student.is_passing()}")
