batting_input = raw_input("Candidate does good batting. Y/N : ")
bowling_input = raw_input("Candidate does good bowling. Y/N : ")


batting = False
if(batting_input == 'Y'):
    print("Batting is good.")
    batting = True
else:
    print("Batting is not good.")

bowling = False
if(bowling_input == 'Y'):
    print("Bowling is good.")
    bowling = True
else:
    print("Bowling is not good.")

if(batting or bowling):
    print("Candidate is Selcted.");
else:
    print("Candidate is Rejected.");

