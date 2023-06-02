
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  letter_dict = {}
  total_arts = 0
  for i in range(N):
    if C[i]=="P":
      if (i+X)<=N:
        for j in range(min(i+X,N),min(i+Y+1,N)):
          if C[j] == "A":
            for k in range(min(j+X,N),min(j+Y+1,N)):
              if C[k] == "B":
                total_arts += 1
                
      if (i-X)>=0:        
        for j in range(max(i-X,0),max(i-Y-1,0),-1):
          if C[j] == "A":
            for k in range(max(j-X,0),max(j-Y-1,0),-1):
              if C[k] == "B":
                total_arts += 1
  return total_arts


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  letter_dict = {x:[] for x in ["P","A","B"]}
  total_arts = 0
  for i in range(N):
    #print(f"C[{i}]:{C[i]}")
    if (C[i]=="P") or (C[i]=="A"):
      letter_dict[C[i]].append(i)
    elif C[i]=="B":
      for j in letter_dict["A"]:
        if X<=(i-j)<=Y:
          for k in letter_dict["P"]:
            if (k<=j) and X<=(j-k)<=Y:
              #print(f"i:{i}")
              #print(f"k:{k}")
              #print(f"j:{j}")
              total_arts += 1
  #print(f"***** Before : {total_arts}")  
  letter_dict = {x:[] for x in ["P","A","B"]}
  for i in range(N-1,-1,-1):
    if (C[i]=="P") or (C[i]=="A"):
      letter_dict[C[i]].append(i)
    elif C[i]=="B":
      for j in letter_dict["A"]:
        if X<=(j-i)<=Y:
          for k in letter_dict["P"]:
            if (k>=j) and (X<=(k-j)<=Y):
              total_arts += 1
  #print(f"***** After : {total_arts}")  
  return total_arts



# Most efficinet one 
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  photographer_idx = []
  actor_photographer_dict = dict() 
  total_arts = 0
  for i in range(N):
    if C[i] == "P":
      photographer_idx.append(i)
    elif C[i] == "A":
      for p in photographer_idx:
        dist = i-p
        if X<=dist<=Y:
          actor_photographer_dict[i] = actor_photographer_dict.get(i,0) + 1
    elif C[i] == "B":
      for ap in actor_photographer_dict:
        dist_ba = i - ap
        if X<=dist_ba<=Y:
          total_arts += actor_photographer_dict[ap]
    #print(f"**************** total_arts before : {total_arts}")      
  photographer_idx = []
  actor_photographer_dict = dict() 
  for i in range(N-1,-1,-1):
    if C[i] == "P":
      photographer_idx.append(i)
    elif C[i] == "A":
      for p in photographer_idx:
        dist = p - i
        if X<=dist<=Y:
          actor_photographer_dict[i] = actor_photographer_dict.get(i,0) + 1
    elif C[i] == "B":
      for ap in actor_photographer_dict:
        dist_ba = ap - i
        if X<=dist_ba<=Y:
          total_arts += actor_photographer_dict[ap]
    #print(f"**************** total_arts after : {total_arts}")    
  return total_arts