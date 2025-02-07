import numpy as np
import pandas as pd

def transform_input_data(sex, smoker, day, time):
    sex_mapping = {"Male": 0, "Female": 1}
    smoker_mapping = {"Yes": 1, "No": 0}
    day_mapping = {"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3}
    time_mapping = {"Lunch": 0, "Dinner": 1}

   
    sex = sex_mapping.get(sex, -1)
    smoker = smoker_mapping.get(smoker, -1)
    day = day_mapping.get(day, -1)
    time = time_mapping.get(time, -1)

    return sex, smoker, day, time

def get_results(model, total_bill, sex, smoker, day, time, size):
    try:
        
        sex, smoker, day, time = transform_input_data(sex, smoker, day, time)

        additional_features = [0] * 6  
        inputs = np.array([[total_bill, sex, smoker, day, time, size] + additional_features])
        result = model.predict(inputs)

        return result

    except KeyError as e:
        raise e
    except Exception as e:
        raise Exception(f"An error occurred during prediction: {str(e)}")




