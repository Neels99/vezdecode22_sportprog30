import requests

users_input = input()
users = users_input.split(' ')

for user in users:
    resp = requests.get('https://codeforces.com/api/user.status?handle={0}'.format(user))
    result = 0
    cache = set()

    for x in resp.json().get('result', []):
        cache.add(str(x['problem']['contestId']) + x['problem']['name'])

    print("{0} {1}".format(user, len(cache)))