import numpy
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        grid_arr = numpy.array(grid)
        grid_arr_tr = grid_arr.transpose()
        
        skyline_lr = []
        skyline_tb = []
        
        for arr in grid_arr:
            skyline_lr.append(max(arr))
        for arr in grid_arr_tr:
            skyline_tb.append(max(arr))
        
        # print(skyline_lr, skyline_tb)
        total = 0
        
        for i in range(len(grid_arr)):
            for j in range(len(grid_arr)):
                min_height = min(skyline_tb[j],skyline_lr[i])
                total += min_height - grid_arr[i][j]
        return total
        
        
        
