from pathlib import Path
from kb_loader import load_rules
from engine import ForwardChainingEngine


KB_PATH = Path("kb") / "laptop_rules.json"


def ask(question):
    answer = input(question + " (y/n): ").strip().lower()
    return answer.startswith("y")


def collect_initial_facts():
    facts = []

    if ask("Is portability important?"):
        facts.append("portable")

    if ask("Do you need long battery life?"):
        facts.append("long_battery")

    print("\nChoose your budget")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    budget = input("Enter 1, 2, or 3: ").strip()

    if budget == "1":
        facts.append("budget_low")
    elif budget == "2":
        facts.append("budget_medium")
    elif budget == "3":
        facts.append("budget_high")

    if ask("Will you use the laptop for gaming?"):
        facts.append("gaming")

    if ask("Will you use it for creative work?"):
        facts.append("creative_work")

    if ask("Will you use it mainly for office work?"):
        facts.append("office_only")

    print("\nPreferred operating system:")
    print("1. Windows")
    print("2. macOS")
    print("3. Linux")

    os_choice = input("Enter 1, 2, or 3: ").strip()

    if os_choice == "1":
        facts.append("pref_os_windows")
    elif os_choice == "2":
        facts.append("pref_os_macos")
    elif os_choice == "3":
        facts.append("pref_os_linux")

    if ask("Do you need AI acceleration?"):
        facts.append("needs_ai_accel")

    if ask("Do you need a large screen?"):
        facts.append("large_screen")

    if ask("Do you travel often?"):
        facts.append("travel_often")

    return facts


def main():
    print("--- Laptop Advisor Expert System ---")

    rules = load_rules(str(KB_PATH))

    engine = ForwardChainingEngine(rules)

    facts = collect_initial_facts()

    engine.assert_facts(facts)
    engine.run()

    results = engine.conclusions()

    print("\n--- Results ---")

    if results["recommendations"]:
        for recommendation in results["recommendations"]:
            print("Recommendation:", recommendation)
    else:
        print("No specific laptop recommendation found.")

    if results["specs"]:
        print("\nSuggested Specifications:")
        for spec in results["specs"]:
            print("-", spec)

    print("\n--- Fired Rules ---")

    if engine.trace:
        for step in engine.trace:
            print("Rule:", step["rule"])
            print("Conditions:", ", ".join(step["antecedents"]))
            print("Result:", step["consequent"])
            print()
    else:
        print("No rules fired.")


if __name__ == "__main__":
    main()

