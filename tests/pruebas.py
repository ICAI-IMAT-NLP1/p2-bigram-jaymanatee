lines = ["hello mister 1 2", "world 3 4"]
start_token = "S"
end_token = "E"


names = [start_token + " ".join(word.lower().split()[:-2]) + end_token for word in lines]
bigrams = [(name[i], name[i+1]) for name in names for i in range(len(name)-1)]
 

print(bigrams)