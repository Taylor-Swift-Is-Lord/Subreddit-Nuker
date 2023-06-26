lines_seen = set() # holds lines already seen
outfile = open("Tumblr_Users_ND.txt", "w")
for line in open("Tumblr_Users.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()