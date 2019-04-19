import os, sys, glob, argparse, numpy as np, pandas as pd, subprocess, re
from nltk import word_tokenize

'''I removed metavars from R and P because I saw no use of them
and they were causing conflict
'''

#Part 1: Preprocessing

def retrieving_data(filename):
    ''' to do:
            - percentage of set to be used training/test
            - further tokenisation
            - truncation 
    '''
    language_text = []

    with open(filename, encoding ='UTF-8') as f:
        position = 0 #keep track of reading position
        if args.startline:
            print('Starting at line {}.'.format(args.startline))
            for i in range(args.startline): # start at line "startline"
                position += 1
                line = f.readline()
        for line in f:
            position += 1
            line = word_tokenize(line) #tolower?
            language_text.append(line)
            if position == args.endline:
                break

    return language_text

    print('Length of English lines: {}'.format(len(english_lines)))
    print('Length of French lines: {}'.format(len(french_lines)))

def truncate_me(text1, text2):
    '''Zip languages together --Lin
    this returns a list of tuples that is the french/english line
    i have truncated it, i don't know if you think there is a better way to output 
    this bit? --Rob
    '''
    twin_lines = []
    for i in range(len(text1)):
        lens = [len(text1[i]), len(text2[i])]
        print(lens)
        twin_lines.append((text1[i][:min(lens)],text2[i][:min(lens)]))
        #print(len(twin_lines[i][0]), len(twin_lines[i][1])) #testing that it worked
    return twin_lines 

def feed_forward():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert text to features")
    parser.add_argument("-S", "--start", metavar="S", dest="startline", type=int,
                    default=0,
                    help="What line of the input data file to start from. Default is 0, the first line.")
    parser.add_argument("-E", "--end", metavar="E", dest="endline",
                    type=int, default=100,
                    help="What line of the input data file to end on. Default is None, whatever the last line is.")
    parser.add_argument("-T", "--test", metavar="T", dest="test_range",
                    type=int, default=20, help="What percentage of the set will be test")
    parser.add_argument("-R", "--random", dest="random", action="store_true", default=False, help="Specify whether to get random training/test")
    parser.add_argument("-P", "--preprocessing", dest="prepro", action="store_true", default=False,
                        help="specifies whether or not to use preprocessing")
    args = parser.parse_args()

    english_lines = retrieving_data('english_slice.txt')
    french_lines = retrieving_data('french_slice.txt')
    truncate_me(english_lines,french_lines)