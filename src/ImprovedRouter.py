"""

INTELLIGENT MODEL ROUTER
COMPS 333F Final Project
Built By: Maria Dharshini (sID: 13126390)

[**Inferences based on performance evaluation conducted using AnythingLLM**]

From the results:
- gt-oss:20b : Best solution quality (but SLOWER)
- deepseek-r1:14b : Great quality and fast
- llama2-chinese: Basic quality (but FASTEST)

(NOTE: All comparisons are made comparatively)

PROBLEM STATEMENT: Using the same model to answer every time of question may not provide the most efficient answer
in the way that is required by user.

IDEA: What if we can optimize the code in such a way that based on the criteria of question received, we can route to
the most efficient LLM model that can provide the more optimal solution (based on explanation, structure and other details)

"""

class ImprovedRouter:
    """
    Smart Router Model that will select the optimal LLM model
    based on question content and complexity
    """
    def __init__(self):
        #Our models used for testing on AnythingLLM
        self.model_performance = {
            "gt-oss:20b": {"quality":10, "speed": 7.0},
            "deepseek-r1:14b": {"quality":9, "speed": 5.0},
            "llama2-chinese": {"quality": 6.3, "speed": 2.0}
        }
        
        #Patterns recognized from course content testing: Using COMPS333F_LAB3_SOLUTIONS
        self.technical_indicators = [
            'deterministic', 'environment', 'dimension', 'performance',
            'evaluation', 'analysis', 'classification', 'probablity',
            'statistical', 'algorithm', 'complexity', 'search'
        ]
        
        #Indicators if model needs to Explain more
        self.explanation_indicators = [
            'explain', 'analyze', 'describe', 'why',
            'how', 'discuss', 'compare', 'contrast',
        ]
        
        #Indicators if model needs a very short answer
        self.simple_terms = [
            'what is', 'when', 'where', 'list', 'define',
            'name', 'identify', 'briefly', 'summarize'
        ]
        
    def analyze_question(self, question: str) -> dict:
        """
        Used to analyze the type of question based on test patterns
        """
        question_lower = question.lower()
        
        #Count no of matching terms to a criteria of question
        tech_count = sum(1 for term in self.technical_indicators if term in question_lower)
        explain_count = sum(1 for term in self.explanation_indicators if term in question_lower)
        simple_count = sum(1 for term in self.simple_terms if term in question_lower)
        
        #Complexity of question based on length of question
        word_count = len(question.split())
        if word_count > 25 or tech_count > 2:
            complexity = "complex"
        elif word_count > 15 or explain_count > 1:
            complexity = "medium"
        else:
            complexity = "simple"
        
        return {
            "tech_count": tech_count,
            "explain_count": explain_count,
            "simple_count": simple_count,
            "complexity": complexity,
            "word_count": word_count
        }
    
    def select_optimal_model(self, question: str) -> str:
        """
        Selects optimal model based on our score-based decision logic
        """
        analysis = self.analyze_question(question)
        
        #DECISION TREE LOGIC TO SELECT OPTIMAL MODEL BASED ON COUNTS(or scores)
        if analysis["tech_count"] >= 2:
            return "gt-oss:20b" #BEST FOR TECHNICAL CONTENT
        elif analysis["explain_count"] >= 1:
            return "deepseek-r1:14b" #BEST FOR EXPLANATIONS
        elif analysis["simple_count"] >= 1 or analysis["complexity"] == "simple":
            return "llama2-chinese" #BEST FOR SHORT AND SIMPLE ANSWERS
        else:
            #DEFAULT BALANCED MODEL OFFERING GOOD RESPONSES + FAST RESPONSES
            return "deepseek-r1:14b"
        
    def get_routing_decision(self, question: str) -> str:
        """
        Routing to optimal model with appropriate counts (or scores)
        """
        best_model = self.select_optimal_model(question)
        analysis = self.analyze_question(question)
        model_info = self.model_performance[best_model]
        
        print(f"Question: {question}")
        print(f"Scores: Tech={analysis['tech_count']}, Exp={analysis['explain_count']}, Simple={analysis['simple_count']}")
        print(f"Complexity: {analysis['complexity']} ({analysis['word_count']} words)")
        print(f"Selected: {best_model} (Quality: {model_info['quality']}/10, Speed: {model_info['speed']}s)")
        print("-" * 50)
    
    def improvement_metrics(self):
        """
        To indicate the improvement of routing to the optimal LLM model
        """
        #Test questions used initially in AnythingLLM
        test_questions = [
            "What is the PEAS description of automated taxi drivers?",
            "Explain why Poker is Non-Deterministic?",
            "Analyze the six standard environment type dimensions for Medical Diagnosis"
        ]
        
        #Initializing time and quality variables
        manual_total_time = 0
        auto_total_time = 0
        manual_total_quality = 0
        auto_total_quality = 0
        
        print("PERFORMANCE COMPARISON - BASED ON SCORES ROUTING")
        print("-" * 60)
        
        for question in test_questions:
            manual_model = "gt-oss:20b"
            auto_model = self.select_optimal_model(question)
            
            manual_perf = self.model_performance[manual_model]
            auto_perf = self.model_performance[auto_model]
            
            manual_total_time += manual_perf["speed"]
            auto_total_time += auto_perf["speed"]
            
            manual_total_quality += manual_perf["quality"]
            auto_total_quality += auto_perf["quality"]
            
            analysis = self.analyze_question(question)
            print(f"\nQuestion: {question}")
            print(f"Analysis: Tech={analysis['tech_count']}, Exp={analysis['explain_count']}, Simple={analysis['simple_count']}")
            print(f"Manual: {manual_model} ({manual_perf['speed']}s, {manual_perf['quality']}/10)")
            print(f"Auto: {auto_model} ({auto_perf['speed']}s, {auto_perf['quality']}/10)")
            print(f"Improvement: {manual_perf['speed'] - auto_perf['speed']:.1f}s faster")
        
        #OVERALL IMPROVEMENT
        avg_manual_time = manual_total_time / 3
        avg_auto_time = auto_total_time / 3
        time_improvement = ((avg_manual_time - avg_auto_time) / avg_manual_time) * 100
        
        print(f"\nOVERALL RESULTS FROM OUR SCORE-BASED SYSTEM:")
        print(f"Average response time: {avg_manual_time:.1f}s → {avg_auto_time:.1f}s")
        print(f"Performance improvement: {time_improvement:.1f}% faster")
        print(f"Quality impact: {manual_total_quality/3:.1f}/10 → {auto_total_quality/3:.1f}/10")
    
#DEMO
def demonstrate_system():
    """
    Demonstrate SMART MODEL ROUTER
    """
    router = ImprovedRouter()
    print("SMART MODEL ROUTER SYSTEM")
    print("=" * 60)
    print("Using tech_count, explain_count, simple_count for decisions")
    print("="*60)

    test_cases = [
        "What is the PEAS description of automated taxi drivers?",
        "Explain why Poker is Non-Deterministic?",
        "Analyze the six standard environment type dimensions for Medical Diagnosis",
        "What does Partially Observable mean?",
        "Describe PEAS full form"
        ]
        
    for i, question in enumerate(test_cases, 1):
        print(f"\n{i}.", end="")
        router.get_routing_decision(question)

if __name__ == "__main__":
    demonstrate_system()
    print("\n" + "=" * 60)
    router = ImprovedRouter()
    router.improvement_metrics()
