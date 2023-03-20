def parallel_processing(n, m, data):
    result = []
    start_time = [0] * n  # a list to keep track of the start time of each thread
    for i in range(m):
        next_thread = 0  # index of the thread that will process the next job
        for j in range(1, n):
            if start_time[j] < start_time[next_thread]:
                next_thread = j
        result.append((next_thread, start_time[next_thread]))
        start_time[next_thread] += data[i]
    return result

def main():
    # read input from keyboard
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # call the function and get the results
    result = parallel_processing(n, m, data)

    # print out the results
    for i in range(m):
        print(result[i][0], result[i][1])

if __name__ == "__main__":
    main()
