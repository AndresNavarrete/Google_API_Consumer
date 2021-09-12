from Consumer import Consumer
from DataProcessor import DataProcessor
from InputManager import InputManager

consumer = Consumer()
inputManager = InputManager()
dataProcessor = DataProcessor(consumer)

dataProcessor.readInput(inputManager)
dataProcessor.proccesData()
dataProcessor.exportExcel()