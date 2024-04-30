def activation(x):
    return 1 / (1 + 2.718281828**-x)


def forwardPass(wiek, waga, wzrost):
    # sourcery skip: inline-immediately-returned-variable
    hidden1 = wiek * -0.46122 + waga * 0.97314 + wzrost * -0.39203 + 0.80109
    hidden1_po_aktywacji = activation(hidden1)
    hidden2 = wiek * 0.78548 + waga * 2.10684 + wzrost * -0.57487 + 0.43529
    hidden2_po_aktywacji = activation(hidden2)
    output = hidden1_po_aktywacji * -0.81546 + hidden2_po_aktywacji * 1.03775
    return output + -0.2368


print(forwardPass(23, 75, 176))
