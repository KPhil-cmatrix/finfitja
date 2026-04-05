# FinFit JA  
A custom GPT-powered banking assistant designed for the Jamaican financial sector.  


## Assignment Description  
This project was developed as part of the major project requirements for the Intelligent Systems (ITT401) course at the University of the Commonwealth Caribbean by Khalia Phillips, a fourth-year Bachelor of Science in Information Technology student.  

The project focuses on the design and implementation of a functional web-based system that integrates a Jamaican domain-specific custom GPT, supported by interactive user interfaces, structured development documentation, and a comprehensive evaluation of system performance.  


## Purpose  
FinFit JA was created to simplify how users access and understand banking information within the Jamaican financial space.  

In many cases, individuals are required to search across multiple bank websites to compare account features, fees, and requirements. This process can be time-consuming and often confusing, especially for users who may not be familiar with financial terminology. FinFit JA addresses this gap by providing a centralized platform where users can receive structured, relevant, and easy-to-understand assistance.  

Through the system, users are able to better understand banking concepts, receive tailored account recommendations, compare available options, and ultimately make more informed financial decisions.  


## How It Works  
FinFit JA operates using a structured, dataset-driven approach rather than relying on general AI responses.  

When a user interacts with the system, whether through a chat query or a form submission, the input is converted into a structured prompt and sent to a backend large language model via the AnythingLLM API. The model then retrieves relevant information from curated banking datasets and applies predefined decision logic to generate responses that are both consistent and contextually appropriate.  

The system is designed around three main types of user interaction. Users may ask informational questions through the Ask FinFit interface, generate personalized recommendations through the Recommendation Generator, or perform structured comparisons using the Comparison Profile. Each of these components is designed to guide the user toward clearer understanding and more confident decision-making.  

It is important to note that all system responses are constrained to curated datasets. This design choice helps to improve accuracy, maintain consistency, and reduce the likelihood of hallucinated or misleading information.  


## Key Features
1. The **Ask FinFit** feature provides a chat-based interface where users can ask questions related to Jamaican banking, including account features, requirements, and general financial concepts. The interface supports guided prompts, maintains session-based chat history, and includes a refresh option for improved usability.  
   
2. The **Recommendation Generator** allows users to input their preferences and financial needs through an interactive form. Based on this input, the system produces a best-fit account recommendation, along with alternative options, key features, and a clear explanation of trade-offs.  

3. The **Comparison Profile** enables users to compare banks or specific account types side-by-side. The interface dynamically adjusts based on the selected comparison level, ensuring that the output remains structured, relevant, and easy to interpret.  

4. The **Dev Process** section outlines the overall development journey of the system, including data collection, data structuring, implementation of decision logic, system integration, interface design, testing, and iterative refinement. It also highlights key challenges encountered and the solutions applied throughout development.  

5. Finally, the **Performance Metrics** section presents the results of pilot testing in a structured format. These results evaluate the system based on accuracy, relevance, user satisfaction, response appropriateness, as well as overall efficiency and reliability.  


## Technology Stack  
The system was developed using the following technologies:  
- AnythingLLM (API Layer)
- OpenRouter (LLM Backend)   
- Pandas   
- Python  
- Requests 
- Streamlit (Frontend)  


## File Structure  
```bash
FinFit-JA/
├── app.py
├── layout.py
├── util/
│   └── api_call.py
├── pages/
│   ├── home.py
│   ├── chat.py
│   ├── matcher.py
│   ├── compare.py
│   ├── dev.py
│   └── metrics.py
```
The project is organized to separate core application logic, layout styling, API communication, and individual page functionality. The `app.py` file serves as the main entry point and controls navigation across the platform. The `layout.py` file manages shared interface elements such as banners, navigation styling, and page structure to ensure a consistent user experience. The `util/api_call.py` module handles communication with the backend model through the AnythingLLM API, acting as the bridge between the frontend and the LLM.  

The `pages` directory contains the individual functional components of the application. Each file represents a specific feature: `home.py` introduces the platform, `chat.py` manages informational queries, `matcher.py` handles personalized recommendations, `compare.py` enables structured comparisons, `dev.py` documents the development process, and `metrics.py` presents evaluation results. This modular structure improves maintainability, readability, and scalability of the system.


## Future Improvements
While FinFit JA demonstrated strong performance across all evaluation metrics, several areas for enhancement were identified. Key opportunities for future development include:
- Improved Query Interpretation: Strengthening the system’s ability to handle ambiguous or indirectly phrased queries by enhancing intent recognition and introducing clarification prompts for more accurate responses.
- Dataset Expansion and Updates: Continuously expanding the dataset to include more financial institutions, richer account details, and updated product information to ensure broader coverage and ongoing relevance within the Jamaican banking sector.
- Performance Optimization: Reducing response time for complex recommendation and comparison queries through improved API handling and backend efficiency.
- Personalization Features: Introducing user profiles, saved preferences, and interaction history to support more tailored recommendations and a more engaging user experience over time.
- Real-World Deployment and Feedback: Deploying the system in a live environment to collect user feedback and monitor performance, enabling continuous refinement of both the dataset and decision logic.
These improvements form the foundation for future versions of FinFit JA as a scalable, real-world financial assistant.


## License
This project is provided for academic and demonstration purposes. Users are encouraged to review the LICENSE file for further details regarding usage permissions and limitations.

## Disclaimer
FinFit JA is an academic prototype and is intended to provide general informational support and recommendation guidance within the Jamaican banking context. The system does not perform financial transactions, store sensitive banking credentials, or provide legally binding financial advice. Additionally, all information provided by the system is based on curated datasets and is accurate only as of March 2026.

Note: Users are strongly encouraged to verify all account details, terms, and conditions directly with the respective financial institutions before making any financial decisions.