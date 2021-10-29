import json
import Constants as C

#loads dict with corresponding data        
def load(num):
    total_dic=dict()
    for name in C.ANIME:
        total_path=f"{C.PATH}{name}/{C.FILES[num]}"
        try:
            with open(total_path) as json_file:
                data = json.load(json_file)
            total_dic[name]=data["Data"]
        except:
            print("error unable to load file")
    return total_dic        

# {
# "Name":string
# "Score":num
# "Genere":list
# }

#
def getAnime_list(animes,genre):
    if animes:
        return animes[genre]
    else:
        return None
#        
def getAnime_data(animes,index):
    if animes and index <len(animes):
        return animes[index]
    else:
        return None
#
def getName(anime):
    if anime:
        return anime["Name"]
    else:
        print(f"Error {anime} is empty")
        return None
#
def getScore(anime):
    if anime:
        return anime["Score"]
    else:
        print(f"Error {anime} is empty")
        return None
#        
def getGenere(anime):
    if anime:
        return anime["Genere"]
    else:
        print(f"Error {anime} is empty")
        return None    