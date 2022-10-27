import requests



def make_request(url):
  '''
  Function to make a GET request against the specified URL
  '''

  r = requests.get(url, verify=False)
  return r

url="https://kite-api.twitter.biz/identity/api/2/roles/unowned-roles?infrastructure_services=hadoop"

make_request(url)