def check_type(sequence:list) -> str:
    type:str = ""

    for i in range(len(sequence) - 2):
        if sequence[i + 1] - sequence[i] == sequence[i + 2] - sequence[i + 1]:
            i += 1
            type = "arithmetic"
        elif sequence[i + 1] / sequence[i] == sequence[i + 2] / sequence[i + 1]:
            i += 1
            type = "geometric"
        else: return ""

    return type

def index_array(elements:list) -> list:
    result:list = []
    for i in range(len(elements)): result.append(i + 1)
    return result

def predict_arithmetic(sequence:list, steps:int, d:float) -> float:
    result:str = ""
    for i in range(steps): result += f"{sequence[0] + (len(sequence) + i) * d}, "
    return result
def predict_geometric(sequence:list, steps:int, r:float) -> float:
    result:str = ""
    for i in range(steps): result += f"{sequence[0] * (pow(r, (len(sequence) + i)))}, "
    return result
def predict_tensor(sequence:list, steps:int) -> str:
    import os
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

    from tensorflow import keras
    import numpy as np

    # creating model
    model:object = keras.Sequential([keras.layers.Dense(units = 1, input_shape=[1])])
    model.compile(optimizer = "sgd", loss = "mean_squared_error")

    # creating arrays
    indexes:list = np.array(index_array(sequence), dtype = float)
    values:list = np.array(sequence, dtype = float)

    # training model
    model.fit(indexes, values, epochs = 1000, verbose = 0)

    # predicting
    result:str = ""
    for i in range(steps):
        prediction = format(model.predict([len(sequence) + (i + 1)])[0][0], ".1f")
        result += f"{prediction}, "

    return result

def predict(sequence:list, steps:int) -> str:
    if len(sequence) <= 2: return "?"
    
    # fixing sequence
    sequence = [float(x) for x in sequence]

    # getting sequence type
    sequence_type:str = check_type(sequence)
    
    # checking sequence type
    if sequence_type == "arithmetic":
        d = sequence[1] - sequence[0]
        result = predict_arithmetic(sequence, steps, d)
    elif sequence_type == "geometric":
        r = sequence[1] / sequence[0]
        result = predict_geometric(sequence, steps, r)
    else: result = predict_tensor(sequence, steps)

    return result[:len(result) - 2]