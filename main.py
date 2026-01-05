import csv
import os
import json

from pathlib import Path

full_base_path = Path(__file__).resolve().parent
input_filename = full_base_path / "test_scores.csv"

output_filename = "output.json"

if os.path.exists(output_filename):
    os.remove(output_filename)

average_final = 0.0
unique_students = 0

number_of_finals_count = 0
total_final_score = 0.0

with open(input_filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

        # TODO: compute average final score

        if row['exam_name'] == 'final':
            number_of_finals_count += 1
            total_final_score = total_final_score + float(row['score'])
            unique_students += 1
        # TODO: unique student count

    average_final = total_final_score / number_of_finals_count

result = {
    "average_final": average_final,
    "unique_students": unique_students,
}

with open(output_filename, "w") as out:
    json.dump(result, out, indent=2)

