import requests
import json
import pandas as pd
from pandas import DataFrame

def GetAllPokemon():
    
    
    x = 0
    Response = requests.get(f"https://pokeapi.co/api/v2/pokemon/?offset={x}&limit={x+ 1279 %25}",                  
            )

    dataJson = json.loads(Response.content)
    for dic in dataJson['results']:            
        yield dic


    x+= 1279 %25
    
    while x+25 < 1279:
        
        Response = requests.get(f"https://pokeapi.co/api/v2/pokemon/?offset={x}&limit={x+25}",                  
            )

        dataJson = json.loads(Response.content)
        for dic in dataJson['results']:
            yield dic

        x+=25
    

    
    #create a dataframe using the kword arguements 
    
    pass
def GetPokemonStats()->pd.DataFrame:
    ResultTable = DataFrame(columns=['id','name', 'hp', 'attack', 'sp-atk', 'sp-def', 'speed'])
    Allpoke = GetAllPokemon()
    for Id, PokeMon in enumerate(Allpoke):
        dataJson = json.loads(requests.get(PokeMon['url']).content)
        list_temp = [Id]
        for  stat in dataJson['stats']:
            list_temp.append(stat['base_stat'])
            pass

        tempResultTable = DataFrame(list_temp)
        tempResultTable = tempResultTable.T # swaps columns and rows 
        tempResultTable.columns = ResultTable.columns

        ResultTable = pd.concat([ResultTable, tempResultTable], ignore_index=True)

    return ResultTable
temp = GetPokemonStats()