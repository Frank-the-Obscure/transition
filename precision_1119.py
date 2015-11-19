# -*- coding: utf-8 -*-
# author: Frank Hu, Frank-the-Obscure @ GitHub
# cal precision and plot

def precision(y_pred, y_real):
    """ cal precision:
    
    input two list
    output precision and plot(to do)
    """
    import math
    import statistics
    import matplotlib.pyplot as plt
    
    deviation = []
    
    for i in range(0, len(y_pred)):
        deviation.append(math.fabs(y_pred[i] - y_real[i]) / y_real[i])
    
    #print(deviation)
    
    for i in range(0, len(deviation)):
        if deviation[i] > 0.3:
            deviation[i] = 0
        else:
            deviation[i] = 1 - 1 / 0.3 * deviation[i]
    #print(deviation)
    print(statistics.mean(deviation))
    plt.scatter(y_pred, y_real)
    plt.show()
    
precision([1,3,4,5],[2,2,3,4])