from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("model_ex-013_acc-0.625000.h5")
prediction.setJsonPath("model_class.json")
prediction.loadModel(num_objects=2)

predictions, probabilities = prediction.predictImage('image.png', result_count=3)


for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)


