# Laptop Advisor Expert System

## Project Description

This project implements a rule-based expert system in Python that recommends laptop types and specifications based on user requirements.

The system uses forward chaining to derive conclusions from facts and IF–THEN rules.

## How the System Works

1. The program asks the user questions about budget, portability, battery life, gaming, creative work, operating system, and other preferences.
2. User answers are stored as facts in working memory.
3. The inference engine compares the facts against the conditions of each rule.
4. When every condition of a rule is satisfied, the rule fires and adds its conclusion to working memory.
5. The engine continues until no additional rules can fire.
6. The program displays recommendations, suggested specifications, and the rules that produced them.

## Project Files

- `engine.py`: Implements the forward-chaining inference engine.
- `kb_loader.py`: Loads the IF–THEN rules from JSON.
- `kb/laptop_rules.json`: Contains the 10 laptop advisor rules.
- `main.py`: Collects user input and displays results.
- `tests/test_engine.py`: Tests the inference engine and rules.

## Forward-Chaining Example

Initial facts:

`budget_high`, `portable`, `long_battery`

Rule:

IF the budget is high AND portability is important AND long battery life is required, THEN recommend a premium ultrabook.

Conclusion:

`recommend:premium_ultrabook`

## Rule Priority

Rules have priorities. When multiple rules can fire, the engine selects the highest-priority rule first. If priorities are equal, the engine uses their original order in the knowledge base.

All applicable rules can eventually fire, so multiple recommendations or specifications may be produced.

## Running the Program

Open a terminal in the project folder and run:

cd expert_system_teaching_version
python3 main.py
Since I uploaded the files directly instead of cloning, you have to move inside expert_system_teaching_version and then running the main.py.

For test cases run:
cd expert_system_teaching_version
python3 -m unittest discover -s tests -p 'testcases.py' -v
make sure to be in expert_system_teaching_version

Answer the questions using `y` or `n` and select your budget and operating system.


## Conclusion

This project demonstrates how a knowledge-based expert system can use forward chaining to make decisions. It separates rules from the reasoning engine, allowing the knowledge base to be expanded without changing the core inference logic.