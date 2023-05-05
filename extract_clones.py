import re
  
input_file = 'requirements.txt'
output_file = 'clone_repos.sh'

git_url_pattern = re.compile(r'^(.+)\s@\s+git\+(.+)$')

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    outfile.write('#!/bin/sh\n\n')
    outfile.write('mkdir -p cloned_repos\n\n')

    for line in infile:
        match = git_url_pattern.match(line.strip())

        if match:
            #branch = match.group(1)
            repo_url = match.group(2)
            repo_name = repo_url.split('/')[-1].split('.')[0]

            outfile.write(f'git clone {repo_url} cloned_repos/{repo_name}\n')

print(f'Shell script to clone repositories has been generated: {output_file}')
