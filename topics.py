"""Topics.py
設計一個函數，輸入為數字，輸出則為*符號為輸入數字邊長的空心正三角形。
輸入: 3
輸出：
      *
     * *
    * * *  
"""

def print_hollow_triangle(size):

  if size <= 0:
    print("邊長必須是正整數。")
    return

  # Top row
  print(" " * (size - 1) + "*")

  # Middle rows
  for i in range(2, size):
    spaces_before = size - i
    spaces_inside = (i - 2) * 2 + 1
    print(" " * spaces_before + "*" + " " * spaces_inside + "*")

  # Bottom row
  if size > 1:
    print("* " * (size - 1) + "*")

#print_hollow_triangle(3)

size = int(input("Triangle size? "))
print_hollow_triangle(size)
