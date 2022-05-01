import re


def solution(emails):
    answer = 0
    for email in emails:
        is_email = re.compile(r"[a-z0-9.]+@[a-z]+\.(com|net|org)+")
        if is_email.match(email):
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(["d@co@m.com", "a@abc.com", "b@def.com", "c@ghi.net"]))
    print(solution(["abc.def@x.com", "abc", "abc@defx", "abc@defx.xyz"]))
