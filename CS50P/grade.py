# Program : Grade Checker
print("Grade Checker")
print("─────────────")

score = int(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score. Enter between 0 and 100.")
elif score >= 90:
   print(f"Score: {score} → Grade: A (Excellent!)")
elif score >= 80:
    print(f"Score: {score} → Grade: B (Good!)")
elif score >= 70:
    print(f"Score: {score} → Grade: C (Average)")
elif score >= 60:
    print(f"Score: {score} → Grade: D (Below Average)")
else:
    print(f"Score: {score} → Grade: F (Failed)")
