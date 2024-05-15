import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import random
#一般单up池
def gachaNormalUntilNew6StarGet():
    count = 0
    countThisRound = 0
    yellowTicket = 0
    while(1):
        count += 1
        increase = 0
        countThisRound += 1
        
        # 小保底
        if countThisRound > 50:
            increase = (countThisRound - 50) * 2

        i = random.randint(1, 100)

        if i <= 2 + increase:

            countThisRound = 0

            # 150抽后6星保底
            if count >= 150:
                yellowTicket += 1
                return count, yellowTicket
            
            # 6星
            if random.random() < 0.5:
                yellowTicket += 1
                return count, yellowTicket
            else:
                yellowTicket += 10
                continue

        # 黄票计算
        if i <= 2 + increase + 8:
            yellowTicket += 5
            continue

        if i <= 2 + increase + 8 + 50:
            yellowTicket += 1
            continue

#限定卡池
def gachaLimitedUntilNew6StarGet():
    count = 0
    yellowTicket = 0
    countThisRound = 0
    new6Star1 = 0 # 限定
    new6Star2 = 0 # 非限定

    while(1):
        count += 1
        increase = 0
        countThisRound += 1

        if countThisRound > 50:
            increase = (countThisRound - 50) * 2
        i = random.randint(1, 100)

        if i <= 2 + increase:
            countThisRound = 0
            tmp = random.random()
            if tmp < 0.35:
                if new6Star1 == 0:
                    new6Star1 = 1
                    yellowTicket += 1
                else:
                    yellowTicket += 10
                
            
            if tmp >= 0.35 and tmp < 0.7:
                if new6Star2 == 0:
                    new6Star2 = 1
                    yellowTicket += 1
                else:
                    yellowTicket += 10
            
            # 抽齐
            if new6Star1 and new6Star2:
                return count, yellowTicket
            
            # 井当期非限定，领限定
            if count >= 300:
                yellowTicket += 1
                return count, yellowTicket

            if tmp >= 0.7:
                yellowTicket += 10
                continue

        if i <= 2 + increase + 8:
            yellowTicket += 5
            continue

        if i <= 2 + increase + 8 + 50:
            yellowTicket += 1
            continue

# 联动卡池
def gachaCollabUntilNew6StarGet():
    count = 0
    countThisRound = 0
    yellowTicket = 0
    while(1):
        count += 1
        increase = 0
        countThisRound += 1
        
        # 小保底
        if countThisRound > 50:
            increase = (countThisRound - 50) * 2

        i = random.randint(1, 100)

        if count >= 120:
            yellowTicket += 1
            return count, yellowTicket
        
        if i <= 2 + increase:

            countThisRound = 0


            # 6星
            if random.random() < 0.5:
                yellowTicket += 1
                return count, yellowTicket
            else:
                yellowTicket += 10
                continue
        # 黄票计算
        if i <= 2 + increase + 8:
            yellowTicket += 5
            continue

        if i <= 2 + increase + 8 + 50:
            yellowTicket += 1
            continue


def calculateNormal(times = 100000):
    countRec = []
    yellowTicketRec = []
    for i in range(times):
        count, yellowTicket = gachaNormalUntilNew6StarGet()
        countRec.append(count)
        yellowTicketRec.append(yellowTicket)
    
    return countRec, yellowTicketRec

def calculateLimited(times = 100000):
    countRec = []
    yellowTicketRec = []
    for i in range(times):
        count, yellowTicket = gachaLimitedUntilNew6StarGet()
        countRec.append(count)
        yellowTicketRec.append(yellowTicket)
    
    return countRec, yellowTicketRec
def calculateCollab(times = 100000):
    countRec = []
    yellowTicketRec = []
    for i in range(times):
        count, yellowTicket = gachaCollabUntilNew6StarGet()
        countRec.append(count)
        yellowTicketRec.append(yellowTicket)
    
    return countRec, yellowTicketRec

def plot_relative_frequency_distribution_with_expectation_and_line(countRec, title):
    count_freq = Counter(countRec)
    total_counts = len(countRec)
    counts = sorted(count_freq.keys())
    frequencies = [count_freq[count] / total_counts for count in counts]

    expectation = sum(count * freq for count, freq in zip(counts, frequencies))

    plt.plot(counts, frequencies, marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel('Count')
    plt.ylabel('Relative Frequency')

    plt.annotate(f'Expectation: {expectation:.2f}', xy=(0.5, 0.9), xycoords='axes fraction', ha='center')

    plt.axvline(x=expectation, color='r', linestyle='--')
    plt.text(expectation, max(frequencies), f'Expectation = {expectation:.2f}', rotation=90, va='bottom', ha='right', color='r')

    plt.grid(True)
    plt.show()

def plot_yellow_ticket_frequency_distribution(yellowTicketRec, title):
    plt.hist(yellowTicketRec, bins=max(yellowTicketRec)-min(yellowTicketRec)+1, density=True, align='left', rwidth=0.8)

    expectation = sum(yellowTicketRec) / len(yellowTicketRec)

    plt.title(title)
    plt.xlabel('Yellow Tickets')
    plt.ylabel('Frequency')
    
    plt.axvline(x=expectation, color='r', linestyle='--')
    plt.text(expectation, plt.gca().get_ylim()[1], f'Expectation = {expectation:.2f}', rotation=90, va='bottom', ha='right', color='r')

    plt.grid(True)
    plt.show()

def plotNormal():
    countRec, yellowTicketRec = calculateNormal(100000)
    # plot_yellow_ticket_frequency_distribution(yellowTicketRec, 'Normal Gacha')
    plot_relative_frequency_distribution_with_expectation_and_line(countRec, 'Normal Gacha')
    plot_relative_frequency_distribution_with_expectation_and_line(countRec, 'Normal Gacha')

# plotNormal()

def plotLimited():
    countRec, yellowTicketRec = calculateLimited(100000)
    plot_yellow_ticket_frequency_distribution(yellowTicketRec, 'Limited Gacha')
    plot_relative_frequency_distribution_with_expectation_and_line(countRec, 'Limited Gacha')

# plotLimited()

def plotcollab():
    countRec, yellowTicketRec = calculateCollab(100000)
    plot_yellow_ticket_frequency_distribution(yellowTicketRec, 'Collab Gacha')
    plot_relative_frequency_distribution_with_expectation_and_line(countRec, 'Collab Gacha')

plotcollab()