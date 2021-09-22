import importlib
hash_table = importlib.import_module('009_hash_table_dict')
LinkedDict = getattr(hash_table, 'LinkedDict')


def get_absent_student(all_array, present_array):
    student = dict()
    for key1 in all_array:
        student[key1] = True
    for key2 in present_array:
        del student[key2]
    for key3 in student.keys():
        return key3


if __name__ == '__main__':
    all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
    present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]
    print(get_absent_student(all_students, present_students))
