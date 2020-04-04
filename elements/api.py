import requests

res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "UnA8Pqrbqg98bh2gRA", "isbns": "9781632168146"})
res = res.json()
print(res['books'][0]['average_rating'])