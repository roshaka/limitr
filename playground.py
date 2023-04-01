from samplr import samplr

@samplr(count=-2, sample_type='tail', expand=False, info=False)
def get_data():
    # return [
    #     {'name': 'Alice', 'age': 32},
    #     {'name': 'Bob', 'age': 25},
    #     {'name': 'Charlie', 'age': 41},
    #     {'name': 'David', 'age': 19},
    #     {'name': 'Eve', 'age': 56},
    #     {'name': 'Frank', 'age': 28},
    #     {'name': 'Grace', 'age': 39},
    #     {'name': 'Heidi', 'age': 22},
    #     {'name': 'Isaac', 'age': 47},
    #     {'name': 'Jen', 'age': 31},
    # ]
    return ["zero", "one", "two", "three", "four", "five", "six"]

get_data()
