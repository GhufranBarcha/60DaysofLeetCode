import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    student_id= []
    age = []
    for i in range(len(student_data)):
        student_id.append(student_data[i][0])
        age.append(student_data[i][1])

    return pd.DataFrame({"student_id":student_id , "age": age} )    

    