def pum(lcm, cmv):
    pum = [[False for _ in range(len(lcm[0]))] for _ in range(len(lcm))]
    for i in range(len(lcm)):
        for j in range(len(lcm[i])):
            operator = lcm[i][j]
            match operator:
                case "ANDD":
                    pum[i][j] = cmv[i] and cmv[j]
                case "ORR":
                    pum[i][j] = cmv[i] or cmv[j]
                case "NOTUSED":
                    pum[i][j] = True
    return pum
