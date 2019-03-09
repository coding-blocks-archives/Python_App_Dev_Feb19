import requests

def main():
  url = "https://graph.facebook.com/4/picture?type=large"
  # url = "https://www.google.com"
  r = requests.get(url)
  print(r.content)
  # print(type(r.content))

if __name__ == "__main__":
  main()