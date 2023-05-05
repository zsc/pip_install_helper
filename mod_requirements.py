import re
  
input_file = 'requirements.txt'
output_file = 'requirements_local.txt'

git_url_pattern = re.compile(r'^(.+)\s@\s+git\+(.+)$')

def convert_to_local_path(line):
    match = git_url_pattern.match(line.strip())

    if match:
        branch = match.group(1)
        repo_url = match.group(2)
        repo_name = repo_url.split('/')[-1].split('.')[0]

        return f'-e file:/data/cloned_repos/{repo_name}#egg={repo_name}\n'
    else:
        return line

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        outfile.write(convert_to_local_path(line))

print(f'Local file path version of requirements has been generated: {output_file}')
