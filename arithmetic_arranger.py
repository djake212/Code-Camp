def arithmetic_arranger(problems, display = "1"):
  import re
  firstnum =[]
  sign = []
  secondnum = []
  dashlist =[]
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  anslst = []
  #create ordered lists
  for numprob in problems:
    firstnum += re.findall('^[0-9]+', numprob)
    sign += re.findall('^[0-9]+\s([+-])', numprob)
    secondnum += re.findall('^[0-9]+\s.\s([a-z0-9]+)', numprob) 
    #too many problems error
    if len(firstnum) > 5:
      return 'Error: Too many problems.'
    #only int error
    try:
      int(firstnum[problems.index(numprob)])
      int(secondnum[problems.index(numprob)])
    except:
      return "Error: Numbers must only contain digits."  
    #too many digits error
    if len(firstnum[problems.index(numprob)]) > 4 or len(secondnum[problems.index(numprob)]) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    #operator not + or -
    if re.search('^.+\s([+-])',numprob) == None:
      return "Error: Operator must be '+' or '-'."
    #print(firstnum,sign,secondnum)
    #determine longer number and number of dashes
  for numprob in problems:
    if int(firstnum[problems.index(numprob)]) >= int(secondnum[problems.index(numprob)]):
      dashlist.append(int(len(firstnum[problems.index(numprob)])) + 2)
    else:
      dashlist.append(int(len(secondnum[problems.index(numprob)])) + 2) 
    #arranging math problems
    if (problems.index(numprob)) != 0:
      spacing = 4*' '
    else:
      spacing = ''
    probtop = spacing + (dashlist[problems.index(numprob)] - len(firstnum[problems.index(numprob)]))*' ' + firstnum[problems.index(numprob)]
    line1 += probtop
    #print(line1)
    probbot = spacing + sign[problems.index(numprob)] + (dashlist[problems.index(numprob)] - len(secondnum[problems.index(numprob)]) - 1)*' ' + secondnum[problems.index(numprob)]
    line2 += probbot
    dashes = spacing + (dashlist[problems.index(numprob)] * '-')
    line3 += dashes


    if display is True:
      firstnumC = firstnum.copy()
      secondnumC = secondnum.copy()
      if sign[problems.index(numprob)] == '+':
        val = str(int(firstnumC[problems.index(numprob)]) + int(secondnumC[problems.index(numprob)]))
        anslst.append(val)
      else:
        val = str(int(firstnumC[problems.index(numprob)]) - int(secondnumC[problems.index(numprob)]))
        anslst.append(val)
      ans = spacing + (dashlist[problems.index(numprob)] - len(anslst[problems.index(numprob)]) )*' ' + anslst[problems.index(numprob)]
      line4 += ans

  line1 += '\n'
  line2 += '\n'
  if display is True:
    line3 += '\n'
    return line1 + line2 + line3 + line4
  else:
    return line1 + line2 + line3
      
    




    


    

  
 
    




