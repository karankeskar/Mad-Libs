import re

mad_lib="""it was ___(FOOD)___ day at school, and ___(NAME)___ was super ___(ADJECTIVE)___ for lunch.
But when she went outside to eat, a ___(NOUN)___ stole her ___(FOOD)___! ___(NAME)___ chased the ___(NOUN)___ all over school.
She ___(VERB1)___, ___(VERB2)___, and ___(VERB3)___ through the playground.
Then she tripped on her ___(NOUN)___ and the ___(NOUN)___ escaped!
Luckily, ___(NAME)___’s friends were willing to share their ___(FOOD)___ with her."""

def mad_libs(mls):
    hints=re.findall("___.*?___",mad_lib)
    if (hints is not None):
        for word in hints:
            q="Enter a {}".format(word)
            new=input(q)
            mls=mls.replace(word,new,1)
        print("\n")
        mls=mls.replace("\n"," ")
        print(mls)
    else:
        print("invalid")


mad_libs(mad_lib)


