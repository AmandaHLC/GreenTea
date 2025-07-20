"""
(2) 國泰國中的老師出了一道題目給同學們練習，同學們自己設定一串奇偶混和地亂數，
並將數字依照” 奇數都在偶數前面”，且”偶數升冪排序”，”奇數降冪排序”。
例如 ‘417324689435’ 將會變成 ‘975331244468’。然而，班上有50位學生，每一個同學給出的數字長度不一，
老師希望能用一段小程式來幫助他驗證答案，請寫一個函數幫幫老師吧!
"""
def sort_odd_even(number_string):

  odd_digits = []
  even_digits = []

  for digit in number_string:
    num = int(digit)
    if num % 2 == 0:
      even_digits.append(num)
    else:
      odd_digits.append(num)

  # Sort odd digits in descending order
  odd_digits.sort(reverse=True)

  # Sort even digits in ascending order
  even_digits.sort()

  # Concatenate the sorted lists and convert back to a string
  sorted_digits = odd_digits + even_digits
  return "".join(map(str, sorted_digits))


number_string = input("Input Number? ")
print(sort_odd_even(number_string))