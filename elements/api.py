import os

res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "UnA8Pqrbqg98bh2gRA", "isbns": "9781632168146"})