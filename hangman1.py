def hangman(word) :
    wrong=0
    stages=["",
            "_____     ",
            "!         ",
            "!   !     ",
            "!   0     ",
            "!  /!>    ",
            "!  / >    ",
            "!         ",
            ]
    reletters=list(word)
    board=["_"]*len(word)
    win=False
    print("ハングマンへようこそ")


    while wrong < len(stages)-1 :    
      a=input("文字を入力してください")
      if a in reletters :   
        b=reletters.index(a)  
        board[b]=a            
        reletters[b]="$"      
                              

      else :
         wrong+=1
      print(" ".join(board))   
      e=wrong+1                
      print("\n".join(stages[0:e]))    
      if "_" not in board :
          print("あなたの勝ち")
          print(" ".join(board))
          win=True
          break
    
    if win==False :
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け.せいかいは{}".format(word))

hangman("tagamitatuya")
