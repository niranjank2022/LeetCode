def numJewelsInStones(jewels: str, stones: str) -> int:
    hashset = set(jewels)
    count = 0
    for stone in stones:
        if stone in hashset:
            count += 1

    return count
