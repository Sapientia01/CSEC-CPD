import sys
import math

def build_sparse_table(arr, n):
    logn = math.floor(math.log2(n)) + 1
    table = [[0] * n for _ in range(logn)]
    for i in range(n):
        table[0][i] = arr[i]
    for j in range(1, logn):
        step = 1 << (j-1)
        for i in range(n - (1 << j) + 1):
            table[j][i] = table[j-1][i] & table[j-1][i+step]
    return table

def query_sparse_table(l, r, table):
    j = math.floor(math.log2(r - l + 1))
    return table[j][l] & table[j][r - (1 << j) + 1]

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index]); index += 1
        arr = list(map(int, data[index:index+n]))
        index += n
        q = int(data[index]); index += 1
        queries = []
        for i in range(q):
            l = int(data[index]); k = int(data[index+1]); index += 2
            queries.append((l, k))
        
        # Build sparse table
        logn = math.floor(math.log2(n)) + 1
        table = [[0] * n for _ in range(logn)]
        for i in range(n):
            table[0][i] = arr[i]
        for j in range(1, logn):
            step = 1 << (j-1)
            for i in range(n - (1 << j) + 1):
                table[j][i] = table[j-1][i] & table[j-1][i+step]
        
        res = []
        for (l, k) in queries:
            low = l - 1
            high = n - 1
            ans_index = -2
            while low <= high:
                mid = (low + high) // 2
                val = query_sparse_table(l-1, mid, table)
                if val >= k:
                    ans_index = mid
                    low = mid + 1
                else:
                    high = mid - 1
            res.append(str(ans_index + 1))
        output_lines.append(" ".join(res))
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()