
#if문 몸무게 측정


a = int(input("몸무게 입력:"))

if a <= 59:
      print("정상")
elif a >= 60 and a <= 70:
      print("비만")
elif a >= 71:
      print("고도비만")
