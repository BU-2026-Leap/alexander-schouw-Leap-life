import csv
import os
import json

from pathlib import Path

full_base_path = Path(__file__).resolve().parent
input_filename = full_base_path / "test_scores.csv"

output_filename = "output.json"

if os.path.exists(output_filename):
    os.remove(output_filename)

def exam_stats(csv_file):
    average_final = 0.0
    unique_students = 0
    student_list = []
    total_final_score = 0.0
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            if row['exam_name'] == 'final':
                total_final_score = total_final_score + float(row['score'])
            if row['student_id'] not in student_list:
                student_list.append(row['student_id'])
                student_set = set(student_list)
                unique_students = len(student_set)
            average_final = total_final_score / unique_students
    return {
        "average_final": average_final,
        "unique_students": unique_students,
    }

result = exam_stats(input_filename)

with open(output_filename, "w") as out:
    json.dump(result, out, indent=2)

    # TODO: compute average final score

    # TODO: unique student count






