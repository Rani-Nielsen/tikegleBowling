
dict_ = {"points":[[7,0],[1,1],[0,3],[3,6],[10,0],[8,2],[0,7],[3,7]],"token":"NwKedfrJJI8dXuhfsIpqLREtvnWeAT6Z"}

def tikegleBowling(input_):
    """
    Udregner point i et spil ti-kegle bowling
    
    :param: en dict som indeholder en key: 'point', som er en liste af lister med hver to elementer
    :return: slut-point i et spil ti-kegle bowling 
    """
    
    turns = input_['points']
    
    score = 0
    
    for i in range(0, len(turns)-1):
        
        # hvis der er strike
        if turns[i][0] == 10:
            score += 10 + sum(turns[i+1])
            
        # hvis der er spare
        elif sum(turns[i]) == 10:
            score += 10 + turns[i+1][0]
            
        # hvis der hverken er strike eller spare
        else:
            score += sum(turns[i])
            
    # udregner tværsummen af den sidste tur
    score += sum(turns[-1])

    return score

tikegleBowling(dict_)
