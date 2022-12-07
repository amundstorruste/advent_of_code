score_shape = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

score_outcome = {
    "loss" : 0,
    "draw" : 3,
    "win" : 6
}

response_to_win = {
    "A" : "Y",
    "B" : "Z",
    "C" : "X"
}

response_to_loose = {
    "A" : "Z",
    "B" : "X",
    "C" : "Y"
}

def identify_win_loss_draw(opponent, response):
    winning_move = response_to_win[opponent] 
    loosing_move = response_to_loose[opponent]
    if response is winning_move:
        return "win" 
    if response is loosing_move:
        return "loss" 
    return "draw"


with open('puzzle_input.txt') as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        opponent, response = line.split()
        win_loss_draw = identify_win_loss_draw(opponent, response)
        score+=score_outcome[win_loss_draw] + score_shape[response]
    print(f"Task a) {score}")


response_to_draw = {
    "A" : "X",
    "B" : "Y",
    "C" : "Z"
}

planned_outcome = {
    "X" : "loss",
    "Y" : "draw",
    "Z" : "win"
}


def identify_response_from_outcome(opponent, outcome):
    win_loss_draw = planned_outcome[outcome]
    if win_loss_draw == "win":
        return response_to_win[opponent]
    if win_loss_draw == "draw":
        return response_to_draw[opponent]
    return response_to_loose[opponent]


with open('puzzle_input.txt') as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        opponent, outcome = line.split()
        response = identify_response_from_outcome(opponent, outcome)
        win_loss_draw = identify_win_loss_draw(opponent, response)
        score+=score_outcome[win_loss_draw] + score_shape[response]
    print(f"Task b) {score}")
