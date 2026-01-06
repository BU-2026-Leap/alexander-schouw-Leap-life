from common.contracts import DataProcessor, ExamScore

class ExamDataProcessor(DataProcessor):
    def compute_number_of_unique_students(self, scores: [ExamScore]) -> int:
        """
        Given a list of ExamScore's, computes the number of unique students in the data set
        """
        student_id_set = set()
        for Examscore in scores:
            student_id_set.add(Examscore.student_id)

        # TODO: implement here
        return len(student_id_set)

    def compute_average_final(self, scores: [ExamScore]) -> float:
        """
        Given a list of ExamScore's, computes the average of all final scores
        """
        number_of_finals = 0
        total_score = 0.0
        for Examscore in scores:
            if Examscore.exam_name.lower() == 'final':
                total_score += Examscore.score
                number_of_finals += 1

        if number_of_finals == 0:
            final_average = 0.0
        else:
            final_average = total_score / number_of_finals

        # TODO: implement here
        return final_average
