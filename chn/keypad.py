def solution(numbers, hand):
    _dict = {'1':{'2': 1, '5': 2, '8': 3, '0': 4},
             '2':{'2': 0, '5': 1, '8': 2, '0': 3},
             '3':{'2': 1, '5': 2, '8': 3, '0': 4},
             '4':{'2': 2, '5': 1, '8': 2, '0': 3},
             '5':{'2': 1, '5': 0, '8': 1, '0': 2},
             '6':{'2': 2, '5': 1, '8': 2, '0': 3},
             '7':{'2': 3, '5': 2, '8': 1, '0': 2},
             '8':{'2': 2, '5': 1, '8': 0, '0': 1},
             '9':{'2': 3, '5': 2, '8': 1, '0': 2},
             '0':{'2': 3, '5': 2, '8': 1, '0': 0},
             '*':{'2': 4, '5': 3, '8': 2, '0': 1},
             '#':{'2': 4, '5': 3, '8': 2, '0': 1}
            }
    answer = ''
    _right_hand = '#'
    _left_hand = '*'
    for i in numbers:
        if i in [1,4,7]:
            _left_hand = str(i)
            answer += "L"
        elif i in [3,6,9]:
            _right_hand = str(i)
            answer += "R"
        else:
            if _dict[_right_hand][str(i)] > _dict[_left_hand][str(i)]:
                _left_hand = str(i)
                answer += "L"
            elif _dict[_right_hand][str(i)] < _dict[_left_hand][str(i)]:
                _right_hand = str(i)
                answer += "R"
            else:
                if hand == "right":
                    _right_hand = str(i)
                    answer += "R"
                else:
                    _left_hand = str(i)
                    answer += "L"
            
    return answer