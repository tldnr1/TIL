# round(값, 반올림위치) : 반올림, 단 자동으로 소수점 줄어들 수 있음 (1.000 => 1.0)
# format(값, 반올림 틀) : 반올림 틀('.2f' 등)에 무조건 맞춰서 출력

f1 = 10.0
f2 = 0.01

print(round(f1/f2, 3))
print(format(f1/f2, '.3f'))
print('{0:.3f}'.format(f1/f2))
# {}에 format 값이 대응됨
# {} 안에 0: 은 슬라이싱 즉, 앞에서 자릿수 자르는거
# {} 안에 .3f는 지정형식
# ,.3f 로 고치면 1,000.000으로 출력이 바뀜