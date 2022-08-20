score = input("Enter Score: ")
try:
    score = float(score)
except:
    print("Error: Score isn't number")
    quit()

if score > 1.0 or score <= 0.1:
    print("Error: Write a number between 0.1 at 1.0")
    quit()

if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("D")

