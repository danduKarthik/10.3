
def process_scores(scores):
    print("Average:", sum(scores)/len(scores))
    print("Highest:", max(scores))
    print("Lowest:", min(scores))

# Get input from user
scores = list(map(float, input("Enter scores separated by spaces: ").split()))
process_scores(scores)
