def number_of_lines(df):
        output = f"Number of lines --> {df.count()}"
        return output

def number_of_words(output, df):
    line = 0
    for row in df.collect():
        line = line + 1
        words = row[0].strip().split(' ')
        output = output+"\n----------------------------------------"
        output = output+f"\nNumber of words in line{line}: {len(row[0].strip().split(' '))}"
        for word in words:
            if(len(word)>0):
                if(len(word)%2!=0):
                    mid_word = word[int(len(word)/2)]
                else:
                    mid_word = word[int(len(word)/2)-1]+word[int(len(word)/2)]
            else:
                mid_word = ""
            output = output + f"\n{word} --> middle letter --> {mid_word}"
    print(f"{output}")
    return output

