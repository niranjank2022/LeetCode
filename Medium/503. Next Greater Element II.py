def nextGreaterElements(nums: list[int]) -> list[int]:
    mono_stack = []

    for val in nums:

        while mono_stack and val <= mono_stack[-1]:
            mono_stack.pop()

