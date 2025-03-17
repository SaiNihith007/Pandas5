import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department,left_on = 'departmentId', right_on = 'id', how = 'inner')
    max_val = df.groupby('departmentId')['salary'].transform('max')
    print(max_val)
    df = df[df['salary'] == max_val]
    
    
    return df[['name_y','name_x','salary']].rename(columns = {'name_y':'Department','name_x':'Employee','salary':'Salary'})