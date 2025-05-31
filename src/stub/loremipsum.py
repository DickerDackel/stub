from importlib.resources import files

ASSETS = files('stub.assets')

fname = ASSETS.joinpath('lipsum.txt')
with open(fname) as f:
    loremipsum = f.read()
