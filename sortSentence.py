class Solution:
    def sortSentence(self, s: str) -> str:
        answer = s.split()
        answer.sort(key=lambda word: int(word[-1]))
        answer = [word[:-1] for word in answer]
        exactanswer = ' '.join(answer)
        return exactanswer

        
