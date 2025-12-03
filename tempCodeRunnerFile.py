            
        for m in range(len(board)):#row
            for n in range(len(board[m])):#col
                cell = board[m][n]
                if cell =='.':
                    continue #cell empty

                #add cell to col, row, and diag trackers
                col[n].append(cell)
                row[m].append(cell)
                if m==n:#top left diagonal
                    diag.append(cell)
                if m+n==2:
                    diag2.append(cell)

                if len(set(col[n]))==1 and len(col[n])==3:
                    #win
                    print(f'winner is {col[n][0]}!')
                elif len(set(row[m]))==1 and len(row[m])==3:
                    #win
                    print(f'winner is {row[m][0]}!')
                elif len(set(diag))==1 and len(diag)==3:
                    #win
                    print(f'winner is {diag[0]}!')
                elif len(set(diag2))==1 and len(diag2)==3:
                    #win
                    print(f'winner is {diag2[0]}!')
