s1 = input("maatn krting: ")
print(f"oldingi: {s1}")
print(f"yangisi: {s1.lower()}")


s2_1, s2_2 = input("1 - soz krting: "), input("2 - soz krting: ")
print(f"oldingisi: ({s2_1}), ({s2_2})")
print(f"yangisi: {s2_1.join("[]")}, {s2_2.join("[]")}")

s3 = input("email manzil krting: ")
if "@" in s3 and "." in s3 and not s3[-1] == ".":
    print(f"togri email: {s3}")
else:
    print(f"NOtogri email: {s3}")
  

s4 = input("matn kirting: ")
s4_res = set(s4)
print(f"eskisi: {s4}")
s4 = str(s4_res)
print(f"yangisi: {s4}")


s5_1, s5_2 = input("soz1 krtiing: "), input("soz2 kirting: ")

s5_res1, s5_res2 = s5_1.capitalize(), s5_2.capitalize()

if s5_res1 == s5_res2:
    print(f"Palindrom bular: {s5_res1}, {s5_res2}")
else:
    print(f"Palindrom emas: {s5_res1}, {s5_res2}")
  

s6 = input("MATN krting: ")
s6_r1 = s6.count(" ")
s6_r1_t1 = s6.count("")
print(f"eng kopi: {s6_r1_t1}, va sozlar soni: {s6_r1+1}")


s7 = input("Son kiriting: ")
res = ""

for i in range(0, len(s7), 3):
    res += s7[i:i+3] + "-"

print(res.rstrip("-"))
