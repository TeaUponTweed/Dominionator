s
dict cardList(
              [,card('curse', -1,0,0,0,0,0,0)],
              [,card('copper', 0,1,0,0,0,0,0)],
              [,card('estate', 1,0,0,0,0,0,2)],
              ['silver',card('silver', 0,2,0,0,0,0,3)],
              ['duchy',card('duchy', 3,0,0,0,0,0,5)],
              ['duchy',card('gold', 0,3,0,0,0,0,5)],
              ['province',card('province', 5,0,0,0,0,0,8)],
              # ['cellar',card('cellar', 0,0,0,0,0,0,2)],
              # ['chapel',card('chapel', 5,0,0,0,0,0,2)],
              ['moat',card('moat', 0,0,0,0,0,2,2)],
              ['harbinger',card('harbinger', 0,0,0,0,1,1,3)],
              ['merchant',card('merchant', 0,2,0,0,1,1,3)],
              ['vassal',card('vassal', 0,0,0,0,0,8)],
              ['village',card('village', 0,0,0,0,2,1,3)],
              # ['workshop',card('workshop', 5,0,0,0,0,0,8)],
              # ['bureaucrat', card('bureaucrat',0,0,0,0,0,0,0)]
              # ['gardens', card('gardens',0,0,0,0,0,0,0)]
              # ['militia', card('militia',0,0,0,0,0,0,0)]
              # ['moneylender', card('moneylender',0,0,0,0,0,0,0)]
              ['poacher', card('poacher',0,0,0,0,0,0,0)]
              ['remodel', card('remodel',0,0,0,0,0,0,0)]
              ['smithy', card('smithy',0,0,0,0,0,0,0)]
              )

class card(object):
  """card:
  """
  name = ""
  def __init__(self,
               name):
    self.name      = name
    self.vps       = 0
    self.treasure  = 0
    self.cost      = 0
    self.actions   = 0
    self.plusCards = 0
    self.buys      = 0

    if(name == 'curse'):
      self.vps = -1
    elif(name == 'copper'):
      self.treasure = 1
    elif(name == 'estate'):



    


