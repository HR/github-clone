import requests
import re
import sys
import os


recursive = True
base_url = 'https://api.github.com'
# /repos/:owner/:repo/git/trees/:sha?recursive=:bool
tree_endpoint = base_url + '/repos/{}/{}/git/trees/{}?recursive={}'
contents_endpoint = base_url + '/repos/{}/{}/contents'
commits_endpoint = base_url + '/repos/{}/{}/commits'
base_normalize_regex = re.compile(r'.*github\.com\/')


def exit_with_m(m='An error occured'):
    print m
    sys.exit()


def joinp(*args):
    '/'.join(args)


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def fetch_file(req_url, file_path):
    r = requests.get(req_url, stream=True)
    try:
        r.raise_for_status()
    except Exception as e:
        exit_with_m('Failed fetching ' + req_url, e)

    with open(file_path, 'wb') as fd:
        for chunk in req.iter_content(chunk_size=128):
            fd.write(chunk)


def fetch(base_url, path=None):
    """
    Recursively fetch the repo metadata
    """
    req_url = base_url if not path else joinp(base_url, path)
    # Request
    r = requests.get(req_url)

    try:
        r.raise_for_status()
    except Exception as e:
        exit_with_m('Failed fetching repo metdata: ', e)

    repo_data = r.json()

    if isinstance(repo_data, list):
        # Recursively fetch content
        for item in repo_data:
            if item['type'] == 'dir':
                # create dir and then fetch recursively
                print 'Walking dir: %s' % item['path']
                path = joinp(path, item['path'])
                fetch(joinp(base_url, path))
            else:
                # download it
                # Ensure dir directory exists locally
                mkdir_p(path)
                print 'Fetching file: %s' % item['path']


if len(sys.argv) > 1:
    gh_url = sys.argv[1]
else:
    exit_with_m('Nothing to clone :(')

# Normalize & parse input
norm_gh_url = re.sub(base_normalize_regex, '', gh_url)
gh_url_comps = norm_gh_url.split('/')
user, repo = gh_url_comps[:2]
branch = gh_url_comps[3]
path = joinp(gh_url_comps[4:])


api_req_url = contents_endpoint.format(user, repo)

print "Fetching sub repo %s..." % (api_req_url)

fetch(api_req_url, path)
