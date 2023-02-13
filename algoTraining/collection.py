from sys import stdin, stdout


def solution(string, k):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):

            if string[i] == string[j] and j - i - 1 <= k:
                return k + 2
    return k + 1


def main():
    k = int(input())
    string = input()
    print(solution(string, k))


if __name__ == "__main__":
    main()
