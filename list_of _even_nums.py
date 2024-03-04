def list_of_even_nums(x):
     even_nums = list(filter(lambda num: num % 2 == 0 , x))
     return even_nums
    
if __name__ == "__main__":
   list_input= (input("enter the list of number :"))
   x = list(map(int, list_input.split()))
   even = list_of_even_nums(x)
   print("list of even numbers......................")
   print(even)