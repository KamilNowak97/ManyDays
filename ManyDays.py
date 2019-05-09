import datetime

dateStart = input("Write start date in  YYYY MM DD format: ").split()
dateEnd = input("Write end date in  YYYY MM DD format: ").split()

result = datetime.date(int(dateEnd[0]),int(dateEnd[1]),int(dateEnd[2])) - datetime.date(int(dateStart[0]),int(dateStart[1]),int(dateStart[2]))

print(result.days, " days left")



