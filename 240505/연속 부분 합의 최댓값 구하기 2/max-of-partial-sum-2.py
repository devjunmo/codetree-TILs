def max_subarray_sum(nums):
    max_ending_here = nums[0]
    max_so_far = nums[0]
    
    for num in nums[1:]:
        max_ending_here = max(max_ending_here + num, num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# 입력을 받는 코드
n = int(input().strip())  # 원소의 개수 입력 받기
nums = list(map(int, input().strip().split()))  # 공백으로 구분된 정수들을 입력 받아 리스트로 변환

# 최대 부분 배열 합 계산 및 출력
print(max_subarray_sum(nums))