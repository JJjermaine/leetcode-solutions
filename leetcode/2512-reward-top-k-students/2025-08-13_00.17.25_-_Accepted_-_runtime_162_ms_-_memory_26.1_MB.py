class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # figured out logic but needed help with syntax from gpt
        pos_dic = Counter(positive_feedback)
        neg_dic = Counter(negative_feedback)

        student_dic = defaultdict(int)

        for i in range(len(report)):
            words = report[i].split()
            for word in words:
                if pos_dic[word]:
                    student_dic[student_id[i]] += 3
                if neg_dic[word]:
                    student_dic[student_id[i]] -= 1
                if not student_dic[student_id[i]]:
                    student_dic[student_id[i]] = 0
        #print(student_dic)
        # Sort by score desc, then id asc
        sorted_items = sorted(student_dic.items(), key=lambda x: (-x[1], x[0]))

        res = []

        for i in range(k):
            res.append(sorted_items[i][0])
        return res
