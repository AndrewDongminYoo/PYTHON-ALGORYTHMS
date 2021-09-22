def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    total_play = dict()
    play_list_dict = dict()
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in total_play:
            total_play[genre] = play
            play_list_dict[genre] = [[i, play]]
        else:
            total_play[genre] += play
            play_list_dict[genre].append([i, play])

    total_play_items = sorted(total_play.items(), key=(lambda x: x[1]), reverse=True)
    result = list()
    for genre, _ in total_play_items:
        index_play_array = play_list_dict[genre]
        index_play_array = sorted(index_play_array, key=(lambda x: x[1]), reverse=True)
        for i in range(len(index_play_array)):
            if i > 1:
                break
            result.append(index_play_array[i][0])
    return result


if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(genres, plays))
    print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))
