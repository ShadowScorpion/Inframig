class HelpMessage():

  def __init__(self):

    self.bold = '\033[1m'
    self.norm = '\033[0m'

    self.help_message = """
!BNAME!N
          inframig

!BDESCRIPTION!N
          Test inframig desc
    
!BSYNOPSIS!N
          inframig <command> <subcommand> [parameters] 

          Use inframig command help for information on a specific  command.  Use
          inframig help  topics  to view a list of available help topics. The 
          synopsis for each command shows its parameters and their usage. Optional
          parameters are shown in square brackets.

!BOPTIONS!N 

          !Bversion!N
              Version of Inframig

          !Bhelp!N
              Help information
""".replace('!B', self.bold).replace('!N', self.norm)

  def printMessage(self):
    print(self.help_message)  

