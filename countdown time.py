import time
def countdown(t):
    while t>0:
        print (t)
        t= t-1
        time.sleep(1)
    print ("Time's Up Mate ッ")
print("How many second to countdown? Enter an Integer.")
seconds = input()
while not seconds.isdigit():
    print ("Opps !! ⍨ it was found that it wasn't an Integer number! Please Enter an Integer number")
    seconds = input ()
seconds = int(seconds)
countdown(seconds)
