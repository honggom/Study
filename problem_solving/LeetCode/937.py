class Solution(object):
    def reorderLogFiles(self, logs):
        char = []
        num = []
        for log in logs:
            if log.split()[1].isdigit():
                num.append(log)
            else:
                char.append(log)

        char.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return char + num
