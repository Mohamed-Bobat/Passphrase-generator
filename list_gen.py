with open('dict.txt', 'r') as infile:
    with open('en_full.txt', 'w') as outfile:
        for lines in infile:
            text = lines.partition(' ')[0]
            if len(text) > 3:
                print(text)
                outfile.write(text+'\n')
            outfile.close
            infile.close
