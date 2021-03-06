'''build-libs.py
Runs the build process for all of the libraries in this directory
in a cross-platform safe way.
'''

import os
import subprocess

base_path = os.path.abspath(os.path.dirname(__file__))

def run(command):
	subprocess.run(command, check=True)

# Build steps
def assetChecksum():
	os.chdir(os.path.join(base_path, 'asset-checksum'))
	run(('cargo', 'build', '--release', '--verbose'))
	run(('wasm-pack', 'build', '--release'))
	os.chdir(base_path)

def fend():
    os.chdir(os.path.join(base_path, 'fend-wasm'))
    run(('cargo', 'update'))
    run(('cargo', 'build', '--release', '--verbose'))
    run(('wasm-pack', 'build', '--release'))
    os.chdir(base_path)

build_steps = {
    'asset-checksum': assetChecksum,
    'fend-wasm': fend
}

# Actually run the builds
print('👷 Building libraries:')
for name, builder in build_steps.items():
	print(f'\t{name}...')
	builder()
	print(f'\t{name} ✔️')

print('Done! 🎉')
