class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = 0
        st_len = len(students)
        sa_len = len(sandwiches)
        if sa_len >= st_len:
            for i in sandwiches[:st_len]:
                if i in students:
                    students.remove(i)
                else:
                    return len(students)
        else:
            for i in sandwiches:
                if i in students:
                    students.remove(i)
                else:
                    return len(students)
        return len(students)