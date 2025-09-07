import requests 
import csv

with open("movies.csv", "w", newline="") as file:
    w = csv.writer(file)
    w.writerow(["id", 
                "title", 
                "director", 
                "release_date", 
                "rt_score"])

    url = requests.get("https://ghibliapi.dev/films?limit=5").json()
    x = url[ :5]

    for movie in x:
        id = movie["id"]
        title = movie["title"]
        director = movie["director"]
        release_date = movie["release_date"]
        rt_score = movie["rt_score"]
    
        w.writerow([id, title, director, release_date, rt_score])



