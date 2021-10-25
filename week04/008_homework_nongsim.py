# Q. 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다.
# 원래 밀가루를 공급받던 공장의 고장으로 앞으로 k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.
# 해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고,
# 라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.
# 현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies),
# 원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때,
# 밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 반환 하시오.
# dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.
# 다음과 같이 입력값이 들어온다면,
# 현재 재고가 4개 있습니다. 그리고 정상적으로 돌아오는 날은 30일까지입니다.
# 즉, 26개의 공급량을 사와야 합니다!
# 그러면 제일 최소한으로 26개를 가져오려면? supplies 에서 20, 10 을 가져오면 되겠죠?
# 그래서 이 경우의 최소 공급 횟수는 2 입니다!
# supplies = [20, 15, 10]
# 이 때! 다음과 같이 입력값이 들어온다면 어떻게 해야 할까요?
# supplies 에서 20, 15를 가져오는게 가장 최고의 상황입니다!
# 즉, 4일과 10일에 공급량을 가져오는 게 좋습니다!
import heapq


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    imported_count = 0  # 총 수입한 횟수
    last_imported_index = 0  # 마지막 수입품이 들어온 인덱스
    max_heap = []  # 최댓값 힙이기 때문에 마이너스로 계산해야 함

    while stock <= k:  # 재고량이 남은 날짜 수보다 적으면 공장이 멈춘다.
        # 인덱스가 수급 가능한 남은 날짜 안에 더 수입할 수 있는 상태라면,
        # 공장이 멈추지 않는 선에서 가능한 공급 물량 중에서 가장 큰 값 (중복 없이)을 탐색한다.
        while last_imported_index < len(dates) and dates[last_imported_index] <= stock:
            heapq.heappush(max_heap, -supplies[last_imported_index])  # 최대값 힙을 유지하기 위해 뺄셈으로 계산
            last_imported_index += 1  # 수입을 한번 실행했으므로 인덱스 +1
        imported_count += 1  # 수입한 횟수도 +1
        heap_pop = heapq.heappop(max_heap)  # 절대값이 가장 큰 값을 리턴함
        stock += -heap_pop  # 현재 물량에 수입받은 물량을 추가함
    return imported_count  # 총 수입한 횟수


print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))