import bz2 as b


f = b.BZ2File('enwiki-20080103.main.bz2','r')
user_edits = b.BZ2File('user_edits.main.bz2','w')
article_info = b.BZ2File('article_info.main.bz2','w')

BIG_COUNT = 100000 #number of edits we want from data
SET_COUNT = 13 
curr_big = 0 #current edit number

while curr_big <= BIG_COUNT:
    little_count = 0
    article_line = ""
    edit_line = ""
    add = True
    while True:
        curr_line = f.readline()
        line_arr = curr_line.split()
        if len(line_arr) > 0 and line_arr[0] == "REVISION":
            #article_line += line_arr[2] + "," #rev id 
            article_line += line_arr[1] + ";" #article_id
            article_line += line_arr[3] + ";" #article_title
            edit_line = ";".join([line_arr[6],line_arr[5],line_arr[1]])
        elif len(line_arr) > 0 and line_arr[0] == "CATEGORY":
            if len(line_arr) == 1:
                add = False
                continue
            article_line += "|".join(line_arr[1:]) #categories article    
        elif line_arr == []:
            if add == True:
                user_edits.write(edit_line + "\n") 
                article_info.write(article_line + "\n")
                curr_big += 1
            break    
        else:
            pass
       
f.close()
user_edits.close()
article_info.close()
