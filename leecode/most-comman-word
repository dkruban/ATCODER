import collections
import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(banned)
        cleaned_paragraph = re.sub(r"[!?',;.]", " ", paragraph)
        words = cleaned_paragraph.lower().split()
        word_counts = collections.Counter(
            word for word in words if word not in banned_set
            )
        return word_counts.most_common(1)[0][0]
