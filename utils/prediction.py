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

def get_function(type:str, c:float) -> str:
    c = str(c)
    
    if type == "arithmetic" and c[0] != "-":
        return f"x + {c}"
    elif type == "arithmetic" and c[0] == "-":
        return f"x - {c[1:]}"
    elif type == "geometric":
        return f"x * {c}"
    else:
        return "Unknown"

def plot_function(function:str) -> None:
    import matplotlib.pyplot as plt
    import numpy as np

    # fixing function
    x:list = np.linspace(-5, 5, 100)
    if function[2] == "*": function = f"x ** {function[4]}"
    function:float = eval(function)

    # plotting
    fig:object = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    ax.spines["left"].set_position("center")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    plt.plot(x, function, "b")
    plt.show()
def plot_tensor(tensor:list) -> None:
    import matplotlib.pyplot as plt

    plt.plot(index_array(tensor), tensor, "b")
    plt.show()

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
    model.fit(indexes, values, epochs = 10000, verbose = 0)

    # predicting
    result:str = ""
    for i in range(steps):
        prediction:float = model.predict([len(sequence) + (i + 1)])[0][0]
        prediction = format(prediction, ".1f")

        result += f"{prediction}, "

    return result

def predict(sequence:list, steps:int) -> str:
    if len(sequence) <= 2: return "?"
    
    # fixing sequence
    sequence = [float(x) for x in sequence]

    # getting sequence type
    sequence_type:str = check_type(sequence)
    
    # predicting
    if sequence_type == "arithmetic":
        d = sequence[1] - sequence[0]
        result:str = predict_arithmetic(sequence, steps, d)
    elif sequence_type == "geometric":
        r = sequence[1] / sequence[0]
        result:str = predict_geometric(sequence, steps, r)
    else: result:str = predict_tensor(sequence, steps)

    # getting function
    if sequence_type == "arithmetic":
        sequence_function:str = get_function(sequence_type, d)
    elif sequence_type == "geometric":
        sequence_function:str = get_function(sequence_type, r)
    else:
        sequence_function:str = get_function(sequence_type, None)

    return sequence_function, result[:len(result) - 2]
