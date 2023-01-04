def swap_count(input_arr):
   pos = sorted(list(enumerate(input_arr)), key=lambda x: x[1])
   c = 0

   for i in range(len(input_arr)):
      while True:
         if (pos[i][0] == i):
            break
            
         else:
            c += 1
            swap_index = pos[i][0]
            pos[i], pos[swap_index] = pos[swap_index], pos[i]

   return c

def solve(input_arr):
   return min(swap_count(input_arr), swap_count(input_arr[::-1]))

vorodi = input()
print(int(solve(vorodi)/2))