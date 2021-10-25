from collections import deque


class StationNode:
    """간단한 지하철 역 노드 클래스"""
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []
        self.visited = False
        self.predecessor = None

    def add_connection(self, other_station):
        """지하철 역 노드 사이 엣지 저장하기"""
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)

    def __str__(self):
        """지하철 노드 문자열 메소드. 지하철 역 이름과 연결된 역들을 모두 출력해준다"""
        res_str = f"{self.station_name}: "  # 리턴할 문자열

        # 리턴할 문자열에 인접한 역 이름들 저장
        for _station in self.adjacent_stations:
            res_str += f"{_station.station_name} "

        return res_str


def create_subway_graph(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프를 리턴하는 함수"""
    _stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file 파일을 연다
    with open(input_file, encoding="UTF-8") as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            previous_station = None  # 엣지를 저장하기 위한 도우미 변수. 현재 보고 있는 역 전 역을 저장한다
            subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

            for name in subway_line:
                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                # 지하철 역 이름이 이미 저장한 key 인지 확인
                if station_name not in _stations:
                    current_station = StationNode(station_name)  # 새로운 인스턴스를 생성하고
                    _stations[station_name] = current_station  # dictionary에 역 이름은 key로, 역 인스턴스를 value로 저장한다

                else:
                    current_station = _stations[station_name]  # 이미 저장한 역이면 stations에서 역 인스턴스를 갖고 온다

                if previous_station:
                    current_station.add_connection(previous_station)  # 현재 역과 전 역의 엣지를 연결한다

                previous_station = current_station  # 현재 역을 전 역으로 저장

    return _stations


def bfs(graph, start_node):
    """시작 노드에서 bfs를 실행하는 함수"""
    queue = deque()  # 빈 큐 생성

    # 모든 노드를 방문하지 않은 노드로 표시
    for station_node in graph.values():
        station_node.visited = False
        station_node.predecessor = None

    # 시작점 노드를 방문 표시한 후 큐에 넣어준다
    start_node.visited = True
    queue.append(start_node)

    while queue:  # 큐에 노드가 있는 동안
        current_station = queue.popleft()  # 큐의 가장 앞 데이터를 갖고 온다
        for neighbor in current_station.adjacent_stations:  # 인접한 노드를 돌면서
            if not neighbor.visited:  # 방문하지 않은 노드면
                neighbor.visited = True  # 방문 표시를 하고
                neighbor.predecessor = current_station
                queue.append(neighbor)  # 큐에 넣는다


def back_track(destination_node):
    """최단 경로를 찾기 위한 back tracking 함수"""
    res_str = ""  # 리턴할 결과 문자열
    temp = destination_node  #  도착 노드에서 시작 노드까지 찾아가는 데 사용할 변수

    # 시작 노드까지 갈 때까지
    while temp is not None:
        res_str = f"{temp.station_name} {res_str}"  # 결과 문자열에 역 이름을 더하고
        temp = temp.predecessor  # temp를 다음 노드로 바꿔준다

    return  res_str

def back_track_reculsive(destination_node):
    """최단 경로를 찾기 위한 back tracking 재귀함수"""
    res_str = destination_node.station_name
    if destination_node.predecessor is None:
        return res_str
    return f"{back_track_reculsive(destination_node.predecessor)} {res_str}"


def dfs(graph, start_node):
    """시작 노드에서 dfs를 실행하는 함수"""
    stack = deque()  # 빈 스택 생성

    # 모든 노드를 처음 보는 노드로 초기화
    for station_node in graph.values():
        station_node.visited = False

    # 시작점 노드를 방문 표시한 후 스택에 넣어준다
    start_node.visited = True
    stack.append(start_node)

    while stack:  # 스택에 노드가 있는 동안
        current_station = stack.pop()  # 스택의 가장 뒤 데이터를 갖고 온다
        current_station.visited = True
        for neighbor in current_station.adjacent_stations:  # 인접한 노드를 돌면서
            if not neighbor.visited:  # 방문하지 않은 노드면
                neighbor.visited = True  # 방문 표시를 하고
                stack.append(neighbor)  # 스택에 넣는다


stations = create_subway_graph("./stations.txt")  # stations.txt 파일로 그래프를 만든다

# stations에 저장한 역 인접 역들 출력 (채점을 위해 역 이름 순서대로 출력)
bfs(stations, stations["상봉"])  # 지하철 그래프에서 을지로3가역을 시작 노드로 bfs 실행
print(back_track_reculsive(stations["양재시민의숲"]))  # 을지로3가에서 강동구청역까지 최단 경로 출력

