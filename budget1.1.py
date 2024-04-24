BUDGET=4000
ABSA_MONTHLY=1000

def investec():
    while True:
        print()
        investec_available=input('Investec Available: R')
        if investec_available.isdigit()==True and int(investec_available)>=BUDGET:
            investec_available=int(investec_available)
            break
        else:
            print()
            print(f'Amount must be equal or more than R{BUDGET}!')
            continue
    return investec_available

def absa():
    while True:
        absa_available=input('Absa Available: R')
        if absa_available.isdigit()==True and int(absa_available)<=ABSA_MONTHLY:
            absa_available=int(absa_available)
            print()
            break
        else:
            print()
            print(f'Amount must be equal or less than R{ABSA_MONTHLY}!')
            print()
            continue
    return absa_available

def transfer(investec_available, absa_available):
    transfer_absa=ABSA_MONTHLY-absa_available
    transfer_savings=investec_available-transfer_absa-BUDGET
    if transfer_savings>=0:
        output=f'Transfer R{transfer_savings} to your savings account and R{transfer_absa} to your Absa account!'
        print('-'*len(output))
        print(output)
        print('-'*len(output))
    else:
        output=f'Transfer R{investec_available-BUDGET} (and R{abs(transfer_savings)} from your savings account) to your Absa account!'
        print('-'*len(output))
        print(output)
        print('-'*len(output))

while True:
    transfer(investec(), absa())