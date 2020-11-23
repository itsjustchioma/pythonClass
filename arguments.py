#health calculator that would tell you how long you will live
def health_calculator(age, apples_ate, cigs_smoked):
    predicted_age = (100 -age) + (apples_ate * 5) - (cigs_smoked * 2)
    print(predicted_age)

buckys_data = [27, 20, 0]

health_calculator(buckys_data[0], buckys_data[1], buckys_data[2])
health_calculator(*buckys_data)