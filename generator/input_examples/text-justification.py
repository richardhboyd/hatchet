def fullJustify(words, maxWidth):
    
    lines = []
    
    # current line words
    curr_line_words = []
    
    # current line length 
    curr_line_len = 0
    
    for word in words:
        
        # check if adding current word exceeds maxWidth
        if curr_line_len + len(word) + len(curr_line_words) > maxWidth:
            
            # add current line to lines array
            lines.append(justify(curr_line_words, maxWidth, False))
            
            # reset curr_line_words and curr_line_len
            curr_line_words = []
            curr_line_len = 0
            
        # add word to current line    
        curr_line_words.append(word)
        curr_line_len += len(word)
        
    # add last line    
    lines.append(justify(curr_line_words, maxWidth, True))
    
    return lines
    
            
def justify(words, maxWidth, is_last_line):

    num_words = len(words)
    num_spaces = maxWidth - sum(len(word) for word in words)
    
    if num_words == 1 or is_last_line: 
        # if one word or last line, left justify
        return words[0] + ' ' * num_spaces
    
    spaces_between_words = num_spaces // (num_words - 1)
    extra_spaces = num_spaces % (num_words - 1)

    justified_words = []
    for i in range(num_words - 1):
        justified_words.append(words[i] + ' ' * spaces_between_words)
        
        if extra_spaces > 0:
            justified_words[-1] += ' '
            extra_spaces -= 1
            
    justified_words.append(words[-1])
    return ''.join(justified_words)
