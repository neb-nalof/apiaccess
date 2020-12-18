from github import Github

token = "put a token here"
g = Github(token)

for repo in g.get_user().get_repos():
    print(repo.name)
    branches = list(repo.get_branches())
    print(branches)


