name_string = "이사부,장보고,대조영,강감찬,문익점,이순신,김두한,이율곡,이퇴계,이사부,장보고,문익점,이순신,김두한,이율곡,이순신,김두한,이율곡,김정민"
names = name_string.split(",")

kim = 0
lee = 0
dedupe_kim = 0
dedupe_lee = 0
lee_soon_shin = 0
dedupe = set(names)
for name in names:
    if name.startswith("김"):
        kim += 1
    elif name.startswith("이"):
        lee += 1
        if name == "이순신":
            lee_soon_shin += 1
for name in dedupe:
    if name.startswith("김"):
        dedupe_kim += 1
    elif name.startswith("이"):
        dedupe_lee += 1
print(f"문제4-1: 김씨와 이씨는 각각 몇 명인가요? 김씨: {kim}명, 이씨: {lee}명")
print(f"\t 김씨와 이씨는 각각 몇 명인가요? (중복 없이) 김씨: {dedupe_kim}명, 이씨: {dedupe_lee}명")
print("\t 중복된 이름에 대해 별개의 인물로 인식하는지에 대해 다소 다툼의 여지가 있어 두개의 답을 제시합니다.")
print(f'문제4-2: "이순신"이라는 이름은 몇 번 반복 되나요? {lee_soon_shin}번 반복됩니다.')
print(f"문제4-3: 중복을 제거한 이름을 출력하세요. {', '.join(dedupe)}")
print(f"문제4-4: 중복을 제거한 이름을 내림차순으로 정렬하여 출력하세요. {', '.join(sorted(dedupe, reverse=True))}")
