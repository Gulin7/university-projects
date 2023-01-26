def create_contestant(p1, p2, p3):
    return {"p1": p1, "p2": p2, "p3": p3}

def get_problem(contestant, problem):
    return contestant[problem]

def set_problem(contestant, problem, score):
    contestant[problem] = score
