import yfinance as yf
import os
import time

if __name__ == "__main__":

    while True:
        print("Waiting for file...")
        while True:
            try:
                with open('ticker-input.txt') as file:
                    userTicker = file.read() #will read ticker from ticker-input.txt file
            except FileNotFoundError:
                time.sleep(2)
            else:
                print("File processing...")
                os.remove('ticker-input.txt')
                break

        quote = yf.Ticker(str(userTicker).upper()) #uses yfinance to receive daily high and low of the file ticker
        
        high = quote.info["dayHigh"] #variable to store high value
        low = quote.info["dayLow"] #variable to store low value
        
        with open('ticker-output.txt', 'w', encoding='utf-8') as ticker_file:
            #writes high and low into a single string sentence. Example output: Daily High: $2705.43, Daily Low: $2635.03
            ticker_file.write("Daily High: $"+ str("{:.2f}".format(high)) + ", Daily Low: $" + str("{:.2f}".format(low)))

        print("Finished processing file\n")