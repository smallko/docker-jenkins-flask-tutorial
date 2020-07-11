import requests
# Change the value of experience that you want to test
url = 'http://192.168.79.151:8000/api'
feature = [[5.8, 4.0, 1.5, 0.3]]
labels ={
  0: "setosa",
  1: "versicolor",
  2: "virginica"
}

r = requests.post(url,json={'feature': feature})
print(labels[r.json()])
