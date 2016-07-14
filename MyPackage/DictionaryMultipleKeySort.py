from operator import itemgetter

stocks = [
          {'fname':'Bucky','lname':'Roberts'},
          {'fname':'Tommy','lname':'Williams'},
          {'fname':'Tommy','lname':'Roberts'},
          {'fname':'Nick','lname':'Sandey'},
          {'fname':'Tommy','lname':'Vincent'},
          {'fname':'Bucky','lname':'Sandey'},
          {'fname':'Bucky','lname':'Williams'},
          ]
for x in sorted(stocks, key=itemgetter('fname')):
    print(x)

print('-----------')

for x in sorted(stocks, key=itemgetter('fname','lname')):
    print(x)