'''
Publishes a Hugo site to GitHub. Assumes GitHub Pages has already been set up,
and the publishDir = "docs" (found in config.toml). Must be run from root Hugo
directory (the script checks this). Note that the script only commits changes
to the docs/ directory–any other changes need to be committed normally.

Usage examples:
python publish.py # Use the default commit message
python publish.py --m "My publish commit message"
'''
import karantools as kt
import os

import argparse
from update_notebooks import update_notebooks

def remove_docs_from_gitignore():
	if os.path.isfile('.gitignore'):
		with open('.gitignore', 'r') as f:
			lines = f.readlines()
		if 'docs/\n' in lines:
			kt.print_bold('Removing "docs/" from .gitignore')
			lines.remove('docs/\n')
			with open('.gitignore', 'w') as f:
				f.writelines(lines)
			return True
		else:
			kt.print_bold('"docs/" not found in .gitignore')
	return False

def add_docs_to_gitignore():
	if os.path.isfile('.gitignore'):
		with open('.gitignore', 'r') as f:
			lines = f.readlines()
		if 'docs/\n' not in lines:
			kt.print_bold('Adding "docs/" back to .gitignore')
			with open('.gitignore', 'a') as f:
				f.write('docs/\n')

def main():
	parser = argparse.ArgumentParser(description='Publishes a Hugo site with a given commit message.')
	parser.add_argument('--m', default='Publish changes to site.',
	                    help='Commit message for publish.')

	args = parser.parse_args()

	expected_dirs = ['themes/', 'content/', 'docs/']

	for expected_dir in expected_dirs:
		assert os.path.isdir(expected_dir), 'Make sure you are in the root directory of the Hugo site.'

	## Notebook processing. ###

	kt.run_command("python3 -m nbconvert --to markdown notebooks/*.ipynb --output-dir=notebooks/outputs/")

	kt.print_bold('\nUpdating notebooks...')
	update_notebooks('content', 'notebooks/outputs')

	## End notebook processing. ###

	# Remove docs/ from .gitignore if it exists
	removed_from_gitignore = remove_docs_from_gitignore()

	kt.run_command("mv docs/CNAME .")

	kt.run_command("rm -rf docs/")

	kt.run_command("hugo")

	kt.run_command("mv CNAME docs/")

	kt.run_command("git reset")

	kt.run_command("git add docs/")

	kt.run_command("git status")

	kt.run_command('git commit -m "%s"' % args.m)

	kt.run_command('git push')

	# Add docs/ back to .gitignore if it was removed earlier
	if removed_from_gitignore:
		add_docs_to_gitignore()


if __name__=='__main__':
	main()
