# BMI < 16 : Severely underweight
# 16 <= BMI < 18.5: Underweight
# 18.5 <= BMI < 25: Normal
# 25 <= BMI < 30: Overweight
# BMI > 30: Obese

def bmi_cm(w, h):
    BMI = int(w) / (int(h)/100) ** 2

    if BMI < 16:
        return "BMI < 16 : Severely underweight"
    elif BMI < 18.5:
        return "16 <= BMI < 18.5: Underweight"
    elif BMI < 25:
        return "18.5 <= BMI < 25: Normal"
    elif BMI < 30:
        return "25 <= BMI < 30: Overweight"
    else: 
        return "BMI > 30: Obese"
    return BMI

bmi_cm(53, 162)