import requests
import re
import sys


recursive = True
# "https://github.com/HR/Crypter/tree/master/build"
base_url = 'https://api.github.com'
# /repos/:owner/:repo/git/trees/:sha?recursive=:bool
tree_endpoint = base_url + '/repos/{}/{}/git/trees/{}?recursive={}'
contents_endpoint = base_url + '/repos/{}/{}/contents/{}'
commits_endpoint = base_url + '/repos/{}/{}/commits'
base_normalize_regex = re.compile(r'.*github\.com\/')


def exit_with_m(m='An error occured'):
    print m
    sys.exit()


if len(sys.argv) > 1:
    gh_url = sys.argv[1]
else:
    exit_with_m('Nothing to clone :(')

# Normalize & parse input
norm_gh_url = re.sub(base_normalize_regex, '', gh_url)
gh_url_comps = norm_gh_url.split('/')
user, repo = gh_url_comps[:2]
branch = gh_url_comps[3]
path = '/'.join(gh_url_comps[4:])

print "Fetching sub repo %s..." % (api_req_url)

api_req_url = contents_endpoint.format(user, repo, path)

fetch(api_req_url)


def fetch(base_url, path=None):
    """
    Recursively fetch the repo metadata
    """
    req_url = base_url if not path else '/'.join(base_url, path)
    # Request
    r = requests.get(req_url)

    try:
        r.raise_for_status()
    except Exception as e:
        exit_with_m('Failed fetching repo metdata: ', e)

    repo_data = r.json()

    if isinstance(repo_info, list):
        # Recursively fetch content
        for item in repo_data:
            if item.type == 'dir':
                # create dir and then fetch recursively
                fetch()
            else:
                # download it
