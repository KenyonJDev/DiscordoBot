from google import google
def userRecipe(custom, after):
    if after == False:       
        term = input(" Bot : What would you like to search?\n User: ")
    else:
        term = custom
    search_results = google.search(term)
    print(" Bot: Here is what I found for '" + term + "':")
    for result in search_results:
        if result.index == 5:
            break
        else:
            result.name = result.name.replace(result.link,"")
            print("       " +  str(result.index+1) + ": " + result.name + " - " + result.link + "\n")