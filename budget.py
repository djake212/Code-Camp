class Category:

  def __init__(self , nam):
    self.name = nam
    self.ledger = []
    self.balance = 0.0
    self.costs = []
  def get_balance(self):
    for things in self.ledger:
      self.balance += things['amount']
    try:
      return self.balance
    finally:
      self.balance = 0.0
    
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True
    
  def deposit(self, amount, description = -1):
    if description == -1: description = ''
    entry = {"amount": amount, "description": description}
    self.ledger.append(entry)
  
  def withdraw(self, amount, description = -1):
    if self.check_funds(amount) == False:
      return False
    else:
      if description == -1: description = ''
      entry = {"amount": (-1.0)*amount, "description": description}
      self.ledger.append(entry)
      self.costs.append(entry)
      return True
  
  def transfer(self, amount, difcateg):
    if self.check_funds(amount) == False:
      return False
    else:
      self.withdraw(amount, 'Transfer to ' + difcateg.name)
      difcateg.deposit(amount, 'Transfer from ' + self.name)
      return True

  def __str__(self):
    astnum = 30 - len(self.name)
    header = int((astnum/2))*'*' + self.name + int((astnum/2))*'*'
    line = ''
    for dicts in self.ledger:
      i = dicts['description']
      i = i[:23]
      u = str(float(dicts['amount']))
      if u[-2:] == '.0':
        u += '0'
      u = u[:7]
      spacenum = 30 - len(i) - len(u)
      line += i + spacenum*' ' + u + '\n'
    footer = 'Total: ' + str(self.get_balance())
    fullpackage = header + '\n' + line + footer
    return fullpackage
      
        

  




def create_spend_chart(categories):
  percdic = {}
  tot = 0.0
  catetot = 0.0
  masterlst = []
  masterlst2 = []
  for category in categories:
    masterlst.append(list(category.name))
    masterlst2.append(category.name)
    for cost in category.costs:
      tot += -1 * cost["amount"]
  for category in categories:
    for cost in category.costs:
      catetot += -1 * cost["amount"]
    percdic.update({category.name : range(int((catetot / tot)*10))})
    catetot = 0.0

  histogram = 'Percentage spent by category\n'
  countdown = 10
  while True:
      countdown -= 1
      if countdown == -2:
        break
      else:
        perc = str((countdown + 1)*10) 
        perc = (3 - len(perc))*' ' + perc
        part = perc + '| '
        for category in categories:
          try: 
            if countdown == -1:
              spot = 'o'
            else:
              percdic[category.name][countdown]
              spot = 'o'
          except:
            spot = ' '
          part += spot + '  '
        histogram += part + '\n'
  histogram += 4*' '+(len(part)-4)*'-' +'\n'

  def bruh(thing):
    return len(thing)
  masterlst2.sort(reverse = True, key=bruh)
  darange = range(len(masterlst2[0]))
  darange2 = range(len(categories))
  for letters in darange:
    part1 = '     '
    count3 = 0
    for category in darange2:
      count3 += 1
      try:
        thing1 = masterlst[category][letters]
      except:
        thing1 = ' '
      part1 += thing1 + '  '
      if count3 == len(categories):
        part1 += '\n'

    histogram += part1
  histogram = histogram.rstrip() + '  '
  return histogram