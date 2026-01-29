from typing import List

class Solution(object):
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordsLength = len(words)
        if wordsLength == 0:
            return []
        someWords = [ words[0] ]
        for i in range(1, len(words)):
            if len("".join(someWords)) + len(words[i]) + i > maxWidth:
                break
            someWords.append(words[i])
        someWordsLength = len(someWords)
        if someWordsLength == wordsLength or someWordsLength == 1:
            justified = " ".join(someWords).ljust(maxWidth)
        else:
            spaces = [ "" ] * (someWordsLength - 1)
            spacesLength = len(spaces)
            for i in range(maxWidth - len("".join(someWords))):
                if len("".join(someWords)) + len("".join(spaces)) >= maxWidth:
                    break
                spaces[i % spacesLength] += " "
            spaces.append("")
            justified = "".join([ someWords[i] + spaces[i] for i in range(len(someWords)) ])
        return [ justified, *self.fullJustify(words[someWordsLength:], maxWidth) ]