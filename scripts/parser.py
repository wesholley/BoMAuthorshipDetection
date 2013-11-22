__author__ = 'scott'

BLOCK_MIN_WORD_LIMIT = 200

inf = open('bom.txt', 'r')
output_dir = 'output'
current_author = ''

continue_content = False  # this indicates if we are starting or continuing a block of dialog

author_text_map = {}  # map of authors -> list of strings


def consume_line(line):
    global current_author, continue_content

    if line[0:2] == 'A:':  # change author, author name should be entirety of line
        line = line[2:].strip()  # remove leading whitespace - we don't care about quoting
        current_author = line
        continue_content = False
        return

    if line[0] == '*':  # remove verse number
        i = line.find(' ')
        line = line[i+1:]

    line = line.strip()  # remove extra whitespace at end of line

    if current_author not in author_text_map.keys():
        author_text_map[current_author] = []

    if continue_content:  # continue block of content
        author_text_map[current_author][-1] += ' ' + line
    else:  # start new block of content
        author_text_map[current_author].append(line)

    continue_content = True  # continue this content unless we hit another Author line


def main():

    line = inf.readline()
    while len(line) != 0:
        line = line.strip()

        if len(line) != 0 and line[0] != '#':  # skip comments and whitespace-only lines
            consume_line(line)

        # read next line
        line = inf.readline()

    print('Done reading file')
    total_blocks = 0
    total_authors = 0
    for key in author_text_map.keys():
        total_authors += 1
        total_blocks += len(author_text_map[key])
        print('Number of blocks for %s = %d' % (key, len(author_text_map[key])))
        print('Example: %s' % author_text_map[key][0])
        outf = open(output_dir + '/' + ('%03d' % len(author_text_map[key])) + '-' + key + '.txt', 'w')
        for block in author_text_map[key]:
            outf.write(block)
            outf.write('\n\n')
        outf.close()
    print('Total blocks = %d, Total authors = %d' % (total_blocks, total_authors))


if __name__ == '__main__':
    main()