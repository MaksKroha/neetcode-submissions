class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)


        def backtracking(curr_arr, summa, idx):
            if summa == target:
                result.append(curr_arr.copy())
                return

            if idx == len(candidates):
                return 

            counter = idx
            while counter < len(candidates):
                if counter == 0 or not candidates[counter] == candidates[counter - 1] or counter == idx:
                    new_summa = summa + candidates[counter]

                    if new_summa > target:
                        return

                    curr_arr.append(candidates[counter])
                    backtracking(curr_arr, new_summa, counter+1)
                    curr_arr.pop()
                counter += 1
        backtracking([], 0, 0)
        return result
                

        