width = float(input("가로:"))

length = float(input("세로:"))

height = float(input("높이:"))

volume = width*length*height
print("박스의 부피는", volume, "입니다.")

 # %% 거리에 따른 박스의 요금 
  
total_length = length + width + height

if total_length <= 80: 
    charge = 5000 
elif total_length <= 100: 
    charge = 8000 
elif total_length <= 120: 
    charge = 10000 
elif total_length <= 160 : 
    charge = 13000 
else: 
    charge = "unavailable"
    
print("Total length:", total_length)
print("Charge:", charge)
