
import sklearn
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Ensure pipeline is always defined at module scope
pipeline = None

# 1. Load the single Pipeline globally
try:
    pipeline_filename = 'text_model_pipeline.pkl'
    with open(pipeline_filename, 'rb') as model_file:
        # This one object contains both the TfidfVectorizer and the MultinomialNB
        pipeline = pickle.load(model_file)
        
    print("✅ Full Classification Pipeline loaded successfully.")
except FileNotFoundError as e:
    print(f"❌ ERROR: Pipeline file not found - {e}. Ensure the .pkl file is in the same directory.")
    pipeline = None
except Exception as e:
    # Catch other pickle/unpickle errors and keep pipeline as None
    print(f"❌ ERROR loading pipeline: {e}")
    pipeline = None

@app.route('/predict', methods=['POST'])
def predict():
    if not pipeline:
        return jsonify({'error': 'Server model not loaded'}), 500

    # Get the text input
    try:
        data = request.get_json(force=True)
        text_input = data.get('text', '')
    except Exception:
        return jsonify({'error': 'Invalid input format, expected JSON with "text" field'}), 400 
    
    # Input must be wrapped in a list for the pipeline's predict method
    input_list = [text_input] 

    # 2. Use the Pipeline's .predict() method
    # The pipeline automatically calls: 
    #   1. Vectorizer.transform(input_list)
    #   2. Classifier.predict(transformed_data)
    prediction_result = pipeline.predict(input_list)
    
    # Format the response: convert NumPy scalars or other types into JSON-serializable Python types
    predicted_raw = prediction_result[0]
    try:
        # numpy scalars have .item()
        predicted_class = predicted_raw.item()
    except Exception:
        predicted_class = predicted_raw

    # decode bytes if needed
    if isinstance(predicted_class, (bytes, bytearray)):
        try:
            predicted_class = predicted_class.decode('utf-8')
        except Exception:
            predicted_class = str(predicted_class)

    response = {
        'input_text': text_input,
        'predicted_class': predicted_class
    }

    return jsonify(response)

if __name__ == '__main__':
    # bind to 0.0.0.0 so the server is reachable from other hosts if needed
    app.run(host='0.0.0.0', port=5000, debug=True)