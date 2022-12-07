def repeat(s: list) -> bool:
    for c in s:
        if s.count(c) > 1:
            return True
    return False


def findMarker(s: str, length: int) -> int:
    for i in range(len(s)-length+1):
        if not repeat(s[i:i+length]):
            return length+i

for l in open("./day6/input", "r").readlines():
    l = l.strip()
    print(f"Markers: {findMarker(l, 4)}")