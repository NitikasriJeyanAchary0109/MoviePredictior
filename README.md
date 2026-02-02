# 🎯 Interest Prediction Model - Streamlit App

A professional, production-ready Streamlit application for deploying a Decision Tree Classifier that predicts user interests (Animation, Action, Drama) based on Age and Gender.

![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24+-blue?style=for-the-badge&logo=scikit-learn&logoColor=white)

## ✨ Features

### 🎨 Professional UI/UX
- **Modern Gradient Design**: Beautiful purple-blue gradient header
- **Custom Card Layouts**: Prediction results displayed in styled cards
- **Responsive Sidebar**: Clean input controls with helpful tooltips
- **Color-coded Feedback**: Info, success, and warning boxes
- **Interactive Visualizations**: Dynamic charts and graphs

### 🔮 Core Functionality
- **Real-time Predictions**: Instant interest predictions with confidence scores
- **Probability Analysis**: Detailed probability breakdown for each category
- **Decision Tree Visualization**: See how the model makes decisions
- **Feature Importance**: Understand which features matter most
- **Sample Data Testing**: Test with pre-built sample dataset

### 📊 Advanced Features
- **Model Performance Metrics**: Tree depth, number of leaves, classes
- **Batch Predictions**: Predict multiple samples at once
- **Interactive Charts**: Probability distribution and feature importance
- **Error Handling**: Robust error management with helpful messages

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Trained model file (`model.pkl`)

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd /Users/nitikasrijeyanachary/Desktop/Task
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:8501
   ```

## 📁 Project Structure

```
Task/
├── app.py              # Main Streamlit application
├── model.pkl           # Trained Decision Tree model
├── requirements.txt    # Python dependencies
├── sample_data.csv     # Sample data for testing
└── README.md          # This file
```

## 🎯 How to Use

### Single Prediction
1. Adjust the **Age** slider (18-80 years)
2. Select **Gender** (Male/Female)
3. Click **"Predict Interest"**
4. View the prediction and confidence scores

### Test with Sample Data
1. Scroll to **"🧪 Test with Sample Data"** section
2. Check **"Load and Test with Sample Data"**
3. Click **"Predict All Samples"**
4. See predictions for multiple users at once

### Explore Model Details
- **Decision Tree Structure**: View the complete tree visualization
- **Feature Importance**: See which features influence predictions most
- **Model Information**: Check tree depth, leaves, and classes

## 🔧 Model Information

- **Algorithm**: Decision Tree Classifier
- **Input Features**: 
  - Age (numeric: 18-80)
  - Gender (binary: Male=1, Female=0)
- **Target Variable**: Interest (Animation, Action, Drama)
- **Model File**: `model.pkl`

## 📊 Dependencies

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
graphviz>=0.20.0
joblib>=1.3.0
seaborn>=0.12.0
plotly>=5.18.0
```

## 🎨 Customization

### Changing Colors
Edit the CSS in `app.py`:
```python
# Find and modify these color codes:
# Primary: #667eea
# Secondary: #764ba2
# Accent: #4caf50
```

### Adding Features
1. Add new input fields in the sidebar
2. Update the `input_data` DataFrame
3. Modify model loading if needed
4. Update the README

### Styling Changes
All custom styling is in the `<style>` section at the top of `app.py`. Modify the CSS to match your brand.

## 🚀 Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Connect your GitHub account to [Streamlit Cloud](https://streamlit.io/cloud)
3. Select your repository and branch
4. Add `requirements.txt` to the app settings
5. Deploy!

### Local Network
```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

### Docker (Optional)
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

## 📈 Performance Tips

1. **For better performance**, install Watchdog:
   ```bash
   pip install watchdog
   ```

2. **Enable caching** in `config.toml`:
   ```toml
   [server]
   enableCORS = false
   enableXsrfProtection = true
   ```

3. **Memory optimization**:
   ```python
   @st.cache_resource
   def load_model():
       # Your model loading code
       pass
   ```

## 🐛 Troubleshooting

### Model Loading Issues
```bash
# Check if model.pkl exists
ls -la model.pkl

# Verify model format
python -c "import pickle; m = pickle.load(open('model.pkl','rb')); print(type(m)); print(m.get_params())"
```

### Port Already in Use
```bash
# Find process using port 8501
lsof -i :8501

# Kill the process
kill -9 <PID>
```

### Memory Issues
- Reduce model size if needed
- Use `@st.cache_resource` for expensive operations
- Consider model optimization with `sklearn.tree.export_graphviz`

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📧 Support

For questions or issues:
1. Check the [Streamlit documentation](https://docs.streamlit.io)
2. Review sklearn documentation for model details
3. Check the troubleshooting section above

---

## 🎉 Success Checklist

- [ ] Model file (`model.pkl`) is present
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] App runs successfully (`streamlit run app.py`)
- [ ] Browser opens at `http://localhost:8501`
- [ ] Predictions work correctly
- [ ] Visualizations display properly
- [ ] Sample data testing functional

## 🚀 Next Steps

1. **Test thoroughly** with various inputs
2. **Customize the UI** to match your brand
3. **Add more features** if needed
4. **Deploy to Streamlit Cloud** for public access
5. **Monitor usage** and improve based on feedback

---

**Built with ❤️ using Streamlit and Scikit-learn**

