from random import randint as rand

for _ in xrange(int(raw_input("Enter the times you want the experiment to run: "))):
    alice_ct = alice_guess = rand(0,1)
    bob_ct = rand(0,1); bob_guess = 1 if bob_ct is 0 else 0
    print "Alice's Coin Toss : ", alice_ct, "\tAlice's Guess : ", alice_guess
    print "Bob's Coin Toss   : ", bob_ct, "\tBob's Guess   : ", bob_guess
    print "Saved." if bob_guess is alice_ct or alice_guess is bob_ct else "Doomed."; print "\n"