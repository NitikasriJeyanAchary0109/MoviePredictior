"""
Interest Prediction Model - Streamlit App
==========================================
Clean & Simple UI for Decision Tree Classifier
Predicts user interests: Animation, Action, Drama
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Page Configuration
st.set_page_config(
    page_title="Interest Predictor",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Clean, Modern CSS
st.markdown("""
<style>
    /* Clean color palette */
    :root {
        --primary: #6366f1;
        --secondary: #8b5cf6;
        --accent: #10b981;
        --background: #f8fafc;
        --card: #ffffff;
        --text: #1e293b;
    }
    
    /* Main container */
    .stApp {
        background: var(--background);
    }
    
    /* Header styling */
    .header {
        text-align: center;
        padding: 2rem 1rem;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3);
    }
    
    .header h1 {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }
    
    .header p {
        color: rgba(255,255,255,0.9);
        font-size: 1rem;
        margin: 0.5rem 0 0 0;
    }
    
    /* Input form card */
    .input-card {
        background: var(--card);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
    }
    
    /* Result card */
    .result-card {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        padding: 2.5rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
        animation: fadeIn 0.5s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .result-emoji {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    
    .result-title {
        color: rgba(255,255,255,0.9);
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    
    .result-prediction {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }
    
    .result-confidence {
        color: rgba(255,255,255,0.85);
        font-size: 1.1rem;
        margin-top: 1rem;
    }
    
    /* Input labels */
    .input-label {
        font-size: 0.9rem;
        font-weight: 600;
        color: var(--text);
        margin-bottom: 0.5rem;
        display: block;
    }
    
    /* Age slider styling */
    .age-display {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary);
        padding: 1rem;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    /* Gender buttons */
    .gender-btn {
        padding: 1rem 2rem;
        border-radius: 12px;
        font-size: 1rem;
        font-weight: 600;
        border: 2px solid #e2e8f0;
        background: white;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .gender-btn:hover {
        border-color: var(--primary);
    }
    
    .gender-btn.selected {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        border-color: transparent;
    }
    
    /* Predict button */
    .predict-btn {
        width: 100%;
        padding: 1rem;
        font-size: 1.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }
    
    .predict-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
    }
    
    .predict-btn:active {
        transform: translateY(0);
    }
    
    /* Spinner */
    .spinner {
        text-align: center;
        padding: 2rem;
    }
    
    /* Error message */
    .error-msg {
        background: #fef2f2;
        border: 1px solid #fecaca;
        color: #dc2626;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    
    /* Section titles */
    .section-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: var(--text);
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .header h1 { font-size: 1.5rem; }
        .result-prediction { font-size: 2rem; }
        .input-card { padding: 1.5rem; }
    }
</style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    """Load the trained decision tree model"""
    try:
        if os.path.exists('model.pkl'):
            model = joblib.load('model.pkl')
            return model
        else:
            return None
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def main():
    """Main function to run the Streamlit app"""
    
    # Load model
    model = load_model()
    
    # Header
    st.markdown("""
    <div class="header">
        <h1>🎯 Interest Predictor</h1>
        <p>AI-powered interest prediction based on your preferences</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check if model is available
    if model is None:
        st.markdown("""
        <div class="error-msg">
            <strong>⚠️ Model not found</strong><br>
            Please ensure 'model.pkl' file is present in the directory.
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Input Form
    with st.container():
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="section-title">📝 Enter Your Information</h3>', unsafe_allow_html=True)
        
        # Age input
        st.markdown('<label class="input-label">What is your age?</label>', unsafe_allow_html=True)
        age = st.slider(
            "Age",
            min_value=18,
            max_value=80,
            value=25,
            step=1,
            label_visibility="collapsed"
        )
        st.markdown(f'<div class="age-display">{age} years</div>', unsafe_allow_html=True)
        
        # Gender input
        st.markdown('<label class="input-label">What is your gender?</label>', unsafe_allow_html=True)
        
        col_f, col_m = st.columns(2)
        
        with col_f:
            female_selected = st.button(
                "👩 Female",
                key="female",
                use_container_width=True
            )
        with col_m:
            male_selected = st.button(
                "👨 Male",
                key="male", 
                use_container_width=True
            )
        
        # Determine selected gender
        if 'gender_sel' not in st.session_state:
            st.session_state.gender_sel = "Female"
        
        if female_selected:
            st.session_state.gender_sel = "Female"
        elif male_selected:
            st.session_state.gender_sel = "Male"
        
        # Show selected
        st.markdown(f"""
        <div style="text-align: center; padding: 0.5rem; color: #6366f1; font-weight: 600;">
            Selected: {st.session_state.gender_sel}
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Predict button
    if st.button("🔮 Predict My Interest", type="primary", use_container_width=True):
        # Prepare input
        gender_encoded = 0 if st.session_state.gender_sel == "Female" else 1
        input_data = pd.DataFrame({
            'Age': [age],
            'Gender': [gender_encoded]
        })
        
        # Make prediction
        try:
            prediction = model.predict(input_data)[0]
            probabilities = model.predict_proba(input_data)[0]
            confidence = max(probabilities) * 100
            
            # Determine emoji based on prediction
            emoji_map = {
                'Animation': '🎬',
                'Action': '💥', 
                'Drama': '🎭'
            }
            
            emoji = emoji_map.get(prediction, '🎯')
            
            # Show result
            st.markdown(f"""
            <div class="result-card">
                <div class="result-emoji">{emoji}</div>
                <div class="result-title">Your predicted interest is</div>
                <div class="result-prediction">{prediction}</div>
                <div class="result-confidence">Confidence: {confidence:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
    
    # Footer
    st.markdown("""
    <div style="text-align: center; padding: 2rem 1rem; color: #94a3b8; font-size: 0.85rem;">
        <p>Built with ❤️ using Streamlit & Machine Learning</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

