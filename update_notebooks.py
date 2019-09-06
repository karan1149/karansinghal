import os
import karantools as kt


def update_notebooks(docs_path, notebook_path, extensions=['.md'], recursion_depth=0):
	assert os.path.isdir(docs_path)
	assert os.path.isdir(notebook_path)

	print("  " * recursion_depth + "%s" % docs_path)
	docs_files = [name for name in os.listdir(docs_path) if any(name.endswith(ext) for ext in extensions)]

	for doc_file in docs_files:
		doc_path = os.path.join(docs_path, doc_file)
		changed = False
		with open(doc_path, 'r') as r:
			with open(doc_path + '_phtemp', 'w') as w:
				for line in r:
					if not line.startswith("{{< notebook "):
						if not line.startswith('<!-- Notebook Start -->'):
							w.write(line)
							continue
						else:
							while '<!-- Notebook End -->' not in next(r):
								pass
							continue
					
					w.write(line.strip() + '\n\n<!-- Notebook Start -->\n\n')
					changed = True
					notebook_tag_chunks = line[13:].strip().split('"')
					kt.assert_eq(len(notebook_tag_chunks), 3)

					notebook_file_path = os.path.join(notebook_path, notebook_tag_chunks[1].replace('ipynb', 'md'))

					with open(notebook_file_path, 'r') as n:
						even = True
						for n_line in n:
							if n_line == '```\n':
								n_line = '```python\n' if even else n_line
								even = not even
							
							w.write(n_line)

					w.write('<!-- Notebook End -->\n')

		os.remove(doc_path)
		os.rename(doc_path + '_phtemp', doc_path)

		if changed:
			kt.print_bold("  " * recursion_depth + "  %s" % doc_file)
		else:
			print("  " * recursion_depth + "  %s" % doc_file)

	doc_folder_paths = [os.path.join(docs_path, name) for name in os.listdir(docs_path) if os.path.isdir(os.path.join(docs_path, name))]

	for doc_folder_path in doc_folder_paths:
		update_notebooks(doc_folder_path, notebook_path, extensions, recursion_depth=(recursion_depth + 1))

if __name__=="__main__":
	expected_dirs = ['themes/', 'content/', 'docs/']

	for expected_dir in expected_dirs:
		assert os.path.isdir(expected_dir), 'Make sure you are in the root directory of the Hugo site.'

	## Notebook processing. ###

	kt.run_command("jupyter nbconvert --to markdown notebooks/*.ipynb --output-dir=notebooks/outputs/")

	kt.print_bold('\nUpdating notebooks...')
	update_notebooks('content', 'notebooks/outputs')

	## End notebook processing. ###
