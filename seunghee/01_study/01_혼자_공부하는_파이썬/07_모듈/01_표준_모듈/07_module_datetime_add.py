# 모듈을 읽어 들입니다.
import datetime
now = datetime.datetime.now()

# 특정 시간 이후의 시간 구하기
print("# datetime.dimedelta로 시간 더하기")
after = now + datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)

time_format = "%Y년 %m월 %d일 %H시 %M분 %S초"
print(after.strftime(time_format))
print()

print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year + 1))
print(output.strftime(time_format))