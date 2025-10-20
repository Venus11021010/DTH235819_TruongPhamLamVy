# Câu 10: Vẽ hình dùng Sleep
# Yêu cầu:
# Vẽ 4 hình dưới đây, dùng sleep để xuất hiện từng hình sau 5 giây

# import turtle
# import time

import time
import os

# 4 hình dạng bằng chuỗi nhiều dòng
shape1 = r"""
      *
      * *
      * * *
* * * * * * *
* * *
* *
*
"""

shape2 = r"""
      *
      * *
      *   *
* * * * * * *
*   *
* *
*
"""

shape3 = r"""
      * * * *
      * * * 
      * *
      *
    * *
  * * * 
* * * * 
"""

shape4 = r"""
      * * * *
      *   * 
      * *
      *
    * *
  *   * 
* * * * 
"""

shapes = [shape1, shape2, shape3, shape4]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

for i, s in enumerate(shapes, start=1):
    clear_screen()
    print(f"HÌNH {i}:\n")
    print(s)
    # hiện 5 giây rồi chuyển sang hình tiếp
    time.sleep(5)

# kết thúc: giữ màn hình cuối cùng (tùy chọn)
print("\nHoàn thành.")



