def process_scores(students):
    averages = {}
    
    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
        
    return averages


def classify_grades(averages):
    
    classified = {}
    
    for name, avg in averages.items():
        if avg >= 90:
            grade = "A"
        elif avg >= 75 and avg <= 89:
            grade = "B"
        elif avg >= 60 and avg <= 74:
            grade = "C"
        else:
            grade = "F"
            
        classified[name] = (avg, grade)
        
    return classified


def generate_report(classified, passing_avg=70):
    passed_count = 0
    failed_count = 0
    total_student = 0
    
    print("==============Student Grade Report================")
        
    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"

        total_student += 1
        
        if status == "PASS":
            passed_count += 1

        if status == "FAIL":
            failed_count += 1
        
        print(f"{name:10}  Avg: {avg:6}  Grade: {grade}  Status: {status}")
    
    print("=" * 50)
    
    return total_student, passed_count, failed_count
    

# Main Block
  
students = {
    "Alice": [85, 90, 88, 92, 87],
    "Bob": [73, 75, 80, 79, 81],
    "Charlie": [95, 92, 96, 99, 98],
    "Maya": [63, 58, 62, 64, 60],
    "Tom": [51, 54, 61, 52, 59],
    "Sara": [78, 68, 76, 77, 79]
}

averages = process_scores(students)
classified = classify_grades(averages)
result = generate_report(classified)

print(f"Total number of students: {result[0]}")
print(f"Total students passed: {result[1]}")
print(f"Total students failed: {result[2]}")
