from tqdm import tqdm  as bar
LENGTH = 10 # Number of iterations required to fill pbar

pbar = bar(total=LENGTH) # Init pbar
for i in range(LENGTH):
  pbar.update(n=1) # Increments counter