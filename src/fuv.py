def fuv(puv, pum):
    """
    Calculates the FUV from the PUV and PUM. FUV[i] is true if PUV[i] is false or if 
    the entire row of PUM[i] is true.
    """
    fuv = [False]*len(puv)
    for i in range(len(puv)):
        if puv[i] == False:
            fuv[i] = True
        else:
            fuv[i] = True
            for j in range(len(pum[i])):
                if pum[i][j] == False:
                    fuv[i] = False
                    break
    return fuv



