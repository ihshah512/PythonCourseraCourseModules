#requests api we can install to use it to interact with internet
import sys
import requests
import json
import yt_dlp
import pandas as pd


#JSON itself is used language agnostic

def main():
    reqeustsFunc()
    #getDataFromYoutube() #function does not work


def reqeustsFunc():
    if len(sys.argv) != 2:
        sys.exit()
    # get the data from web
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

    #store the data into a variable or object
    o = response.json()

    #STORE DATA INTO LIST
    result_list = o["results"]

    # Create the data frame
    df = pd.DataFrame(result_list)

    #keep the cololumns you want
    coloumn = ["artistName", "trackName", "releaseDate", "collectionName"]
    df = df[coloumn]

    #HOW TO CONCATENATE THE ARGUMENT PASSING ON COMMAND LINE WITH FILE NAME
    itunes_results_csv = f"{sys.argv[1]}_itunes_results.csv"
    itunes_results_xlsx = f"{sys.argv[1]}_itunes_results.xlsx"

    #save the data into the files
    df.to_csv(itunes_results_csv, index=False)
    df.to_excel(itunes_results_xlsx, index=False)
    print(f"Successfully saved {len(df)} songs to CSV and Excel!")

    #print(json.dumps(o, indent=3)) #this line of code prints a formatted form of jason data
    for result in o["results"]:
        # Note the 'f' at the start and the { } around every variable
        #print(f"Singer: {result['artistName']:<30}, Song: {result['trackName']:<40}, Date Released: {result['releaseDate']}")
        print(f"{result['trackName']:<40}")
def getDataFromYoutube():

    URL = 'https://www.youtube.com/results?search_query=nusrat'
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(URL, download=False)
        # This 'info' dictionary is your JSON data
        print(info['entries'][0]['title'])


main()
