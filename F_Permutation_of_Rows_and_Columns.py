import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index]); m = int(data[index+1]); index += 2
        a = []
        for i in range(n):
            row = list(map(int, data[index:index+m]))
            index += m
            a.append(row)
        b = []
        for i in range(n):
            row = list(map(int, data[index:index+m]))
            index += m
            b.append(row)
        
        row_count_a = defaultdict(int)
        for row in a:
            sorted_row = tuple(sorted(row))
            row_count_a[sorted_row] += 1
            
        row_count_b = defaultdict(int)
        for row in b:
            sorted_row = tuple(sorted(row))
            row_count_b[sorted_row] += 1
            
        if row_count_a != row_count_b:
            output_lines.append("NO")
            continue
            
        col_count_a = defaultdict(int)
        for j in range(m):
            col = []
            for i in range(n):
                col.append(a[i][j])
            sorted_col = tuple(sorted(col))
            col_count_a[sorted_col] += 1
            
        col_count_b = defaultdict(int)
        for j in range(m):
            col = []
            for i in range(n):
                col.append(b[i][j])
            sorted_col = tuple(sorted(col))
            col_count_b[sorted_col] += 1
            
        if col_count_a != col_count_b:
            output_lines.append("NO")
        else:
            output_lines.append("YES")
            
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()