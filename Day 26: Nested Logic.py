# Enter your code here. Read input from STDIN. Print output to STDOUT
issue_date =  list(map(int, input().split()))
sday, smonth, syear = issue_date[0], issue_date[1], issue_date[2]
submit_date = list(map(int, input().split()))
iday, imonth, iyear = submit_date[0], submit_date[1], submit_date[2]
fine = 0

if syear > iyear: 
    print(10000)
elif syear == iyear and smonth > imonth: 
    print((smonth-imonth)*500)
elif syear == iyear and smonth == imonth and sday > iday: 
    print((sday-iday)*15)
else: 
    print(0)
