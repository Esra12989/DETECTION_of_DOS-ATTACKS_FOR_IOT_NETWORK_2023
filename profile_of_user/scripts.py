
import pickle
 
def run(features):
    # Load the saved model
    filename = 'profile_of_user/finalized_Esra_model_DT_GA.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    values = features.split(',')
    float_values = [float(value) for value in values]
    # Perform prediction using the loaded model
    prediction = loaded_model.predict([float_values])
    # print(prediction[0])
    return prediction[0]  # Return the predicted value