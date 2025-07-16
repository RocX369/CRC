def main(length: int = 10):
    q = []
    for i in range(length):
        q.append(None)

    print(q)

    for i in range(length):
        if q[i] == None:
            del q[i]
            q.insert(i, 5)
            break

    print(q)

    for i in range(length):
        if q[i] != None:
            del q[i]
            q.insert(i, None)
            break

    print(q)

if __name__ == "__main__":
    main(10)
