import csv

def analyze(entries):
    print(f'first entry: {entries[0]}')

with open("reddit_vm.csv", "r", encoding='UTF-8', errors="ignore") as input:
    entries = [(e['id'], int(e['score']), int(e['comms_num']), e['title']) for e in csv.DictReader(input)]
    avgScore = analyze(entries)

def findAvgComments():
    sum_comments = 0
    for comms in entries:
        sum_comments += comms[2]
    return("Average comments per post: " + str(round(sum_comments/len(entries), 2)))

def findAvgScore():
    sum_score = 0
    for scores in entries:
        sum_score += scores[1]
    return("Average score: " + str(round(sum_score/len(entries), 2)))
def findMaxScore():
    curr_score = 0
    highest_score = 0
    highest_score_title = ''
    for scores in entries:
        curr_score = scores[1]
        if curr_score > highest_score:
            highest_score = curr_score
            highest_score_title = scores[3]
    return("Highest score: " + str(highest_score) + ", title: " + highest_score_title)

def findMinScore():
    curr_score = 0
    lowest_score = 0
    lowest_score_title = ''
    for scores in entries:
        curr_score = scores[1]
        if curr_score < lowest_score:
            lowest_score = curr_score
            lowest_score_title = scores[3]
    return("Lowest score: " + str(lowest_score) + ", title: " + lowest_score_title)

def findMaxComments():
    curr_comment_num = 0
    highest_comment_num = 0
    highest_comment_num_title = ''
    for comms in entries:
        curr_comment_num = comms[2]
        if curr_comment_num > highest_comment_num:
            highest_comment_num = curr_comment_num
            highest_comment_num_title = comms[3]
    return("Highest number of comments: " + str(highest_comment_num) + ", title: " + highest_comment_num_title)

print(findAvgComments())
print(findAvgScore())
print(findMaxScore())
print(findMinScore())
print(findMaxComments())
