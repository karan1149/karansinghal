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

parser = argparse.ArgumentParser(description='Publishes a Hugo site with a given commit message.')
parser.add_argument('--m', default='Publish changes to site.',
                    help='Commit message for publish.')

args = parser.parse_args()

expected_dirs = ['themes/', 'content/', 'docs/']

for expected_dir in expected_dirs:
	assert os.path.isdir(expected_dir), 'Make sure you are in the root directory of the Hugo site.'

kt.run_command("mv docs/CNAME .")

kt.run_command("rm -rf docs/")

kt.run_command("hugo")

kt.run_command("mv CNAME docs/")

kt.run_command("git reset")

kt.run_command("git add docs/")

kt.run_command('git commit -m "%s"' % args.m)

kt.run_command('git push')