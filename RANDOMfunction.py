import random
name=["Akash","bubly","nikhil","nitesh","gaurav","alisha"]
team = " alisa,arsod,abhi,asam,aniu,atul "
j='|'
print(random.choice(name))
print(random.randrange(1,10))
random.shuffle(name)
print(name)
print(j.join(name))
print(len(name))
print(team.split(','))