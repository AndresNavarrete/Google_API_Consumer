from Consumer import Consumer
from DataProcessor import DataProcessor
from InputManager import InputManager
from time import time

def main():
    consumer = Consumer()
    inputManager = InputManager()
    dataProcessor = DataProcessor(consumer)

    dataProcessor.readInput(inputManager)
    dataProcessor.proccesData()
    dataProcessor.exportExcel()

if __name__ == "__main__":
    initialTime = time.time()

    main()

    finalTime = time.time()
    secondsElapsed = round(finalTime - initialTime, 2)
    print("Time elapsed: {} seconds ".format(secondsElapsed))