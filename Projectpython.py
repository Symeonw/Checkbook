#The beginning of the end...
def start():
  print ("~~~Welcome to your terminal checkbook!~~~\n \nWhat would you like to do? \n 1) View current account balance\n 2) Record new Debt\n 3) Record new Credit\n 4) Exit")
  while True:
    global ui_choice
    ui_choice = input(" \nSelect option: ")
    ui_check()
    output = ()
    if output == False:
      continued
    ui_choice = int(ui_choice)
    ui_help()
    break

  
    
def ui_help():
  if ui_choice == 5:
    print(" \nEnter a number between 1 and 4.")

def ui_int():
  try: 
    int(ui_choice)
  except:
    return False

def ui_range_check():
  if int(ui_choice) >= 1 and int(ui_choice) <= 5:
    return True
  else:
    return False

def ui_check():      
  ui_int()
  if ui_int() == False:
    global output
    output = False
  else:
    ui_range_check()
    if ui_range_check == False:
      output = False

debt_ledger_add = 0
credit_ledger_add = 0
debt_ledger = -100
credit_ledger = 500
inter_exit = ()
count_start = 0
bad_entry = ()
def modules():
  while True:
    global count_start
    global inter_exit
    if inter_exit == "Y":
      inter_exit = ()
      pass
    elif inter_exit == "N" or inter_exit == () and count_start >= 1:
      start()
    elif count_start < 1:
      count_start += 1

    if ui_choice == 1:
      general_ledger_check()
      exit_strat_balance()
    elif ui_choice == 2:
      debt_ledger_check()
      exit_strat_transact()
    elif ui_choice == 3:
      credit_ledger_check()
      exit_strat_transact()
    elif ui_choice == 4:
      program_termination()

def general_ledger_check():
  global general_ledger
  general_ledger = credit_ledger + debt_ledger
  print ("Current Balance is:",general_ledger)

def debt_ledger_check():
    print ("Loading Debt Recording Aparatus...")
    debtint = input("Please enter amount to debt: ")
    try:
      float(debtint)
      print (" \nInput taken")
    except:
      print (" \nPlease enter only numbers.\nReturning to main menu. \n")
      print('-----------------------------------------')
    if debtint.isdigit() == True: 
      global debt_ledger_add
      global debt_ledger
      debtint = float(debtint)
      debt_ledger_add += debtint
      debt_ledger -= debt_ledger_add
      debt_ledger = round(debt_ledger,2)
    else:
      global bad_entry
      bad_entry = True
def credit_ledger_check():
  print ("Loading Credit Recording Aparatus...")
  creditint = (input("Please enter amount to credit: "))
  try:
    float(creditint)
  except:
    print (" \nPlease enter only numbers.\nReturning to main menu. \n")
    print('-----------------------------------------')
  if creditint.isdigit() == True:
    creditint = float(creditint)
    global credit_ledger_add
    global credit_ledger
    credit_ledger_add += creditint
    credit_ledger += credit_ledger_add
    credit_ledger = round(credit_ledger,2)
  else:
    global bad_entry
    bad_entry = True

def program_termination():
  print ("*****PROGRAM TERMINATED*****")
    
        

def exit_strat_balance():
  while True:
    print("--------------------------------------")
    global inter_exit
    if inter_exit == "Y":
      inter_exit = ()
      break
    inter_exit = input(" \nSelect 'Y' to return to the main menu.") 
    if inter_exit == "Y":
      inter_exit = ()
      break
    elif inter_exit == "N":
      pass
    else:
      print (" \n*Please enter 'Y' or 'N'.*")

def exit_strat_transact():
  while True:
    global bad_entry
    if bad_entry == True:
      bad_entry = ()
      break
    print("--------------------------------------")
    global inter_exit
    if inter_exit == "Y":
      break
    inter_exit = input(" \nWould you like to enter an additional transaction?(Y/N)") 
    if inter_exit == "Y":
      continue
    elif inter_exit == "N":
      break
    else:
      print (" \n*Please enter Y/N.")
start()
modules()