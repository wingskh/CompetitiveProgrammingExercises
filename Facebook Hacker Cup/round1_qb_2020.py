total_tasks = int(input())
p_list = []
q_list = []

for i in range(total_tasks):
    n, m, k, s = list(map(int, input().split()))
    p_list = list(map(int, input().split()))
    a_p, b_p, c_p, d_p = list(map(int, input().split()))
    q_list = list(map(int, input().split()))
    a_q, b_q, c_q, d_q = list(map(int, input().split()))

    is_more_cluster = True if m >= n else False

    for j in range(max(n, m)-k):
        if j < n-k:
            p_list.append((a_p*p_list[j+k-2] + b_p*p_list[j+k-1] + c_p) % d_p + 1)
        if j < m-k:
            q_list.append((a_q*q_list[j+k-2] + b_q*q_list[j+k-1] + c_q) % d_q + 1)

    p_list.sort()
    q_list.sort()

    low = 0
    high = d_p+d_q
    answer = high

    while low <= high:
        mid = int(low + (high - low)/2)
        step = 0

        for driver_index, log_driver in enumerate(p_list):
            if step == len(q_list):
                break
            left_cluster = q_list[step]

            for cluster_loc in range(step, len(q_list)):
                right_cluster = q_list[step]
                distance = 0

                if log_driver <= left_cluster:
                    distance = right_cluster - log_driver
                elif log_driver >= right_cluster:
                    distance = log_driver - left_cluster
                else:
                    distance = right_cluster - left_cluster + min(log_driver - left_cluster, right_cluster - log_driver)

                if distance > mid:
                    break
                else:
                    step += 1

        if step == len(q_list):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    print(f"Case #{i+1}: {answer}")

